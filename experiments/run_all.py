"""Run the full pipeline: verification, falsification, figures."""
import subprocess
import sys

for script in ["experiments/verify_main.py", "experiments/falsify.py", "experiments/make_figures.py"]:
    print(f"=== {script} ===")
    r = subprocess.run([sys.executable, script], capture_output=False)
    if r.returncode != 0:
        raise SystemExit(f"{script} failed with code {r.returncode}")
print("Pipeline complete.")
