"""
Bluestock Mutual Fund Analytics Capstone
Master execution script for the data ingestion pipeline.
"""

from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent

SCRIPTS = [
    "data_ingestion.py",
    "data_quality_check.py",
    "fund_master_exploration.py",
    "live_nav_fetch.py",
]


def run_script(script_name):
    """Execute a project Python script and stop if it fails."""
    script_path = PROJECT_ROOT / script_name

    print(f"\nRunning {script_name}...")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{script_name} failed with exit code {result.returncode}"
        )


def main():
    """Run all project pipeline scripts in sequence."""
    for script in SCRIPTS:
        run_script(script)

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()