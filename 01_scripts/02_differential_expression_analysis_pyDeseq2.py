# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: pydeseq2
#     language: python
#     name: python3
# ---

# %% [markdown]
# # RNA-seq Differential Expression Analysis with pyDESeq2
#
# This notebook reproduces the treatment vs control DE workflow from the R DESeq2 report using Python and pyDESeq2.

# %% [markdown]
# ## 1. Setup
# Install dependencies if needed, then import libraries.

# %%
# If needed, uncomment and run:
# conda create -n pydeseq2 python pip
# conda activate pydeseq2
# # %pip install pydeseq2 pandas numpy matplotlib seaborn scipy ipykernel

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
from scipy.stats import zscore

sns.set_context("notebook")
sns.set_style("whitegrid")

# %% [markdown]
# ## 2. Load counts and metadata
#
# Expected files:
# - `data/nf-core_rnaseq/salmon.merged.gene_counts.tsv`
# - `data/metadata/metadata.tsv`

# %%
project_root = Path.cwd().resolve()
if not (project_root / ".git").exists():
    # Support running from subfolders
    for parent in [project_root, *project_root.parents]:
        if (parent / ".git").exists():
            project_root = parent
            break

counts_path = project_root / "data" / "nf-core_rnaseq" / "salmon.merged.gene_counts.tsv"
meta_path = project_root / "data" / "metadata" / "metadata.tsv"

counts_raw = pd.read_csv(counts_path, sep="\t")
metadata = pd.read_csv(meta_path, sep="\t")

print("Counts matrix shape (raw):", counts_raw.shape)
print("Metadata shape:", metadata.shape)
display(metadata.head())

# %% [markdown]
# ## 3. Build pyDESeq2 inputs
#
# pyDESeq2 expects:
# - `counts`: samples x genes integer count matrix
# - `metadata`: sample-level design table indexed by sample IDs
#
# The nf-core merged table may contain non-integer estimated counts; we round to nearest integer for DE modeling.

# %%
# Align metadata and count columns
metadata = metadata.rename(columns={"group": "condition"}).copy()
metadata["sample"] = metadata["sample"].astype(str)
metadata["condition"] = pd.Categorical(
    metadata["condition"], categories=["control", "treatment"], ordered=True
)
metadata = metadata.set_index("sample")

sample_cols = metadata.index.tolist()
required_cols = {"gene_id", "gene_name", *sample_cols}
missing = required_cols.difference(counts_raw.columns)
if missing:
    raise ValueError(f"Missing expected columns in counts file: {sorted(missing)}")

counts_genes = counts_raw.set_index("gene_id")[sample_cols]

# Convert to integer counts for DESeq2-like NB model
counts_genes = counts_genes.apply(pd.to_numeric, errors="coerce").fillna(0)
counts_genes_int = counts_genes.round().astype(int)

# pyDESeq2 needs samples x genes
counts_py = counts_genes_int.T

print("Counts for pyDESeq2 (samples x genes):", counts_py.shape)
print("Conditions:", metadata["condition"].value_counts().to_dict())
display(counts_py.iloc[:3, :5])

# %% [markdown]
# ## 4. Run pyDESeq2
#
# Contrast: treatment vs control

# %%
dds = DeseqDataSet(
    counts=counts_py,
    metadata=metadata[["condition"]],
    design_factors="condition",
    refit_cooks=True,
)
dds.deseq2()

stats = DeseqStats(dds, contrast=["condition", "treatment", "control"])
stats.summary()

res_df = stats.results_df.copy()
res_df.index.name = "gene"
res_df = res_df.reset_index().sort_values("padj", na_position="last")
display(res_df.head())

# %% [markdown]
# ## 5. LFC shrinkage and significant genes
#
# Use shrunken log2 fold changes for ranking and plotting.

# %%
stats

# %%
# pyDESeq2 shrinkage updates stats.results_df
stats.lfc_shrink(coeff="condition[T.treatment]")
res_shrunk = stats.results_df.copy()
res_shrunk.index.name = "gene"
res_shrunk = res_shrunk.reset_index().sort_values("padj", na_position="last")

res_shrunk = res_shrunk.dropna(subset=["padj"])
res_sig = res_shrunk[
    (res_shrunk["padj"] < 0.05) & (res_shrunk["log2FoldChange"].abs() >= 1)
].copy()

print("Total genes tested      :", len(res_shrunk))
print("Significant genes       :", len(res_sig))
print("Upregulated (LFC >= 1) :", int((res_sig["log2FoldChange"] >= 1).sum()))
print("Downregulated (LFC <= -1):", int((res_sig["log2FoldChange"] <= -1).sum()))
display(res_sig.head(10))

# %% [markdown]
# ## 6. Volcano and MA plots

# %%
plot_df = res_shrunk.copy()
plot_df["significance"] = np.where(
    (plot_df["padj"] < 0.05) & (plot_df["log2FoldChange"] >= 1),
    "Up",
    np.where(
        (plot_df["padj"] < 0.05) & (plot_df["log2FoldChange"] <= -1), "Down", "NS"
    ),
)
plot_df["neglog10_padj"] = -np.log10(plot_df["padj"].clip(lower=1e-300))

