'''
Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
'''
# !!! Запускается в Google.Colab

import seaborn as sns

penguins = sns.load_dataset("penguins")

penguins.loc[penguins['bill_length_mm'] < 35, 'bill_type'] = 'low'
penguins.loc[(penguins['bill_length_mm'] > 35) & (penguins['bill_length_mm'] < 42), 'bill_type'] = 'middle'
penguins.loc[penguins['bill_length_mm'] > 42, 'bill_type'] = 'high'


penguins.head()