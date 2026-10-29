import os
import time
from datetime import datetime, timezone

job_name = os.getenv("JOB_NAME", "data-processing")

print(f"Starting job: {job_name}", flush=True)
print(f"Started at: {datetime.now(timezone.utc)}", flush=True)

for i in range(1, 6):
    print(f"Processing record {i}/5", flush=True)
    time.sleep(1)

print("Processing completed successfully!", flush=True)
