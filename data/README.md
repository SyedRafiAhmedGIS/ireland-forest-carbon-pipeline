# 📂 Data Directory

This directory contains sample data to allow instant, zero-friction testing of the pipeline.

### Included Files
- `sample_nfi_ireland.csv`: A minimal, realistic National Forest Inventory (NFI) plot dataset for Ireland.

### How to Use Real Data
To run this pipeline on real data:
1. Replace `sample_nfi_ireland.csv` with your actual NFI ground-truth CSV.
2. Ensure your Sentinel-1 (GRD) and Sentinel-2 (L2A) GeoTIFFs are placed in a local `data/rasters/` directory (ignored by `.gitignore` due to size).
3. Update the paths in `configs/ireland_config.yaml` to point to your local raster directory.

See also `docs/REAL_DATA_GUIDE.md` for a full walkthrough with real Sentinel data.
