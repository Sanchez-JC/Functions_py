import numpy as np
from sklearn.linear_model import LinearRegression

def regresion_lineal(x, y):
    """
    Realiza una regresión lineal y devuelve:
    - pendiente (coeficiente de la recta)
    - intercepto
    - R² (coeficiente de determinación)
    - x_reg: array de valores x para graficar la recta
    - y_reg: array de valores y predichos para la recta
    
    Parámetros:
    x: array de valores independientes
    y: array de valores dependientes
    
    Retorna:
    pendiente, intercepto, r2, x_reg, y_reg
    """
    # Convertir a arrays numpy y darles forma adecuada
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)

    # Crear y entrenar el modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(x, y)

    # Obtener parámetros de la regresión
    pendiente = modelo.coef_[0]
    intercepto = modelo.intercept_
    r2 = modelo.score(x, y)

    # Crear arrays para la recta de regresión
    x_min, x_max = np.min(x), np.max(x)
    x_reg = np.linspace(x_min, x_max, 100).reshape(-1, 1)
    y_reg = modelo.predict(x_reg)

    return pendiente, intercepto, r2, x_reg.flatten(), y_reg
