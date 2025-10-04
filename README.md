# 🛰️ ObSARve – Accelerating Earth’s Vision with SAR and FPGA

### NASA Space Apps Challenge 2025  
**Challenge:** *Like Alice in Wonderland – Down the Radar Rabbit Hole*  
**Team:** ObSARve  
**Study Area:** Gangotri Glacier, Uttarakhand, India  

---

## 🌍 Overview

**ObSARve** is a project designed to enhance the analysis and processing of **Synthetic Aperture Radar (SAR)** data for environmental monitoring and climate studies.  
Our focus area is the **Gangotri Glacier**, one of the primary sources of the Ganges River. Using **NASA ASF Vertex** data from **2017, 2020, and 2024**, we analyzed glacier surface variations over time and proposed a **hardware-accelerated (FPGA) pipeline** for real-time SAR data processing.

---

## 🎯 Objectives

- Analyze **multi-temporal SAR data** to study glacier surface changes.  
- Develop an efficient **preprocessing and visualization workflow** using NASA data.  
- Implement the same processing pipeline on **FPGA hardware** for faster and energy-efficient computation.  
- Explore **real-time or onboard processing** potential for **UAVs or satellites**.  

---

## 🔬 Methodology

### 1. **Data Collection**
- Source: **NASA ASF Vertex (Sentinel-1 SAR SLC data)**  
- Years analyzed: **2017, 2020, and 2024**  
- Region of Interest: **Gangotri Glacier, Uttarakhand, India**

### 2. **Preprocessing Workflow (Python + SNAP)**

- SLC → TIFF → Preprocessing → Image/GIF → Analysis
  
- Converted `.SLC` data to `.TIFF` using **ESA SNAP Toolbox**
- Applied **radiometric calibration**, **terrain correction**, and **speckle filtering**
- Processed and visualized using:
  - **Python** libraries: Rasterio, Matplotlib, NumPy, GDAL  
  - Generated **GIFs** and **Google Earth overlays** for temporal change detection

### 3. **FPGA Implementation (Proposed and Partially Built)**
- TIFF → SD Card → MicroBlaze → DMA → FPGA Kernel → Processed Data → Image/GIF
  
We designed an **FPGA-based system architecture** in **Xilinx Vivado** to accelerate SAR preprocessing.  
Current progress includes:
- Integration of **MicroBlaze processor**, **DMA**, and **memory components** in Vivado  
- Planning of a **custom FPGA kernel** for SAR data processing  

Due to time constraints during the hackathon, the full computational pipeline is yet to be implemented.  
However, the system design establishes a solid foundation for **real-time SAR data processing** and **hardware-based acceleration**, which we aim to complete in the future.

---

## ⚙️ Tools & Technologies

| Category | Tools / Libraries |
|-----------|-------------------|
| **Data** | NASA ASF Vertex – Sentinel-1 SLC Data |
| **Software** | ESA SNAP Toolbox, Python, Google Earth Pro |
| **Python Libraries** | Rasterio, Matplotlib, NumPy, GDAL |
| **Hardware** | Xilinx FPGA, MicroBlaze, DMA |
| **Design Suite** | Xilinx Vivado |
| **AI Assistance** | ChatGPT (for workflow guidance, documentation, and planning) |

---

## 📊 Results

- Successfully preprocessed and visualized **SAR data** of Gangotri Glacier for 2017, 2020, and 2024  
- Generated **TIFFs**, **images**, and **GIFs** showing surface change and glacier retreat  
- Designed an **FPGA system architecture** (MicroBlaze + DMA) for future hardware acceleration  
- Developed a clear **workflow and proof-of-concept** for real-time glacier monitoring using SAR



---

## 🚀 Future Goals

- Complete FPGA implementation by integrating the SAR processing kernel  
- Benchmark performance for speed, accuracy, and energy efficiency  
- Scale the design to process **full-resolution SAR datasets**  
- Integrate **AI-based change detection models** (CNNs, Transformers) for automated glacier monitoring  
- Deploy on **UAVs or small satellites** for **onboard, real-time data processing**

---

## 🤖 Use of Artificial Intelligence

We used **ChatGPT** as an AI tool to:
- Guide workflow development and understand SAR preprocessing techniques  
- Structure Python-based preprocessing scripts  
- Help organize documentation (README and project submission)  

In future versions, we plan to incorporate **AI models** for:
- Automated glacier boundary detection  
- Ice melt and surface deformation classification  
- Intelligent data filtering and noise reduction in SAR imagery  

---

## 🛰️ NASA & Partner Resources

| Source | Link |
|---------|------|
| **NASA ASF Vertex (SAR Data)** | https://vertex.daac.asf.alaska.edu |
| **ESA SNAP Toolbox** | https://step.esa.int/main/toolboxes/snap/ |
| **Google Earth Pro** | https://www.google.com/earth/versions/ |
| **Xilinx Vivado Design Suite** | https://www.xilinx.com/products/design-tools/vivado.html |
| **Python Rasterio Library** | https://rasterio.readthedocs.io |
| **Matplotlib Library** | https://matplotlib.org |

---

## 📹 Project Demo

**Video Link:** [[Add your YouTube / Google Drive public link here]  ](https://youtu.be/7olwssjQ0LU)
**Duration:** 42 seconds  
**Description:**  
Demonstrates SAR data preprocessing, glacier surface visualization, FPGA architecture (MicroBlaze + DMA), and the proposed future direction for real-time SAR data processing.

---

## 🧑‍🚀 Team ObSARve

- K.Sphoorti, I.Mounika, K.Vyshamya 
- BVRIT Hyderabad College of Engineering for women 
- Hyderabad, India  
- Contact: 23wh1a0492@bvrithyderabad.edu.in, 23wh1a0494@bvrithyderabad.edu.in, 23wh1a0468@bvrithyderabad.edu.in

---

## 📄 License

This project is released under the **MIT License**.  
You are free to use, modify, and distribute the work with appropriate credit.

---

## 💬 Acknowledgments

- **NASA Space Apps Challenge** for providing the platform  
- **NASA ASF DAAC** for open SAR datasets  
- **ESA SNAP Team** for the Sentinel processing toolbox  
- **ChatGPT** for AI-guided documentation and workflow planning  
- **Mentors & Teammates** for collaboration and technical support  

---

> *“From space to silicon — ObSARve accelerates Earth observation through smarter SAR processing and FPGA innovation.”*

