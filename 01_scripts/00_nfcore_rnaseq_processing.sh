# script to process RNA sequencing files
# We are using v3.23.0 of the nf-core/rnaseq pipeline with the profile "prokaryotic"
nextflow run 'https://github.com/nf-core/rnaseq' \
    -name 'Ecoli_MG1655_saccharin' \
    --outdir './results/nfcore_rnaseq_processing_subsampled' \
    --input './data/seq_files_subsampled/samplesheet_50k_subsampled_2samples.csv' \
    --fasta './data/genome_files/GCF_000005845.2_ASM584v2_genomic.fna.gz' \
    --gtf './data/genome_files/GCF_000005845.2_ASM584v2_genomic.gtf.gz' \
    -r 3.23.0 \
    -profile prokaryotic,docker \
    -c custom.config 