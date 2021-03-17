import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        low = int(row[6])
        lows.append(low)


plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
fig, ax = plt.subplots(figsize=(10, 6))
fig.autofmt_xdate()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("2018年每日最高/最低温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("温度（F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
