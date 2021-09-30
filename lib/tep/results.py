from pathlib import Path
import os

def get_results_files(tool, project):
	results_dir = Path(os.environ["RESULT_DIR"], tool)
	return list(results_dir.glob(project + "-*.json"))

