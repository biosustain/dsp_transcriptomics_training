FROM mcr.microsoft.com/devcontainers/base:noble
WORKDIR /home

RUN apt-get update \
    && apt-get install -y \
        openjdk-21-jre \
        python3-venv \
        r-base \
        r-base-dev \
        r-cran-bookdown \
        r-cran-dplyr \
        r-cran-dt \
        r-cran-ggplot2 \
        r-cran-ggrepel \
        r-cran-here \
        r-cran-kableextra \
        r-cran-pheatmap \
        r-cran-rcolorbrewer \
        r-cran-rmarkdown \
        r-cran-tidyr \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libfontconfig1-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libfreetype6-dev \
        libpng-dev \
        libtiff5-dev \
        libjpeg-dev \
    && curl -L -s -o /usr/local/bin/nextflow \
        https://github.com/nextflow-io/nextflow/releases/download/v25.10.4/nextflow-25.10.4-dist \
    && chmod +x /usr/local/bin/nextflow \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && chmod -R 777 /usr/local/lib/R/site-library

COPY install_packages.R /tmp/install_packages.R
RUN Rscript /tmp/install_packages.R && rm /tmp/install_packages.R
