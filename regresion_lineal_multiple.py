import numpy as np
from sklearn.linear_model import LinearRegression

# X: Variables independientes (ej. 3 muestras, 2 características)
X = np.array([[1, 2], [2, 4], [3, 6]])
# y: Variable dependiente objetivo
y = np.array([5, 11, 15])

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Ver coeficientes e intersección
print("Coeficientes:", modelo.coef_)
print("Intersección:", modelo.intercept_)