fig, ax = plt.subplots(figsize=(9, 6))
palette = {"Up": "#d7191c", "Down": "#2c7bb6", "NS": "lightgray"}
sns.scatterplot(
    data=plot_df,
    x="log2FoldChange",
    y="neglog10_padj",
    hue="significance",
    palette=palette,
    alpha=0.7,
    s=20,
    linewidth=0,
    ax=ax,
)
ax.axvline(-1, ls="--", c="black", lw=1)
ax.axvline(1, ls="--", c="black", lw=1)
ax.axhline(-np.log10(0.05), ls="--", c="black", lw=1)
ax.set_title("Volcano Plot - Treatment vs Control")
ax.set_xlabel("log2(Fold Change)")
ax.set_ylabel("-log10(adjusted p-value)")
plt.legend(title="")
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(9, 6))
sns.scatterplot(
    data=plot_df,
    x="baseMean",
    y="log2FoldChange",
    hue="significance",
    palette=palette,
    alpha=0.7,
    s=20,
    linewidth=0,
    ax=ax,
)
ax.set_xscale("log")
ax.axhline(-1, ls="--", c="black", lw=1)
ax.axhline(1, ls="--", c="black", lw=1)
ax.axhline(0, ls="-", c="gray", lw=1)
ax.set_title("MA Plot - Treatment vs Control (shrunken LFC)")
ax.set_xlabel("Mean normalized count (baseMean)")
ax.set_ylabel("log2 Fold Change")
plt.legend(title="")
plt.tight_layout()
plt.show()


# %% [markdown]
# ## 7. Top gene count plot and heatmap
#
# Uses normalized counts from pyDESeq2 output object.


# %%
def get_norm_counts(dds_obj):
    if hasattr(dds_obj, "layers") and "normed_counts" in dds_obj.layers:
        arr = dds_obj.layers["normed_counts"]
        return pd.DataFrame(arr, index=dds_obj.obs_names, columns=dds_obj.var_names)
    if hasattr(dds_obj, "normed_counts"):
        arr = dds_obj.normed_counts
        return pd.DataFrame(arr, index=dds_obj.obs_names, columns=dds_obj.var_names)
    raise AttributeError("Could not find normalized counts in dds object.")


norm_counts = get_norm_counts(dds)

if len(res_sig) > 0:
    top_gene = res_sig.iloc[0]["gene"]
    top_gene_df = norm_counts[[top_gene]].join(metadata[["condition"]])

    fig, ax = plt.subplots(figsize=(6, 5))
    sns.boxplot(data=top_gene_df, x="condition", y=top_gene, ax=ax)
    sns.stripplot(
        data=top_gene_df, x="condition", y=top_gene, color="black", alpha=0.7, ax=ax
    )
    ax.set_title(f"Normalized counts - {top_gene}")
    ax.set_xlabel("Condition")
    ax.set_ylabel("Normalized count")
    plt.tight_layout()
    plt.show()

    top_n = min(50, len(res_sig))
    top_genes = res_sig.head(top_n)["gene"].tolist()
    heat_df = norm_counts[top_genes].T
    heat_df = (
        heat_df.apply(
            lambda s: pd.Series(zscore(s, ddof=1), index=s.index),
            axis=1,
            raw=False,
            result_type="expand",
        )
        .replace([np.inf, -np.inf], np.nan)
        .fillna(0)
    )

    col_colors = metadata["condition"].map(
        {"control": "#2c7bb6", "treatment": "#d7191c"}
    )
    sns.clustermap(
        heat_df,
        cmap="RdBu_r",
        center=0,
        col_colors=col_colors,
        xticklabels=True,
        yticklabels=True,
        figsize=(10, 12),
    )
    plt.suptitle("Top DE genes - Treatment vs Control (row z-score)", y=1.02)
    plt.show()
else:
    print("No significant genes at padj < 0.05 and |log2FC| >= 1.")

# %% [markdown]
# ## 8. Save pyDESeq2 results

# %%
results_dir = project_root / "results"
results_dir.mkdir(parents=True, exist_ok=True)

all_out = results_dir / "DE_treatment_vs_control_all_pydeseq2.tsv"
sig_out = results_dir / "DE_treatment_vs_control_significant_pydeseq2.tsv"

res_shrunk.to_csv(all_out, sep="\t", index=False)
res_sig.to_csv(sig_out, sep="\t", index=False)

print("Saved:", all_out)
print("Saved:", sig_out)

# %% [markdown]
# ## 9. Optional comparison with existing R DESeq2 output

# %%
r_sig_path = project_root / "results" / "DE_treatment_vs_control_significant.tsv"
if r_sig_path.exists():
    r_sig = pd.read_csv(r_sig_path, sep="\t")
    overlap = len(set(r_sig["gene"]).intersection(set(res_sig["gene"])))
    print("R DESeq2 significant genes:", len(r_sig))
    print("pyDESeq2 significant genes:", len(res_sig))
    print("Overlap:", overlap)
else:
    print("R DESeq2 significant file not found, skipping comparison.")

# %%
