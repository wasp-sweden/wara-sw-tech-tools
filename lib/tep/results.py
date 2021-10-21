from pathlib import Path
import os
import datetime

def get_results_files(tool, project):
	results_dir = Path(os.environ["RESULT_DIR"], tool)
	return list(results_dir.glob(project + "-*.json"))

# has the sneaky side effect of potentially creating the directory, sorry
def get_result_path(meta):
	path = Path(os.environ["RESULT_DIR"], meta["tool"], meta["tag"])
	path.mkdir(parents=True, exist_ok=True)
	return path.joinpath(f"{meta['tool']}-{meta['timestamp']}.json")
	

def create_metadata(tool, subject, tag = "default"):
	return {
		"tool": tool,
		"subject": subject,
		"tag": tag,
		"timestamp": datetime.datetime.now().isoformat(),
		"env": {
			"uname": os.uname()
		}
	}

def create_results(meta, results):
	return {
		"meta": meta,
		"results": results,
	}
