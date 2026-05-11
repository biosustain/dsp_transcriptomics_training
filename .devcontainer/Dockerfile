FROM mcr.microsoft.com/devcontainers/base:noble
WORKDIR /home

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        software-properties-common \
        dirmngr \
        wget \
        ca-certificates \
    && wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc \
        | tee /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc \
    && echo "deb https://cloud.r-project.org/bin/linux/ubuntu noble-cran44/" \
        > /etc/apt/sources.list.d/cran-r44.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        r-base \
        r-base-dev \
        openjdk-21-jre \
        python3-venv \
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
