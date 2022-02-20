from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/library/Fonts/STHeiti Medium.ttc")

y_1 = [10, 11, 12, 13, 14, 15, 16, 27, 10, 20, 22, 15, 10, 23, 21, 14, 15, 16]
y_2 = [20, 25, 23, 11, 25, 23, 20, 18, 15, 12, 8, 10, 12, 11, 5, 6, 8, 10]

x_1 = range(1, 19)
x_2 = range(30, 48)

# set image size
fig = plt.figure(figsize=(20, 8), dpi=80)

# draw image
plt.scatter(x_1, y_1, label="3月份")
plt.scatter(x_2, y_2, label="10月份")

# # set X unit
_x = list(x_1) + list(x_2)
_xtick_labels = ["3月{}日".format(i) for i in x_1]
_xtick_labels += ["10月{}日".format(i - 30) for i in x_2]
plt.xticks(_x[::2], _xtick_labels[::2], fontproperties=my_font, rotation=45)

# Add Legend
plt.legend(loc="upper left", prop=my_font)

# Add description
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
plt.title("温度变化", fontproperties=my_font)
plt.savefig("./pic11.png")
plt.show()
