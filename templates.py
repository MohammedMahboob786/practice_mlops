import os
from pathlib import Path

# List of file paths to create
list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
    "src/exception/exception.py",
    "src/logger/logging.py"
]

# Loop through each file path and create directories and files if they don't exist
for file_path in list_of_files:
    file_path = Path(file_path)  # Convert string path to Path object
    file_dir = file_path.parent  # Get directory part of the path

    # Create directories if they do not exist
    if not file_dir.exists():
        file_dir.mkdir(parents=True, exist_ok=True)
        print(f"Directory created: {file_dir}")

    # Create the file if it does not exist
    if not file_path.exists():
        file_path.touch()  # This creates an empty file
        print(f"File created: {file_path}")
    else:
        print(f"File already exists: {file_path}")
