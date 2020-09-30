import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.winter, edgecolor='none', s=40)

# Zdefiniowanie tytułu wykresu i etykiet osi.
plt.title("Sześciany liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Sześciany wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet.
plt.tick_params(axis='both', which='major', labelsize=14)

# Zdefiniowanie zakresu dla każdej osi.
plt.axis([0, 6000, 0, 110000000000])

plt.savefig('s_plot.png', bbox_inches='tight')
