# 🌲 Ireland Forest Carbon Monitoring Pipeline

> 💡 **Project Evolution:** This is the foundational, Ireland-specific implementation (v1) that proved the Sentinel-1/2 hybrid LULUCF concept.
> 🚀 **Looking for the production-ready version?** Check out the **[Forest Carbon Continuity Pipeline (v2)](https://github.com/SyedRafiAhmedGIS/forest-carbon-continuity-pipeline)**, which features CI/CD gating, a Makefile, bundled data, and a <4-hour handover onboarding process.

**A Sentinel-1/2 Hybrid Approach for EU LULUCF Compliance.**  
*Built for cloud-proof, species-specific, and reproducible carbon accounting.*

![Pipeline Workflow](docs/pipeline_demo.gif)

## 🚀 Quick Start
1. **Setup Environment:** `conda env create -f environment.yaml`
2. **Activate:** `conda activate ireland-forest-carbon`
3. **Run Pipeline:** Open `notebooks/99_Master_Orchestrator.ipynb` and click "Run All".


### 📓 Interactive Notebooks (Open in Colab)
- **[00 Smart Upload Preview](https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/00_Smart_Upload_Preview.ipynb)** <a href='https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/00_Smart_Upload_Preview.ipynb' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>
- **[01 Preprocessing CRS](https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/01_Preprocessing_CRS.ipynb)** <a href='https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/01_Preprocessing_CRS.ipynb' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>
- **[02 Cloud Masking Fusion](https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/02_Cloud_Masking_Fusion.ipynb)** <a href='https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/02_Cloud_Masking_Fusion.ipynb' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>
- **[03 NFI Ground Truth](https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/03_NFI_Ground_Truth.ipynb)** <a href='https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/03_NFI_Ground_Truth.ipynb' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>
- **[04 ML Species Classification](https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/04_ML_Species_Classification.ipynb)** <a href='https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/04_ML_Species_Classification.ipynb' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>
- **[05 Carbon Stock Uncertainty](https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/05_Carbon_Stock_Uncertainty.ipynb)** <a href='https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/05_Carbon_Stock_Uncertainty.ipynb' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>
- **[06 Forest Density LandCover Layers](https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/06_Forest_Density_LandCover_Layers.ipynb)** <a href='https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/06_Forest_Density_LandCover_Layers.ipynb' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>
- **[99 Master Orchestrator](https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/99_Master_Orchestrator.ipynb)** <a href='https://colab.research.google.com/github/SyedRafiAhmedGIS/ireland-forest-carbon-pipeline/blob/main/notebooks/99_Master_Orchestrator.ipynb' target='_blank'><img src='https://colab.research.google.com/assets/colab-badge.svg' alt='Open In Colab'/></a>

## 🏗️ Architecture
- **`src/`**: Core modular Python logic (The Engine)
- **`notebooks/`**: Interactive Colab Wrappers with Smart Uploads & Previews
- **`configs/`**: Region-specific YAML (Ireland, UK, Scandinavia)
- **`docs/`**: "Code as Documentation" & Pipeline GIF Generator

## 📊 Pipeline Phases
1. **CRS Reprojection:** WGS84 $\rightarrow$ ETRS89/UTM 29N (EPSG:25829)
2. **Cloud-Proof Masking:** Sentinel-1 VH/VV radar fusion.
3. **NFI Integration:** Relascope/Laser Hypsometer math ($H = D \times \tan(\theta) + h$).
4. **ML Classification:** U-Net (Dice+BCE Loss) for Sitka Spruce, Lodgepole Pine, Native Mixed.
5. **Carbon Accounting:** Species $\times$ Age Matrix with $\pm 95\%$ CI uncertainty.
6. **Density & LULC Layers:** VDF, MDF, Open Forest, Nurseries, Barren Land mapping.

---
*Built by Syed Rafi Ahmed | M.Tech Remote Sensing & GIS*
