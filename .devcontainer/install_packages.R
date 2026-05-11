install.packages(
  c(
    "languageserver",  # R language server for VS Code
    "ggpubr",          # plot theming
    "fgsea",           # GSEA
    "plotly",          # interactive plots
    "remotes"          # needed to install mulea from GitHub
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

# mulea is not on CRAN — install from GitHub
remotes::install_github("ELTEbioinformatics/mulea")