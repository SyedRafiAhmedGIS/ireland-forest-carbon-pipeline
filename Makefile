.PHONY: setup run clean test help

# Default target
help:
	@echo "Available commands:"
	@echo "  make setup   - Create the conda environment"
	@echo "  make run     - Launch Jupyter Lab to run the notebooks"
	@echo "  make clean   - Remove __pycache__ and .ipynb_checkpoints"
	@echo "  make test    - Run pytest on the tests/ directory"

setup:
	@echo "Setting up environment..."
	conda env create -f environment.yaml
	@echo "Environment created. Activate it with: conda activate ireland-forest-carbon"

run:
	@echo "Starting Jupyter Lab..."
	jupyter lab notebooks/

clean:
	@echo "Cleaning up temporary files..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -r {} +

test:
	@echo "Running tests..."
	pytest tests/ -v
