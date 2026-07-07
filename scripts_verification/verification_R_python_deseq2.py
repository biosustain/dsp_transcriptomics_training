# Script to compare results from DEseq2 using R or Python packages
# Out put of script "01_scripts/02_differential_expression_analysis_pyDeseq2.ipynb"  is compared


# %%
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display


# %% data paths
results_r_path = '../results/DE_treatment_vs_control_all.tsv'
results_python_path = '../results/DE_treatment_vs_control_all_pydeseq2.tsv'

outdir_path = './outdir_verification'


# %% read data and add prefix
results_r = pd.read_csv(results_r_path, 
                        sep='\t').add_suffix('_R')
display(results_r)

results_python = pd.read_csv(results_python_path, 
                             sep='\t').add_suffix('_python')
display(results_python)


# %% log2FC comparison

#merge log2fc dataframes
log2fc_merged = pd.merge(
                left=results_r[['gene_R', 'log2FoldChange_R']], 
                right=results_python[['gene_python', 'log2FoldChange_python']], 
                left_on='gene_R', 
                right_on='gene_python', 
                how='outer'
                )
display(log2fc_merged)

#count NaN values per column and export as csv
log2fc_nan_counts = log2fc_merged.isna().sum()
display(log2fc_nan_counts)

log2fc_nan_counts.to_csv(f'{outdir_path}/log2fc_nan_counts.csv')

#calculate log2FC deviation of Python result from R result (difference and %):
# direction of interpretation is relative to R result (python minus R OR Python/R)
log2fc_merged['diff_log2fc'] = log2fc_merged['log2FoldChange_python'] - log2fc_merged['log2FoldChange_R']

log2fc_merged['ratio_log2fc'] = log2fc_merged['log2FoldChange_python'] / log2fc_merged['log2FoldChange_R']

display(log2fc_merged)

#export as csv
log2fc_merged.to_csv(
                    f'{outdir_path}/log2fc_differences_python_vs_R.csv', 
                    index=False
                    )

# create scatter plot --> fill NaN values with zero for plotting
plt.scatter(log2fc_merged['log2FoldChange_R'].fillna(0), 
            log2fc_merged['log2FoldChange_python'].fillna(0), 
            s=2
            )
plt.grid(True)
plt.xlabel('log2FoldChange_R')
plt.ylabel('log2FoldChange_python')
plt.title('log2FC in R and Python (NaN set to zero for visualisation)')

plt.savefig(f'{outdir_path}/log2FC_Python_vs_R.png', 
            dpi=300
            )
plt.show()



# %% padj comparison

#merge padj dataframes
padj_merged = pd.merge(
                left=results_r[['gene_R', 'padj_R']], 
                right=results_python[['gene_python', 'padj_python']], 
                left_on='gene_R', 
                right_on='gene_python', 
                how='outer'
                )
display(padj_merged)

#count NaN values per column and export as csv
padj_nan_counts = padj_merged.isna().sum()
display(padj_nan_counts)

log2fc_nan_counts.to_csv(f'{outdir_path}/padj_nan_counts.csv')

#calculate padj deviation of Python result from R result (difference and %):
# direction of interpretation is relative to R result (python minus R OR Python/R)
padj_merged['diff_padj'] = padj_merged['padj_python'] - padj_merged['padj_R']

padj_merged['ratio_padj'] = padj_merged['padj_python'] / padj_merged['padj_R']

display(padj_merged)

#export as csv
padj_merged.to_csv(
                    f'{outdir_path}/padj_differences_python_vs_R.csv', 
                    index=False
                    )

# create scatter plot --> fill NaN values with zero for plotting
plt.scatter(padj_merged['padj_R'].fillna(0), 
            padj_merged['padj_python'].fillna(0), 
            s=2
            )
plt.grid(True)
plt.xlabel('padj_R')
plt.ylabel('padj_python')
plt.title('padj in R and Python (NaN set to zero for visualisation)')

plt.savefig(f'{outdir_path}/padj_Python_vs_R.png', 
            dpi=300
            )
plt.show()


# %%
