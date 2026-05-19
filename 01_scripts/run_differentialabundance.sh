#!/bin/bash

# =============================================================================
# nf-core/differentialabundance run script
# Study: MG1655 (E. coli deDios 2025 - PRJNA1158806)
# Working directory: /workspaces/dsp_transcriptomics_training
# =============================================================================

set -euo pipefail

nextflow run nf-core/differentialabundance \
    -r 1.5.0 \
    -profile docker \
    -params-file params_degs.json \
    --outdir results/differentialabundance
