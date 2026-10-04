import warnings, os

warnings.filterwarnings('ignore')

from ultralytics import YOLO

if __name__ == '__main__':
    # 选择模型配置文件:
    # - yolo11.yaml                          : YOLO11 baseline
    # - yolo11-AFPN-P2345.yaml              : YOLO11 + AFPN (P2-P5四层检测)
    # - yolo11-AFPN-P345.yaml               : YOLO11 + AFPN (P3-P5三层检测)
    # - yolo11-c3k2-AFPN-P2345.yaml         : YOLO11 + C3k2 + AFPN
    # - my-yolo-fdpn-sope-c3k2-emsc4_1.yaml : 本文提出的改进模型 (FDPN + SOPE + C3k2_EMSC)

    model = YOLO('ultralytics/cfg/models/11/my-yolo-fdpn-sope-c3k2-emsc4_1.yaml')
    # model.load('yolo11n.pt')  # 加载预训练权重(可选)

    model.train(data='myDataSet_10/data.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=16,
                close_mosaic=0,     # 最后多少个epoch关闭mosaic数据增强，0代表全程开启
                workers=8,          # Windows下卡住可尝试设置为0
                device='0',         # GPU设备号
                optimizer='SGD',
                resume=True,        # 断点续训
                amp=False,          # loss出现nan可关闭amp
                project='runs/train',
                name='exp',
                )
