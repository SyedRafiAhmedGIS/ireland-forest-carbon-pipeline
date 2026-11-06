import numpy as np
import rasterio

def apply_cloud_masking(sar_vh_path, sar_vv_path, output_mask_path):
    """Uses VH/VV ratios to separate forest from peat/water (Cloud-Proof)"""
    with rasterio.open(sar_vh_path) as vh, rasterio.open(sar_vv_path) as vv:
        vh_linear, vv_linear = vh.read(1).astype(float), vv.read(1).astype(float)
        vh_db = 10 * np.log10(np.where(vh_linear > 0, vh_linear, 1e-10))
        ratio = np.divide(vh_linear, vv_linear, out=np.zeros_like(vh_linear), where=vv_linear!=0)
        forest_mask = (vh_db > -15) & (ratio > 0.15)
        mask = np.where(forest_mask, 1, 0).astype(np.uint8)
        out_meta = vh.meta.copy()
        out_meta.update({'dtype': 'uint8', 'count': 1})  # mask must stay uint8, not inherit float32
        with rasterio.open(output_mask_path, 'w', **out_meta) as dst:
            dst.write(mask, 1)
    # FIX 1: Return the correct path variable
    return output_mask_path

def extract_ndvi_max(nir_path, red_path, output_ndvi_path):
    """Extracts phenological NDVI max-values from Sentinel-2"""
    with rasterio.open(nir_path) as nir, rasterio.open(red_path) as red:
        nir_data, red_data = nir.read(1).astype(float), red.read(1).astype(float)
        ndvi = np.divide((nir_data - red_data), (nir_data + red_data), out=np.zeros_like(nir_data), where=(nir_data+red_data)!=0)
        with rasterio.open(output_ndvi_path, 'w', **nir.meta) as dst:
            dst.write(ndvi, 1)
    return output_ndvi_path
