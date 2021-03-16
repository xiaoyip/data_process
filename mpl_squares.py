import matplotlib.pyplot as plt

input_value = [i for i in range(1, 6)]
squares = [i**2 for i in range(1, 6)]

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
fig, ax = plt.subplots()
ax.plot(input_value, squares, linewidth=3)

# 设置图标标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()
