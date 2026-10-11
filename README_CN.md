# MGP2-YOLO：面向智慧农业的高效番茄叶片病害检测模型

> 基于 YOLO11n 改进的番茄叶片病虫害目标检测模型，面向智慧温室监测场景。

**[下载公开数据集（GitHub Releases：dataset-v1.0）](https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease/releases/tag/dataset-v1.0)**

[English README](README.md) | [中文说明](README_CN.md)

## 项目简介

MGP2-YOLO 在 YOLO11n 的基础上引入 **GMSEC、MAFPN 和 P2BFPN** 三个模块，旨在改善多尺度特征提取、跨尺度信息融合和细微病斑的特征表示。研究还将模型集成至智慧温室监测原型系统，采用服务器端推理与 Unity3D 可视化。

## 模型改进

### 1. GMSEC（Grouped Multi-Scale Efficient Convolution，分组多尺度高效卷积）

GMSEC 使用**部分通道多尺度卷积**：一半输入通道走恒等映射路径，另一半通道分配至并行的 **3 × 3** 和 **5 × 5** 卷积分支，最后通过 **1 × 1** 卷积融合。该设计在不对所有通道执行多核卷积的情况下增强多尺度特征表示。

在 MGP2-YOLO 中，基于 GMSEC 的模块部署在**骨干网络 P5 阶段**以及**检测颈部网络 P3、P5 阶段**。

### 2. MAFPN（Multi-scale Aggregation Feature Pyramid Network，多尺度聚合特征金字塔网络）

MAFPN 通过两个 **FocusFeature** 聚合模块对 **P3、P4、P5** 特征进行尺寸和通道对齐，并进行跨尺度融合。模块采用核大小为 **5 × 5、7 × 7、9 × 9、11 × 11** 的并行深度卷积提取不同感受野的上下文特征。

### 3. P2BFPN（P2-Boosted Feature Pyramid Network，P2 增强特征金字塔网络）

P2BFPN 利用 **SPDConv（Space-to-Depth Convolution）** 将浅层 **P2** 特征转换至 **P3** 分辨率，并与其他尺度的特征进行融合，再通过 **CSP-OmniKernel** 处理局部细节和上下文信息。

**该结构仅在特征融合过程中引入 P2 信息，不新增 P2 检测头；预测尺度仍为 P3、P4、P5。**

> **辅助组件**
> - **SPDConv**：利用空间到通道的重排操作，帮助保留下采样过程中的细粒度空间信息；并不表示整个后续卷积过程完全无信息损失。
> - **CSP-OmniKernel**：结合 CSP 通道分流和 OmniKernel 上下文建模，在控制处理范围的同时融合不同尺度的信息。

## 数据集

本研究使用多来源番茄叶片病虫害图像数据集，共包含 **4,832 张原始图像**。

| 图像来源 | 原始图像数量 | 说明 |
| --- | ---: | --- |
| 自建田间数据集 | 3,361 | 厦门苗来园种植基地；2025 年 3 月至 2026 年 2 月，覆盖两个番茄生长周期 |
| PlantVillage | 1,471 | 公开数据集图像，拍摄条件相对受控 |
| **总计** | **4,832** | **10 个类别** |

**类别：9 类病害/虫害及 1 类健康叶片**

`Bacterial_Spot`、`Early_Blight`、`Late_Blight`、`Leaf_Miner`、`Leaf_Mold`、`Mosaic_Virus`、`Septoria_Leaf_Spot`、`Spider_Mites`、`Yellow_Leaf_Curl_Virus`、`Healthy`

图像中的病害区域采用 **YOLO 格式边界框**进行标注。

### 数据划分、增强与质量筛选

首先将原始图像划分到训练集、验证集和测试集，**然后在各子集内部开展离线数据增强**（旋转、平移和缩放）。增强样本沿用对应原图的数据子集归属。离线增强后，对视觉质量不理想的增强图像进行筛选与剔除，不在不同子集之间重新分配图像。

研究中使用的最终数据集数量如下：

