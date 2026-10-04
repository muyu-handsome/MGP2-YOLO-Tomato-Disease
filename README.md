# YOLO11 Tomato Leaf Disease Detection

基于改进YOLO11的番茄叶片病害检测模型。

## 模型改进

本项目在YOLO11基础上进行了以下改进：

1. **C3k2_EMSC (Efficient Multi-Scale Convolution)**: 在backbone末端引入高效多尺度卷积模块，增强多尺度特征提取能力
2. **FocusFeature**: 特征聚焦模块，通过多尺度深度可分离卷积聚合多层级特征
3. **SPDConv (Space-to-Depth Convolution)**: 无损下采样模块，替代传统步长卷积减少空间信息损失
4. **CSPOmniKernel**: CSP结构的全向核模块，结合频率通道注意力增强特征表达

## 数据集

- **类别数**: 10类番茄叶片病害
- **类别**: Bacterial_Spot, Early_Blight, Healthy, Late_Blight, Leaf_Mold, Leaf_Miner, Mosaic_Virus, Septoria, Spider_Mites, Yellow_Leaf_Curl_Virus
- **来源**: [Roboflow - Tomato Leaf Diseases Detect]([https://universe.roboflow.com/sylhet-agricultural-university/tomato-leaf-diseases-detect/dataset/3](https://zenodo.org/records/23132682?preview=1))

## 环境配置

```bash
pip install -e .
```

### 依赖
- Python >= 3.8
- PyTorch >= 1.8.0
- torchvision >= 0.9.0
- einops
- timm
- prettytable

## 使用方法

### 训练
```bash
python train.py
```

### 验证
```bash
python val.py
```

### 推理
```bash
python detect.py
```

### 热力图可视化
```bash
python heatmap.py
```

## 项目结构

```
├── ultralytics/                    # 核心框架
│   ├── cfg/models/11/             # 模型配置文件
│   │   ├── yolo11.yaml            # YOLO11 baseline
│   │   ├── yolo11-AFPN-*.yaml     # AFPN对比模型
│   │   └── my-yolo-fdpn-*.yaml    # 本文改进模型系列
│   └── nn/
│       ├── extra_modules/         # 自定义模块
│       │   ├── block.py           # C3k2_EMSC, FocusFeature, SPDConv, CSPOmniKernel等
│       │   ├── afpn.py            # AFPN特征金字塔
│       │   └── head.py            # 自定义检测头
│       ├── modules/               # 标准模块
│       ├── tasks.py               # 模型构建
│       └── backbone/              # 骨干网络
├── myDataSet_10/                  # 数据集配置
│   └── data.yaml
├── train.py                       # 训练脚本
├── val.py                         # 验证脚本
├── detect.py                      # 推理脚本
├── heatmap.py                     # 热力图可视化
├── plot_result.py                 # 训练曲线绘制
├── get_FPS.py                     # FPS测试
├── get_model_erf.py               # 有效感受野分析
└── pyproject.toml                 # 项目配置
```

## 模型配置

| 模型 | 配置文件 | 说明 |
|------|---------|------|
| Baseline | yolo11.yaml | 标准YOLO11 |
| +AFPN | yolo11-AFPN-P2345.yaml | 四层AFPN检测头 |
| +AFPN(P345) | yolo11-AFPN-P345.yaml | 三层AFPN检测头 |
| +C3k2+AFPN | yolo11-c3k2-AFPN-P2345.yaml | C3k2+AFPN |
| **Ours** | my-yolo-fdpn-sope-c3k2-emsc4_1.yaml | FDPN+SOPE+C3k2_EMSC |

## License

This project is based on [Ultralytics YOLO](https://github.com/ultralytics/ultralytics), licensed under AGPL-3.0.
