import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def regresion_lineal(x, y):
    """
    Realiza una regresión lineal y devuelve los arrays de la recta de regresión
    y el coeficiente de determinación R²
    
    Parámetros:
    x: array de valores independientes
    y: array de valores dependientes
    
    Retorna:
    x_reg: array de valores x para la recta de regresión
    y_reg: array de valores y predichos para la recta de regresión
    r_cuadrado: coeficiente de determinación R²
    """
    
    # Convertir a arrays numpy si no lo son
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)
    
    # Crear y entrenar el modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(x, y)
    
    # Predecir valores para la recta de regresión
    x_min = np.min(x)
    x_max = np.max(x)
    x_reg = np.linspace(x_min, x_max, 100).reshape(-1, 1)
    y_reg = modelo.predict(x_reg)
    
    # Calcular R²
    y_pred = modelo.predict(x)
    r_cuadrado = r2_score(y, y_pred)
    
    # Devolver arrays aplanados (1D) para consistencia
    return x_reg.flatten(), y_reg, r_cuadrado