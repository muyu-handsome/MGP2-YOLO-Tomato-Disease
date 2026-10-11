# MGP2-YOLO: An Efficient Tomato Leaf Disease Detection Model for Smart Agricultural Systems

> An improved YOLO11n-based object detector for tomato leaf disease and pest detection in smart greenhouse environments.

[**Download the public dataset (GitHub Release v1.0)**](https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease/releases/tag/dataset-v1.0)

## Overview

MGP2-YOLO is designed to improve multi-scale feature extraction, cross-scale feature fusion, and the representation of small disease symptoms. It incorporates three components into a YOLO11n-based architecture: **GMSEC**, **MAFPN**, and **P2BFPN**. The detector is also integrated into a smart greenhouse monitoring prototype with server-side inference and Unity3D visualization.

## Model Improvements

### 1. GMSEC — Grouped Multi-Scale Efficient Convolution

GMSEC processes selected feature channels using parallel **3 × 3** and **5 × 5** convolutions while preserving an identity pathway. The branch outputs are fused by a **1 × 1** convolution to enhance multi-scale representations without applying multi-kernel processing to every input channel. In MGP2-YOLO, GMSEC-based blocks are incorporated into the backbone P5 stage and the neck P3/P5 stages.

### 2. MAFPN — Multi-scale Aggregation Feature Pyramid Network

MAFPN uses two **FocusFeature** aggregation blocks to align and combine features from **P3, P4, and P5**. It integrates multi-scale context through parallel depthwise convolutions with kernel sizes of **5 × 5, 7 × 7, 9 × 9, and 11 × 11**.

### 3. P2BFPN — P2-Boosted Feature Pyramid Network

P2BFPN introduces fine-grained **P2** features into the **P3** fusion pathway using **SPDConv (space-to-depth convolution)** and subsequent feature fusion. **CSP-OmniKernel** processing incorporates local details and wider contextual information. The network retains **three prediction scales (P3, P4, and P5)** without adding a separate P2 detection head.

## Dataset

The study uses a multi-source tomato leaf disease dataset containing **4,832 original images** from two sources:

| Source | Original images | Description |
| --- | ---: | --- |
| Self-collected field images | 3,361 | Miaolaiyuan planting base, Xiamen, China; March 2025–February 2026, covering two growing cycles |
| PlantVillage | 1,471 | Publicly available tomato leaf images collected under relatively controlled conditions |
| **Total** | **4,832** | **10 categories** |

**Categories (9 disease/pest categories and healthy leaves):**

`Bacterial_Spot`, `Early_Blight`, `Late_Blight`, `Leaf_Miner`, `Leaf_Mold`, `Mosaic_Virus`, `Septoria_Leaf_Spot`, `Spider_Mites`, `Yellow_Leaf_Curl_Virus`, `Healthy`.

### Dataset preparation and partitions

Original images were assigned to training, validation, and test subsets **before offline augmentation**. Rotation, translation, and scaling were applied within the assigned subsets, and augmented images retained their source images' subset membership. Images with unsatisfactory visual quality were excluded during post-augmentation quality screening. **Online Mosaic augmentation** was used during training; no additional test-time augmentation was applied in the reported evaluation.

The reported final dataset sizes are:

| Subset | Images |
| --- | ---: |
| Training | 10,745 |
| Validation | 2,668 |
| Test | 1,083 |
| **Total** | **14,496** |

Images are annotated with **YOLO-format bounding boxes**. The reported test results were obtained using the offline-augmented test subset. The table above reports the verified final subset counts, rather than an assumed fixed split ratio.

### Public download

The dataset archive is available in the **GitHub Release**:

**[MGP2-YOLO Tomato Leaf Disease Dataset — dataset-v1.0](https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease/releases/tag/dataset-v1.0)**

Download the **`DataSet_10.zip`** file under *Assets*. The Release page provides the dataset description and downloadable archive. No Zenodo preview token or reviewer-only access is required for this release.

> **Data source acknowledgement:** PlantVillage is a third-party public dataset. Please acknowledge its original source and follow the applicable terms when reusing or redistributing its images.

## Main Experimental Results

The following values refer to the primary experiment reported in the manuscript.

| Model | Precision | Recall | mAP@50 | mAP@50:95 | Parameters | GFLOPs |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| YOLO11n | 0.7430 | 0.5870 | 0.6643 | 0.5473 | 2.58M | 6.3 |
| **MGP2-YOLO** | **0.7832** | **0.6336** | **0.7036** | **0.5963** | **3.99M** | **14.6** |

MGP2-YOLO improves detection accuracy relative to YOLO11n at the cost of higher computational complexity. It does **not** outperform every compared architecture on every metric.

- **Model-level inference:** 252 FPS on an NVIDIA RTX 5070 Ti GPU.
- **Measured deployment latency:** 200–400 ms from image acquisition to prediction delivery, including video decoding, inference, and message transmission.

The model-level FPS is **not** the throughput of the complete greenhouse monitoring pipeline.

## Experimental Environment

| Item | Configuration |
| --- | --- |
| Operating system | Windows 10 |
| Python | 3.10.0 |
| PyTorch | 2.6.0 |
| CUDA | 12.8 |
| CPU | Intel Core i5-14600KF |
| GPU | NVIDIA RTX 5070 Ti (16 GB) |
| Input image size | 640 × 640 |
| Training epochs | 200 |
| Training batch size | 16 |
| Main optimizer | SGD |

## Installation and Reproduction

Clone the project repository:

```bash
git clone https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease.git
cd MGP2-YOLO-Tomato-Disease
```

If using the packaged modified Ultralytics source, extract `ultralytics.zip` and install it from the **extracted Python package directory** containing `pyproject.toml` or `setup.py`:

```bash
pip install -e .
```

The repository includes training, validation, and inference scripts (`train.py`, `val.py`, and `detect.py`). Before reproducing an experiment, update local dataset and model configuration paths and check the script's checkpoint-loading and resume settings. Use the released dataset archive and the training settings described in the manuscript. The availability of experiment checkpoints, logs, and curves should be checked separately; the dataset release itself is not a trained-model checkpoint release.

## Citation

If you use this project or dataset, please cite the associated manuscript:

**MGP2-YOLO: An Efficient Tomato Leaf Disease Detection Model for Smart Agricultural Systems**. *Signal, Image and Video Processing* (manuscript under review).

## Links

- **Source code:** https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease
- **Public dataset:** https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease/releases/tag/dataset-v1.0
