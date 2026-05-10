# Run FastQC
fastqc SRR23955798_1.fastq -o fastqc_results/

# Run MultiQC
multiqc fastqc_results/*.zip -o multiqc_results/