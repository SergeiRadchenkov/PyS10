from seaborn import load_dataset, scatterplot, PairGrid, displot, heatmap
from matplotlib.pyplot import show

data = load_dataset('penguins')

# ● Использовать 2-3 точечных графика
# scatterplot(data=data, x='flipper_length_mm', y='body_mass_g')

# ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
# scatterplot(data=data, x='flipper_length_mm', y='body_mass_g', size=5, style='island', hue='sex')

# ● Использовать PairGrid с типом графика на ваш выбор
# g = PairGrid(data=data, hue='species')
# g.map(scatterplot)

# ● Изобразить Heatmap
# displot(data=data, x='bill_depth_mm', y='bill_length_mm', hue='species')

# glue = load_dataset('glue').pivot(index='Model', columns='Task', values='Score')
# heatmap(glue)

# ● Использовать 2-3 гистограммы
data['bill_depth_mm'].hist(bins=10)

show()