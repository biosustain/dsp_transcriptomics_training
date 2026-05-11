install.packages(
  c(
    "languageserver",  # R language server for VS Code
    "bookdown",
    "dplyr",
    "DT",
    "ggplot2",
    "ggpubr",
    "ggrepel",
    "here",
    "kableExtra",
    "pheatmap",
    "RColorBrewer",
    "rmarkdown",
    "tidyr",
    "plotly",
    "remotes"
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
    "KEGGREST",
    "fgsea"
  ),
  update = FALSE,
  ask = FALSE
)

# mulea is not on CRAN — install from GitHub
remotes::install_github("ELTEbioinformatics/mulea")
