install.packages(
  c(
    "languageserver",  # R language server for VS Code
    "ggpubr",          # plot theming
    "fgsea",           # GSEA
    "mulea",            # ORA
    "plotly"
  ),
  dependencies = TRUE,
  repos = "https://cloud.r-project.org",
  Ncpus = parallel::detectCores()
)

if (!requireNamespace("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager", repos = "https://cloud.r-project.org")
}

BiocManager::install(
  c(
    "DESeq2",
    "apeglm",
    "EnhancedVolcano",
    "KEGGREST"
  ),
  update = FALSE,
  ask = FALSE
)
