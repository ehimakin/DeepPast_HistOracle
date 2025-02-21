#Chronovisor. File and Folder setup
import os

# Define the project structure
folders = [
    "app/models",
    "app/utils",
    "app/inference",
    "app/state_machine",
    "datasets/raw",
    "datasets/processed",
    "datasets/metadata",
    "test/unit",
    "test/integration",
    "test/benchmarks",
    "notebooks",
    "docs/experiments",
    "scripts"
]

# Define files to create
files = {
    "README.md": "# Historical AI Reconstruction n\nThis project explores AI-driven historical inference using state machines and n-x prediction.",
    ".gitignore": "# Ignore unnecessary files\n*.log\n*.csv\n*.json\n__pycache__/\n",
    "docs/architecture.md": "# Architecture\n\nThis document outlines the methodology and design structure of the project.",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with initial content
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ structure created successfully!")
