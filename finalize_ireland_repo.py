"""
finalize_ireland_repo.py
Automates the final polish of the ireland-forest-carbon-pipeline repository.
Creates sample data, updates README with v1->v2 narrative, adds Colab badges, and generates a Makefile.

Usage:
    python finalize_ireland_repo.py   (run from the repository root)

Requires only the Python standard library.
"""

import csv
from pathlib import Path

# Configuration
REPO_NAME = "ireland-forest-carbon-pipeline"
V2_REPO_URL = "https://github.com/SyedRafiAhmedGIS/forest-carbon-continuity-pipeline"
NOTEBOOKS = [
    "00_Smart_Upload_Preview.ipynb",
    "01_Preprocessing_CRS.ipynb",
    "02_Cloud_Masking_Fusion.ipynb",
    "03_NFI_Ground_Truth.ipynb",
    "04_ML_Species_Classification.ipynb",
    "05_Carbon_Stock_Uncertainty.ipynb",
    "06_Forest_Density_LandCover_Layers.ipynb",
    "99_Master_Orchestrator.ipynb",
]


def create_sample_data():
    """Creates a realistic dummy NFI dataset for instant testing."""
    print("📦 Generating sample data...")
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    # Realistic dummy NFI data for Ireland
    sample_data = [
        ["plot_id", "latitude", "longitude", "species", "dbh_cm", "height_m", "age_years", "carbon_tonnes_ha"],
        ["IRL_001", 52.9583, -7.8542, "Sitka Spruce", 28.5, 22.1, 25, 145.2],
        ["IRL_002", 53.1204, -6.9876, "Lodgepole Pine", 24.0, 19.5, 20, 112.8],
        ["IRL_003", 52.8112, -8.1123, "Native Mixed", 32.1, 24.0, 45, 189.5],
        ["IRL_004", 53.3498, -6.2603, "Sitka Spruce", 30.2, 23.5, 30, 162.1],
        ["IRL_005", 52.6543, -7.4321, "Native Mixed", 29.8, 21.8, 35, 155.4],
    ]

    csv_path = data_dir / "sample_nfi_ireland.csv"
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
    print(f"   ✅ Created: {csv_path}")

    # Data README
    data_readme = data_dir / "README.md"
    with open(data_readme, "w", encoding="utf-8") as f:
        f.write("""# 📂 Data Directory

This directory contains sample data to allow instant, zero-friction testing of the pipeline.

### Included Files
- `sample_nfi_ireland.csv`: A minimal, realistic National Forest Inventory (NFI) plot dataset for Ireland.

### How to Use Real Data
To run this pipeline on real data:
1. Replace `sample_nfi_ireland.csv` with your actual NFI ground-truth CSV.
2. Ensure your Sentinel-1 (GRD) and Sentinel-2 (L2A) GeoTIFFs are placed in a local `data/rasters/` directory (ignored by `.gitignore` due to size).
3. Update the paths in `configs/ireland_config.yaml` to point to your local raster directory.

See also `docs/REAL_DATA_GUIDE.md` for a full walkthrough with real Sentinel data.
""")
    print(f"   ✅ Created: {data_readme}")


def update_readme():
    """Updates the main README with the v1->v2 narrative and Colab badges."""
    print("📝 Updating README.md...")
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("   ⚠️ README.md not found. Skipping.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add Project Evolution Banner at the top (after the main title)
    evolution_banner = f"""
> 💡 **Project Evolution:** This is the foundational, Ireland-specific implementation (v1) that proved the Sentinel-1/2 hybrid LULUCF concept.
> 🚀 **Looking for the production-ready version?** Check out the **[Forest Carbon Continuity Pipeline (v2)]({V2_REPO_URL})**, which features CI/CD gating, a Makefile, bundled data, and a <4-hour handover onboarding process.
"""
    if "> 💡 **Project Evolution:**" not in content:
        content = content.replace(
            "# 🌲 Ireland Forest Carbon Monitoring Pipeline",
            "# 🌲 Ireland Forest Carbon Monitoring Pipeline\n" + evolution_banner,
        )

    # 2. Add Colab Badges to the Quick Start section
    colab_section = "\n### 📓 Interactive Notebooks (Open in Colab)\n"
    for nb in NOTEBOOKS:
        nb_name = nb.replace(".ipynb", "").replace("_", " ")
        colab_url = f"https://colab.research.google.com/github/SyedRafiAhmedGIS/{REPO_NAME}/blob/main/notebooks/{nb}"
        colab_section += (
            f"- **[{nb_name}]({colab_url})** "
            f"<a href='{colab_url}' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>\n"
        )

    if "### 📓 Interactive Notebooks" not in content:
        # Insert before the Architecture section
        content = content.replace("## 🏗️ Architecture", colab_section + "\n## 🏗️ Architecture")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("   ✅ README.md updated with Evolution Banner and Colab badges.")


def create_makefile():
    """Creates a simple Makefile for easy local development.
    Note: Makefile recipes require actual TAB characters, which are embedded below directly."""
    print("🛠️ Creating Makefile...")
    makefile_content = (
        ".PHONY: setup run clean test help\n"
        "\n"
        "# Default target\n"
        "help:\n"
        "\t@echo \"Available commands:\"\n"
        "\t@echo \"  make setup   - Create the conda environment\"\n"
        "\t@echo \"  make run     - Launch Jupyter Lab to run the notebooks\"\n"
        "\t@echo \"  make clean   - Remove __pycache__ and .ipynb_checkpoints\"\n"
        "\t@echo \"  make test    - Run pytest on the tests/ directory\"\n"
        "\n"
        "setup:\n"
        "\t@echo \"Setting up environment...\"\n"
        "\tconda env create -f environment.yaml\n"
        "\t@echo \"Environment created. Activate it with: conda activate ireland-forest-carbon\"\n"
        "\n"
        "run:\n"
        "\t@echo \"Starting Jupyter Lab...\"\n"
        "\tjupyter lab notebooks/\n"
        "\n"
        "clean:\n"
        "\t@echo \"Cleaning up temporary files...\"\n"
        "\tfind . -type d -name \"__pycache__\" -exec rm -r {} +\n"
        "\tfind . -type d -name \".ipynb_checkpoints\" -exec rm -r {} +\n"
        "\n"
        "test:\n"
        "\t@echo \"Running tests...\"\n"
        "\tpytest tests/ -v\n"
    )

    with open("Makefile", "w", encoding="utf-8", newline="\n") as f:
        f.write(makefile_content)
    print("   ✅ Makefile created.")


def main():
    print(f"🚀 Finalizing {REPO_NAME} for interview readiness...\n")

    # Ensure we are in the right directory
    if not Path("environment.yaml").exists():
        print("❌ Error: environment.yaml not found. Please run this script from the root of the repository.")
        return

    create_sample_data()
    update_readme()
    create_makefile()

    print("\n" + "=" * 60)
    print("🎉 REPO FINALIZATION COMPLETE!")
    print("=" * 60)
    print("Next Steps:")
    print("1. Review the updated README.md.")
    print("2. Run `make setup` (or `conda env create -f environment.yaml`) to install dependencies.")
    print("3. Run `make run` to launch Jupyter and test the pipeline with the new sample data.")
    print("4. Commit and push these changes:")
    print("   git add .")
    print("   git commit -m 'chore: finalize v1 repo with sample data, makefile, and colab badges'")
    print("   git push origin main")


if __name__ == "__main__":
    main()
