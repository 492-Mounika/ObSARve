import rasterio
import numpy as np
import os
import struct
import json

tiff_files = [
    "5c5a_sigma0_VH_2024.tif",
    "5c5a_sigma0_VV_2024.tif",
    "Gangotri_2017_VH.tif",
    "Gangotri_2017_VV.tif",
    "Gangotri_2020_VV.tif",
    "Gangotri_2020_VH.tif"
]

# Output folder (where binary files will be saved)
outdir = "bin_tiles"
os.makedirs(outdir, exist_ok=True)

manifest = []

for tif in tiff_files:
    with rasterio.open(tif) as src:
        data = src.read(1)  # read first band

        if data.dtype != np.uint16:
            # Scale float32 → uint16 if necessary
            data = ((data - np.min(data)) / (np.max(data) - np.min(data)) * 65535).astype(np.uint16)


        fname = os.path.splitext(os.path.basename(tif))[0] + ".bin"
        bin_path = os.path.join(outdir, fname)


        with open(bin_path, "wb") as f:
            height, width = data.shape
            f.write(struct.pack('<IIH', width, height, 1))  # width(4), height(4), dtype(2)
            f.write(data.tobytes())



        manifest.append({
            "file": fname,
            "width": width,
            "height": height,
            "dtype": "uint16",
            "bytes": data.nbytes + 10  # including header
        })

# Save manifest.json
with open(os.path.join(outdir, "manifest.json"), "w") as mf:
    json.dump(manifest, mf, indent=2)

print("Conversion done. Binary files and manifest saved in:", outdir)
