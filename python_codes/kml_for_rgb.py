from simplekml import Kml
import os

rgb_folder = r"C:\Users\admin\Desktop\GANGOTRI_GLACIER\reprojected\kml\rgb_tiffs"
kml_folder = os.path.join(rgb_folder, "kml")
os.makedirs(kml_folder, exist_ok=True)

for f in os.listdir(rgb_folder):
    if f.endswith("_RGB.tif"):
        kml = Kml()
        kml.newgroundoverlay(name=f, icon_href=os.path.join(rgb_folder, f))
        kml.save(os.path.join(kml_folder, f.replace(".tif", ".kml")))
        print(f"Saved KML: {f.replace('.tif', '.kml')}")
