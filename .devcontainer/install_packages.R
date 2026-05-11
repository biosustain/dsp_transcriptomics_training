install.packages(
  c(
    "languageserver",
    "ggpubr",
    "plotly",
    "remotes",
    "bookdown",
    "DT",
    "here",
    "kableExtra",
    "pheatmap"
  ),
  dependencies = TRUE,
  repos = "https://cloud.r-project.org",
  Ncpus = parallel::detectCores()
)

if (!requireNamespace("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager", repos = "https://cloud.r-project.org")
}

# Install Bioconductor packages — fgsea must come before mulea
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
