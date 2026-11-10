import geopandas as gpd
import pandas as pd
import numpy as np

def calculate_tree_height(distance_m, angle_rad, observer_height_m):
    """Laser Hypsometer formula: H = D * tan(θ) + h"""
    return distance_m * np.tan(angle_rad) + observer_height_m

def process_nfi_ground_truth(nfi_path, output_path):
    """Filters DBH >= 10cm (EU Standard) and applies height formula if possible"""
    if nfi_path.endswith('.csv') or nfi_path.endswith('.xlsx'):
        df = pd.read_csv(nfi_path) if nfi_path.endswith('.csv') else pd.read_excel(nfi_path)
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y), crs="EPSG:4326")
    else:
        gdf = gpd.read_file(nfi_path)
    if 'DBH' in gdf.columns:
        gdf = gdf[gdf['DBH'] >= 10.0]
    if all(c in gdf.columns for c in ['Distance', 'Angle', 'ObsHeight']):
        gdf['Height'] = calculate_tree_height(gdf['Distance'], np.radians(gdf['Angle']), gdf['ObsHeight'])
    gdf = gdf.to_crs("EPSG:25829")
    gdf.to_file(output_path, driver="GPKG")
    return output_path
