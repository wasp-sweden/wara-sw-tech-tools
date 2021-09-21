from pathlib import Path
import os

def get_results_files(project, tool):
	results_dir = Path(os.environ["OVE_BASE_DIR"], "results", project)
	return list(results_dir.glob(tool + "-*.json"))

