import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

sra_numbers = ["SRR23955797", "SRR23955798", "SRR23955799" ]

parallel_jobs = 1
threads_per_job = 4

def process_srr(sra_id):
    print(f"\n=== Processing: {sra_id} ===")
    start = time.time()
    
#Step1: Download
    subprocess.call(f"prefetch {sra_id}", shell=True)
    
#Step2 : Convert (FASTEST way)
    subprocess.call(
        f"fasterq-dump {sra_id} --split-files --threads {threads_per_job} -O fastq",
        shell=True
    )
    
#Step3: Compress (parallel compression)
    subprocess.call(
        f"pigz -p {threads_per_job} fastq/{sra_id}*.fastq",
        shell=True
    )

    end = time.time()
    print(f"⏱ {(end-start)/60:.2f} min")
    
#Run jobs in parallel
with ThreadPoolExecutor(max_workers=parallel_jobs) as executor:
    executor.map(process_srr, sra_numbers)
