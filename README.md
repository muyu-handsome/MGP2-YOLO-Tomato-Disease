# MGP2‑YOLO: An Efficient Tomato Leaf Disease Detection Model for Smart Agricultural Systems
> Improved YOLO11n for tomato leaf disease detection in smart greenhouse scenarios

> ⚠️ **Dataset Access Note (For peer‑review only)**
> This Zenodo record is an unpublished draft for manuscript review.
> Review‑only preview link：https://zenodo.org/records/23132682?preview=1
> The dataset will be formally released with persistent DOI after manuscript acceptance.

## Model Improvements
Based on YOLO11n baseline, this work proposes three custom modules for multi‑scale feature learning and small‑lesion detection:

1. **GMSEC (Grouped Multi‑Scale Efficient Convolution)**
Introduced at the end of backbone. Parallel multi‑kernel grouped convolution enhances multi‑scale feature extraction with low computational overhead.

2. **MAFPN (Multi‑scale Aggregation Feature Pyramid Network)**
Cross‑scale feature aggregation module. Fuses multi‑level features to reduce semantic gaps and strengthen cross‑scale information interaction.

3. **P2BFPN (P2‑Boosted Feature Pyramid Network)**
Reuses low‑level P2 feature via SPDConv lossless down‑sampling. Improves detection performance for tiny and subtle lesions without adding extra detection head.

> Auxiliary component：
> - **SPDConv (Space‑to‑Depth Convolution)**：Lossless down‑sampling, reduces spatial information loss compared with traditional strided convolution.
> - **CSP‑OmniKernel**: Integrates CSP structure and Omni‑Kernel to capture multi‑scale contextual information.

## Dataset
- **Total images**: 4 832 multi‑source tomato leaf images
- **Categories**: 10 classes (9 diseases + healthy leaf)
- **Class list**: `Bacterial_Spot`, `Early_Blight`, `Healthy`, `Late_Blight`, `Leaf_Mold`, `Leaf_Miner`, `Mosaic_Virus`, `Septoria_Leaf_Spot`, `Spider_Mites`, `Yellow_Leaf_Curl_Virus`
- **Data composition**:
  - 3 361 field images collected from Miaolaiyuan planting base (Xiamen, China, Mar.2025‑Feb.2026, two complete tomato growth cycles)
  - 1 471 samples from public PlantVillage dataset
- **Annotation**: YOLO‑format bounding‑box annotations for lesion regions
- **Split ratio**: train / val / test = 7 : 2 : 1
- **Dataset download**: https://zenodo.org/records/23132682?preview=1

## Environment
### Core experimental environment
- OS: Windows 10 Pro (64‑bit)
- Python: 3.10.0
- PyTorch: 2.6.0
- CUDA: 12.8

### Install dependencies
```bash
pip install -e .
