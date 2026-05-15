# Script to process RNA sequencing files
# We are using v3.23.0 of the nf-core/rnaseq pipeline with the profile "prokaryotic"
# A custom config file is used here to limit the number of CPUs and memory
nextflow run 'https://github.com/nf-core/rnaseq' \
    -name 'Ecoli_MG1655_saccharin_2_samples' \
    --outdir '/workspaces/dsp_transcriptomics_training/results/nfcore_rnaseq_processing_subsampled' \
    --input '/workspaces/dsp_transcriptomics_training/data/seq_files_subsampled/samplesheet_50k_subsampled_2samples.csv' \
    --fasta '/workspaces/dsp_transcriptomics_training/data/genome_files/GCF_000005845.2_ASM584v2_genomic.fna.gz' \
    --gtf '/workspaces/dsp_transcriptomics_training/data/genome_files/GCF_000005845.2_ASM584v2_genomic.gtf.gz' \
    -r 3.23.0 \
    -profile prokaryotic,docker \
    -c /workspaces/dsp_transcriptomics_training/01_scripts/custom.config 