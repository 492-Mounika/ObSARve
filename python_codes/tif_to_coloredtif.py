import rasterio
from rasterio.enums import Resampling
from rasterio import warp  # <-- fix for reproject
import numpy as np
import matplotlib.pyplot as plt

# === Step 1: File paths ===
files = {
    "2017": {"VV": r"C:\Users\admin\Desktop\GANGOTRI_GLACIER\Gangotri_2017_VV.tif",
             "VH": r"C:\Users\admin\Desktop\GANGOTRI_GLACIER\Gangotri_2017_VH.tif"},
    "2020": {"VV": r"C:\Users\admin\Desktop\GANGOTRI_GLACIER\Gangotri_2020_VV.tif",
             "VH": r"C:\Users\admin\Desktop\GANGOTRI_GLACIER\Gangotri_2020_VH.tif"},
    "2024": {"VV": r"C:\Users\admin\Desktop\GANGOTRI_GLACIER\Gangotri_2024_VV.tif",
             "VH": r"C:\Users\admin\Desktop\GANGOTRI_GLACIER\Gangotri_2024_VH.tif"}
}

# === Step 2: Load bands and profiles ===
data = {}
profiles = {}

def load_band(file_path):
    with rasterio.open(file_path) as src:
        return src.read(1), src.profile

for year in files:
    data[year] = {}
    profiles[year] = {}
    for pol in files[year]:
        print(f"Loading {year} {pol}...")
        band, profile = load_band(files[year][pol])
        data[year][pol] = band
        profiles[year][pol] = profile

# === Step 3: Resample 2020 & 2024 to match 2017 ===
target_shape = data["2017"]["VV"].shape
target_profile = profiles["2017"]["VV"]

def resample_to_match(src_array, src_profile, target_shape, target_profile):
    """Resample src_array to target_shape using bilinear resampling"""
    resampled = np.empty(shape=target_shape, dtype=src_array.dtype)
    warp.reproject(
        source=src_array,
        destination=resampled,
        src_transform=src_profile['transform'],
        src_crs=src_profile['crs'],
        dst_transform=target_profile['transform'],
        dst_crs=target_profile['crs'],
        resampling=Resampling.bilinear
    )
    return resampled

for year in ["2020", "2024"]:
    for pol in ["VV", "VH"]:
        print(f"Resampling {year} {pol} to match 2017 shape...")
        data[year][pol] = resample_to_match(data[year][pol], profiles[year][pol], target_shape, target_profile)

# === Step 4: Compute difference maps (VV + VH) ===
diff_17_20_VV = data["2020"]["VV"] - data["2017"]["VV"]
diff_20_24_VV = data["2024"]["VV"] - data["2020"]["VV"]

diff_17_20_VH = data["2020"]["VH"] - data["2017"]["VH"]
diff_20_24_VH = data["2024"]["VH"] - data["2020"]["VH"]

# === Step 5: Plot original VV + difference maps ===
plt.figure(figsize=(18, 10))

plt.subplot(2,3,1)
plt.title("2017 VV")
plt.imshow(data["2017"]["VV"], cmap='gray')
plt.colorbar()

plt.subplot(2,3,2)
plt.title("2020 VV")
plt.imshow(data["2020"]["VV"], cmap='gray')
plt.colorbar()

plt.subplot(2,3,3)
plt.title("2024 VV")
plt.imshow(data["2024"]["VV"], cmap='gray')
plt.colorbar()

plt.subplot(2,3,4)
plt.title("Diff 2017-2020 VV")
plt.imshow(diff_17_20_VV, cmap='RdYlBu')
plt.colorbar()

plt.subplot(2,3,5)
plt.title("Diff 2020-2024 VV")
plt.imshow(diff_20_24_VV, cmap='RdYlBu')
plt.colorbar()

plt.tight_layout()
plt.show()

# === Step 6: Plot VH difference maps (optional) ===
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title("Diff 2017-2020 VH")
plt.imshow(diff_17_20_VH, cmap='RdYlBu')
plt.colorbar()

plt.subplot(1,2,2)
plt.title("Diff 2020-2024 VH")
plt.imshow(diff_20_24_VH, cmap='RdYlBu')
plt.colorbar()

plt.tight_layout()
plt.show()
