import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x ** 3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

ax.set_title("Cubes Numbers", fontsize=20)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cubes of Values', fontsize=14)

ax.axis=([0, 5100, 0, 1000000])
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()