| 子集 | 图像数量 |
| --- | ---: |
| 训练集（Train） | 10,745 |
| 验证集（Validation） | 2,668 |
| 测试集（Test） | 1,083 |
| **合计** | **14,496** |

训练阶段还使用在线 **Mosaic** 增强；论文报告的测试结果基于离线增强后的测试集，未额外采用测试时增强（TTA）。上表为最终子集图像数，**不将其描述为固定的 7:2:1 比例**。

### 数据集公开下载

数据集已通过 **GitHub Releases** 发布：

**[MGP2-YOLO Tomato Leaf Disease Dataset — dataset-v1.0](https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease/releases/tag/dataset-v1.0)**

打开发布页面，在 **Assets** 中下载 **`DataSet_10.zip`**（约 **566 MB**）。该链接为公开的 GitHub Release 地址，**不再使用 Zenodo 私人预览链接或审稿专用访问令牌**。

> **数据来源与使用提醒：** PlantVillage 属于第三方公开数据来源。使用或再次分发有关图像时，请引用其原始来源并遵守适用许可条款。数据集公开不代表其中全部内容自动采用相同的再分发许可。

## 主要实验结果

以下数值来自论文报告的主要实验，对比基线模型为 YOLO11n。

| 模型 | Precision | Recall | mAP@50 | mAP@50:95 | 参数量 | GFLOPs |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| YOLO11n | 0.7430 | 0.5870 | 0.6643 | 0.5473 | 2.58M | 6.3 |
| **MGP2-YOLO** | **0.7832** | **0.6336** | **0.7036** | **0.5963** | **3.99M** | **14.6** |

MGP2-YOLO 相比 YOLO11n 提升了检测指标，但参数量和计算量也有所增加，体现了**检测精度与计算复杂度之间的权衡**；不应理解为在全部指标上均优于所有对比模型。

- **模型级推理速度**：在 NVIDIA RTX 5070 Ti GPU 上测得 **252 FPS**。
- **系统端到端延迟**：从图像采集到检测结果送达约 **200–400 ms**，包括视频解码、模型推理和消息传输。

**252 FPS 为模型级指标，不代表完整温室监测流程的实际端到端帧率。**

## 运行环境

| 项目 | 配置 |
| --- | --- |
| 操作系统 | Windows 10 |
| Python | 3.10.0 |
| PyTorch | 2.6.0 |
| CUDA | 12.8 |
| CPU | Intel Core i5-14600KF |
| GPU | NVIDIA RTX 5070 Ti（16 GB） |
| 输入图像尺寸 | 640 × 640 |
| 训练轮数 | 200 |
| 训练 Batch size | 16 |
| 主要优化器 | SGD |

## 环境安装与实验复现

首先克隆仓库：

```bash
git clone https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease.git
cd MGP2-YOLO-Tomato-Disease
```

如使用仓库中的修改版 Ultralytics 源码压缩包，请先解压 `ultralytics.zip`，再进入**包含 `pyproject.toml` 或 `setup.py` 的解压目录**，执行：

```bash
pip install -e .
```

仓库提供训练、验证和推理相关脚本（如 `train.py`、`val.py`、`detect.py`）。运行前，请根据本地环境检查并修改数据集路径、模型配置、预训练权重路径以及断点续训（`resume`）设置。实验配置应以论文和实际训练记录为准。

**注意：** 数据集 Release 主要提供数据文件，不应将其误认为包含完整训练模型权重、训练日志或结果曲线；上述实验材料请以仓库中实际公开的文件为准。

## 论文引用

如果本项目或数据集对您的研究有所帮助，请引用相应论文（当前为在审稿件）：

**MGP2-YOLO: An Efficient Tomato Leaf Disease Detection Model for Smart Agricultural Systems**. *Signal, Image and Video Processing*（投稿审稿中）。

## 项目链接

- **项目代码：** https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease
- **公开数据集：** https://github.com/muyu-handsome/MGP2-YOLO-Tomato-Disease/releases/tag/dataset-v1.0
