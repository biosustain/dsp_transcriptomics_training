# Install CRAN packages
install.packages(
  c(
    "Rcpp", "BH", "httr", "googledrive", "googlesheets4", "ragg",
    "rvest", "tidyverse", "readr", "pheatmap", "kableExtra", "plotly",
    "rmarkdown", "factoextra", "ggpubr", "remotes"
  ),
  dependencies = TRUE,
  repos = "https://cloud.r-project.org",
  Ncpus = parallel::detectCores()
)

# Install Bioconductor packages
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager", repos = "https://cloud.r-project.org")

BiocManager::install(
  c(
    "DESeq2", "AnnotationDbi", "org.Mm.eg.db", "msigdbr",
    "clusterProfiler", "DOSE", "europepmc", "enrichplot", "fgsea"
  ),
  Ncpus = parallel::detectCores()
)
