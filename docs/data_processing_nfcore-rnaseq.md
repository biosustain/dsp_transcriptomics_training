
# 2.3. Data processing using the nf-core/rnaseq pipeline
This section details the steps to perform RNAseq data processing using the nf-core/rnaseq pipeline.

## Sources of data and genome files
RNAseq analysis of *Escherichia coli* str. K-12 substr. MG1655 (accession: GCF_000005845.2) will be performed. RNA sequencing read files and genome files were obtained from the following links. The data do not have to be downloaded. We have already deposited a size-reduced data set as well as the genome files in the repository.  

[RNAseq files (.fastq.gz) - PRJNA1158806](https://www.ebi.ac.uk/ena/browser/view/PRJNA1158806)  

[*E. coli* genome sequence (.fna.gz)](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz) 

[*E. coli* genome annotation file (.gtf.gz)](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gtf.gz)  

## Running the nf-core/rnaseq pipeline v3.23.0
We will not process the original data set because more computing power would be required. Instead, we will process only two size-reduced samples where 50 000 reads were randomly sampled from the original data (used script for sub-sampling: ```util/subsample_50k_PRJNA1158806.sh```).  
We will use pipeline release [v3.23.0](https://nf-co.re/rnaseq/3.23.0). From this release, it is possible to use Bowtie2 for read alignment which is advantageous to process prokayotic RNAseq data. For simplicity, we specify a "prokaryotic" profile which automatically uses Bowtie2 for read alignment and Salmon for read quantification.  

To process the data, we will use the following command:  
```
nextflow run 'https://github.com/nf-core/rnaseq' \
    -name 'Ecoli_MG1655_saccharin_2_samples' \
    --outdir '/workspaces/dsp_transcriptomics_training/results/nfcore_rnaseq_processing_subsampled' \
    --input '/workspaces/dsp_transcriptomics_training/data/seq_files_subsampled/samplesheet_50k_subsampled_2samples.csv' \
    --fasta '/workspaces/dsp_transcriptomics_training/data/genome_files/GCF_000005845.2_ASM584v2_genomic.fna.gz' \
    --gtf '/workspaces/dsp_transcriptomics_training/data/genome_files/GCF_000005845.2_ASM584v2_genomic.gtf.gz' \
    -r 3.23.0 \
    -profile prokaryotic,docker \
    -c /workspaces/dsp_transcriptomics_training/01_scripts/custom.config 
```  

```-name```: name of the processing run  
```--outdir```: (absolute) path to the outfile directory where results will be saved (the sub-directory is created automatically)  
```--ìnput```: (absolute) path to the sample sheet  
```--fasta```: (absolute) path to the gzipped genome fasta file  
```--gtf```: (absolute) path to gzipped genome annotation file  
```-r```: nf-core/rnaseq pipeline release/version  
```-profile```: profile(s) to run; here "prokaryotic" mode using "docker"  
```-c```: (absolute) path to the custom configuration file; used here to limit the number of CPUs and memory  

The nextlow command is stored in a bash script and can be executed by running the following command in the terminal:  
```
bash 01_scripts/00_nfcore_rnaseq_processing.sh
```  
The processing time is about 7 minutes.  

#### Automatic generation of configuration files
There are many parameters of the pipeline that can be customized. Rather than doing this manually, nf-core offers the possibility to generate the parameter configuration automatically [here](https://nf-co.re/rnaseq/3.23.0). Press the button ```Launch version 3.23.0``` to see all pipeline parameters and change as needed. A configuration file can be generated automatically that can be used with a nextflow command for pipeline configuration.


## Structure of the outfile directory
The results of the pipeline run will be saved in the folder ```results/nfcore_rnaseq_processing_subsampled```. The folder structure is as follows:  
```
.
├── bowtie2_salmon
├── fastqc
├── fq_lint
├── multiqc
├── pipeline_info
└── trimgalore
```

### Detailed structure of the outfile directory
```
.
├── bowtie2_salmon
│   ├── control_1
│   │   ├── aux_info
│   │   ├── cmd_info.json
│   │   ├── libParams
│   │   ├── logs
│   │   ├── quant.genes.sf
│   │   └── quant.sf
│   ├── control_1.markdup.sorted.bam
│   ├── control_1.markdup.sorted.bam.bai
│   ├── deseq2_qc
│   │   ├── deseq2.dds.RData
│   │   ├── deseq2.pca.vals.txt
│   │   ├── deseq2.plots.pdf
│   │   ├── deseq2.sample.dists.txt
│   │   ├── R_sessionInfo.log
│   │   └── size_factors
│   ├── log
│   │   ├── control_1.bowtie2.log
│   │   └── saccharin_1.bowtie2.log
│   ├── picard_metrics
│   │   ├── control_1.markdup.sorted.MarkDuplicates.metrics.txt
│   │   └── saccharin_1.markdup.sorted.MarkDuplicates.metrics.txt
│   ├── saccharin_1
│   │   ├── aux_info
│   │   ├── cmd_info.json
│   │   ├── libParams
│   │   ├── logs
│   │   ├── quant.genes.sf
│   │   └── quant.sf
│   ├── saccharin_1.markdup.sorted.bam
│   ├── saccharin_1.markdup.sorted.bam.bai
│   ├── salmon.merged.gene_counts_length_scaled.tsv
│   ├── salmon.merged.gene_counts_scaled.tsv
│   ├── salmon.merged.gene_counts.tsv
│   ├── salmon.merged.gene_lengths.tsv
│   ├── salmon.merged.gene.SummarizedExperiment.rds
│   ├── salmon.merged.gene_tpm.tsv
│   ├── salmon.merged.transcript_counts.tsv
│   ├── salmon.merged.transcript_lengths.tsv
│   ├── salmon.merged.transcript.SummarizedExperiment.rds
│   ├── salmon.merged.transcript_tpm.tsv
│   ├── salmon.merged.tx2gene.tsv
│   ├── samtools_stats
│   │   ├── control_1.markdup.sorted.bam.flagstat
│   │   ├── control_1.markdup.sorted.bam.idxstats
│   │   ├── control_1.markdup.sorted.bam.stats
│   │   ├── control_1.sorted.bam.flagstat
│   │   ├── control_1.sorted.bam.idxstats
│   │   ├── control_1.sorted.bam.stats
│   │   ├── saccharin_1.markdup.sorted.bam.flagstat
│   │   ├── saccharin_1.markdup.sorted.bam.idxstats
│   │   ├── saccharin_1.markdup.sorted.bam.stats
│   │   ├── saccharin_1.sorted.bam.flagstat
│   │   ├── saccharin_1.sorted.bam.idxstats
│   │   └── saccharin_1.sorted.bam.stats
│   └── stringtie
│       ├── control_1.ballgown
│       ├── control_1.coverage.gtf
│       ├── control_1.gene.abundance.txt
│       ├── control_1.transcripts.gtf
│       ├── saccharin_1.ballgown
│       ├── saccharin_1.coverage.gtf
│       ├── saccharin_1.gene.abundance.txt
│       └── saccharin_1.transcripts.gtf
├── fastqc
│   ├── raw
│   │   ├── control_1_raw_1_fastqc.html
│   │   ├── control_1_raw_1_fastqc.zip
│   │   ├── control_1_raw_2_fastqc.html
│   │   ├── control_1_raw_2_fastqc.zip
│   │   ├── saccharin_1_raw_1_fastqc.html
│   │   ├── saccharin_1_raw_1_fastqc.zip
│   │   ├── saccharin_1_raw_2_fastqc.html
│   │   └── saccharin_1_raw_2_fastqc.zip
│   └── trim
│       ├── control_1_trimmed_1_val_1_fastqc.html
│       ├── control_1_trimmed_1_val_1_fastqc.zip
│       ├── control_1_trimmed_2_val_2_fastqc.html
│       ├── control_1_trimmed_2_val_2_fastqc.zip
│       ├── saccharin_1_trimmed_1_val_1_fastqc.html
│       ├── saccharin_1_trimmed_1_val_1_fastqc.zip
│       ├── saccharin_1_trimmed_2_val_2_fastqc.html
│       └── saccharin_1_trimmed_2_val_2_fastqc.zip
├── fq_lint
│   ├── raw
│   │   ├── control_1.fq_lint.txt
│   │   └── saccharin_1.fq_lint.txt
│   └── trimmed
│       ├── control_1.fq_lint.txt
│       └── saccharin_1.fq_lint.txt
├── multiqc
│   └── bowtie2_salmon
│       ├── multiqc_report_data
│       ├── multiqc_report.html
│       └── multiqc_report_plots
├── pipeline_info
│   ├── execution_report_2026-05-15_15-41-45.html
│   ├── execution_timeline_2026-05-15_15-41-45.html
│   ├── execution_trace_2026-05-15_15-41-45.txt
│   ├── nf_core_rnaseq_software_mqc_versions.yml
│   ├── params_2026-05-15_15-42-05.json
│   └── pipeline_dag_2026-05-15_15-41-45.html
└── trimgalore
    ├── control_1_trimmed_1.fastq.gz_trimming_report.txt
    ├── control_1_trimmed_2.fastq.gz_trimming_report.txt
    ├── saccharin_1_trimmed_1.fastq.gz_trimming_report.txt
    └── saccharin_1_trimmed_2.fastq.gz_trimming_report.txt
```