import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Шаг 1: Загрузка данных

df = pd.read_csv('bottle.csv')
df_binary = df[['Salnty', 'T_degC']]

# Шаг 2: Очистка данных
df_binary.columns = ['Sal', 'Temp']
df_binary.fillna(method='ffill', inplace=True)

# Шаг 3: Визуализация данных
sns.lmplot(x="Sal", y="Temp", data=df_binary, order=2, ci=None)
plt.title("Зависимость температуры от солёности")
plt.show()

# Шаг 4: Подготовка данных
X = np.array(df_binary['Sal']).reshape(-1, 1)
y = np.array(df_binary['Temp']).reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Шаг 5: Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Шаг 6: Оценка модели
print(f"Коэффициенты модели: {model.coef_}")
print(f"Перехват: {model.intercept_}")
print(f"Точность модели: {model.score(X_test, y_test):.2f}")

# Шаг 7: Прогнозирование и визуализация
y_pred = model.predict(X_test)
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='black')
plt.title("Прогноз температуры по солёности")
plt.show()
