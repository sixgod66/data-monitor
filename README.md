# data-monitor
异常数据监控

# 背景：
很多业务中需要发现业务异常点，用于监控，如何自动发现，取均值，中值，到底哪些点比较合适，可以考虑一下以下的方法：

## 两种方案：
1. 基于高斯分布的业务异常点监控：https://github.com/trekhleb/homemade-machine-learning/tree/master/homemade/anomaly_detection   仔细看里面的jupyter的demo， jupyter的demo如下： https://nbviewer.jupyter.org/github/trekhleb/homemade-machine-learning/blob/master/notebooks/anomaly_detection/anomaly_detection_gaussian_demo.ipynb
2. 通过箱体的下限来自动识别异常点： https://tianchi.aliyun.com/dataset/notebook/detail?spm=5176.12282042.0.0.611c290aEFgnEl&postId=6772  里面有使用箱体，具体如下：里面有箱体的汇报，如何获得箱体的下限研究一下     
        plt.subplot(122)
        train_data.boxplot(column='Age',showfliers=False)
        plt.show()
