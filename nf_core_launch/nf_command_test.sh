export NXF_VER=24.10.0 nextflow run 'https://github.com/nf-core/rnaseq' \
    -name 'test' \
    --outdir '../outdir/nf_core_output' \
    -r 3.16.1 \
    -profile test,docker