from matplotlib import pyplot as plt
from matplotlib import font_manager


x = range(2, 26, 2)
y = [12, 15, 23, 11, 25, 23, 10, 8, 10, 12, 8, 16]
my_font = font_manager.FontProperties(fname="/System/library/Fonts/STHeiti Medium.ttc")

fig = plt.figure(figsize=(20, 8), dpi=80)
plt.xticks(range(2, 25))
plt.plot(x, y)
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
plt.title("Temperature Change Trends")
plt.savefig("./pic1.png")
plt.show()
