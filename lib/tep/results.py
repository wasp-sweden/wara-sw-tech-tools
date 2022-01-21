from pathlib import Path
import os
import datetime
import subprocess
import re

def get_results_files(tool, project, tag="default"):
	"""Returns a list of all result files for specific tool, project and tag tuple.
	The project name may contain wildcards."""
	results_dir = Path(os.environ["RESULT_DIR"], tool, tag)
	return list(results_dir.glob(project + "-*.json"))

# has the sneaky side effect of potentially creating the directory, sorry
def get_result_path(meta):
	"""Returns the path where a result file should be saved, based on its metadata.
	May create the parent directories."""
	path = Path(os.environ["RESULT_DIR"], meta["tool"], meta["tag"])
	path.mkdir(parents=True, exist_ok=True)
	return path.joinpath(f"{meta['subject']}-{meta['timestamp']}.json")
	

def create_metadata(tool, subject, tag = "default"):
	"""Create a new metadata object used in the result format."""
	return {
		"tool": tool,
		"subject": subject,
		"tag": tag,
		"timestamp": datetime.datetime.now().isoformat(),
		"env": {
			"uname": os.uname()
		}
	}

def get_projects(pattern = None):
	"""Returns a list of projects matching the regex pattern. If no pattern is
	supplied, all projects are returned."""
	projects = os.environ["OVE_PROJECT_LIST"].split(" ")
	if pattern is not None:
		projects = [project for project in projects if re.fullmatch(pattern, project)]
	return projects

def create_results(meta, results):
	"""Combines a metadata object with its results data."""
	return {
		"meta": meta,
		"results": results,
	}
