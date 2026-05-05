  ## Script to sub-sample 50 000 reads of fastq files randomly
  # Reduces the size of fastq files and thus allows processing in the training environment
  # Use sektk (https://github.com/lh3/seqtk); keep random seeds constant for both fastq files: -s100)
  
  seqtk sample -s100 SRR30606311_1.fastq 50000 > SRR30606311_1_sub_50k.fastq
  seqtk sample -s100 SRR30606311_2.fastq 50000 > SRR30606311_2_sub_50k.fastq

  seqtk sample -s100 SRR30606312_1.fastq 50000 > SRR30606312_1_sub_50k.fastq
  seqtk sample -s100 SRR30606312_2.fastq 50000 > SRR30606312_2_sub_50k.fastq

  seqtk sample -s100 SRR30606313_1.fastq 50000 > SRR30606313_1_sub_50k.fastq
  seqtk sample -s100 SRR30606313_2.fastq 50000 > SRR30606313_2_sub_50k.fastq

  seqtk sample -s100 SRR30606314_1.fastq 50000 > SRR30606314_1_sub_50k.fastq
  seqtk sample -s100 SRR30606314_2.fastq 50000 > SRR30606314_2_sub_50k.fastq

  seqtk sample -s100 SRR30606315_1.fastq 50000 > SRR30606315_1_sub_50k.fastq
  seqtk sample -s100 SRR30606315_2.fastq 50000 > SRR30606315_2_sub_50k.fastq

  seqtk sample -s100 SRR30606316_1.fastq 50000 > SRR30606316_1_sub_50k.fastq
  seqtk sample -s100 SRR30606316_2.fastq 50000 > SRR30606316_2_sub_50k.fastq



