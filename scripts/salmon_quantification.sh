# Build Salmon index
salmon index -t transcriptome.fa -i salmon_index -k 31

# Run Salmon quantification
salmon quant \
  -i salmon_index \
  -l A \
  -1 sample1.fastq.gz \
  -2 sample2.fastq.gz \
  -p 12 \
  --validateMappings \
  -o salmon_out