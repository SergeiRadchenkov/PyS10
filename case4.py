'''
Изобразить гистограмму по flipper_length_mm
с оттенком height_group. Сделать анализ.
'''
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import read_csv

penguins = read_csv('penguins.csv')

sns.histplot(penguins, x='flipper_length_mm', hue='height_group')
plt.show()