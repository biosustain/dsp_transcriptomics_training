FROM mcr.microsoft.com/devcontainers/base:noble

RUN apt-get update && apt-get install -y \
  build-essential \
  gfortran \
  libblas-dev \
  libcairo2-dev \
  libcurl4-openssl-dev \
  libfontconfig1-dev \
  libfreetype6-dev \
  libfribidi-dev \
  libglib2.0-dev \
  libglpk-dev \
  libgmp-dev \
  libharfbuzz-dev \
  libjpeg-dev \
  liblapack-dev \
  libmpfr-dev \
  libnlopt-dev \
  libpng-dev \
  libssl-dev \
  libtiff5-dev \
  libxml2-dev \
  libxt-dev \
  pkg-config \
  r-base-dev \
  zlib1g-dev

COPY install_packages.R /tmp/install_packages.R
RUN Rscript /tmp/install_packages.R && rm /tmp/install_packages.R
