import os
import numpy as np
import rasterio
from rasterio.enums import Resampling

# Paths
tiff_folder = r"C:\Users\admin\Desktop\GANGOTRI_GLACIER\reprojected\kml"
output_folder = os.path.join(tiff_folder, "rgb_tiffs")
os.makedirs(output_folder, exist_ok=True)

files = ["Gangotri_2017_VV_WGS84.tif",
         "Gangotri_2020_VV_WGS84.tif",
         "Gangotri_2024_VV_WGS84.tif"]

def create_rgb(current, previous=None):
    norm = (current - np.min(current)) / (np.max(current) - np.min(current))
    rgb = np.zeros((current.shape[0], current.shape[1], 3), dtype=np.float32)

    # Rocks
    rocks = norm < 0.2
    rgb[rocks] = [0.6, 0.3, 0.0]

    # Stable ice
    ice = norm >= 0.2
    rgb[ice] = [0.0, 1.0, 1.0]

    # Ice retreat overlay
    if previous is not None:
        retreat = (previous - current) > 0.05
        rgb[retreat] = [1.0, 0.0, 0.0]

    return rgb

prev = None
for f in files:
    path = os.path.join(tiff_folder, f)
    with rasterio.open(path) as src:
        data = src.read(1)
        profile = src.profile

    # Resample to previous shape if needed
    if prev is not None and data.shape != prev.shape:
        data_resampled = np.empty(prev.shape, dtype=data.dtype)
        rasterio.warp.reproject(
            source=data,
            destination=data_resampled,
            src_transform=src.transform,
            dst_transform=src.transform,
            src_crs=src.crs,
            dst_crs=src.crs,
            resampling=Resampling.bilinear
        )
        data = data_resampled

    rgb = create_rgb(data, prev)
    profile.update(count=3, dtype=rasterio.float32)
    out_path = os.path.join(output_folder, f.replace(".tif", "_RGB.tif"))
    with rasterio.open(out_path, "w", **profile) as dst:
        dst.write(np.moveaxis(rgb, 2, 0))
    print(f"Saved {out_path}")
    prev = data
