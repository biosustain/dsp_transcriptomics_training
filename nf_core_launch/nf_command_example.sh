nextflow run 'https://github.com/nf-core/rnaseq' \
    -name 'name_of_run' \
    --outdir 'path_to_outdirectory' \
    --input 'path_to_input_csv_file' \
    --fasta 'path_to_genome_fasta_file' \
    --gtf 'path_to_genome_annotation_gtf_file' \
    -r 3.16.1 \
    -profile docker