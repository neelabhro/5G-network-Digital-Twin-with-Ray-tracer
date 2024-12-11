import matplotlib.pyplot as plt
from PIL import Image

# 加载地图
map_image_path = 'D:\KTH-Study\Y2-P1\EQ2443 Project Course\data & map\map_of_R1_Hall.png'  # 替换为实际地图路径
map_image = Image.open(map_image_path)

# 测量点（手动标注像素坐标）及对应信号强度
points = [
    (100, 150, 10), (120, 200, 15), (150, 250, 20),  # 示例点位
    (180, 300, 25), (200, 350, 30), (230, 400, 35),
    # 根据实际图片填入更多点
]

# 绘制地图和点
plt.figure(figsize=(10, 8))
plt.imshow(map_image, extent=[0, map_image.size[0], 0, map_image.size[1]])

# 绘制点，颜色代表信号强度
x, y, sinr = zip(*points)
plt.scatter(x, y, c=sinr, cmap='YlOrRd', s=100, edgecolors='k')
plt.colorbar(label='SINR (dB)')
plt.title("Signal Strength Visualization")
plt.xlabel("X (pixels)")
plt.ylabel("Y (pixels)")
plt.gca().invert_yaxis()  # 图像y轴方向倒置，确保和图片一致
plt.show()
