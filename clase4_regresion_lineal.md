# Clase 4: Regresión Lineal

## Motivación
La regresión lineal es una técnica fundamental en el análisis de datos que nos permite modelar la relación entre una variable dependiente y una o más variables independientes. Su importancia radica en su simplicidad, interpretabilidad y amplia aplicabilidad en diversos campos como la economía, la biología, la ingeniería y muchas otras disciplinas.

## Definición 1.2 
### Modelo de regresión lineal simple
Dado que una función lineal se define como una función de la forma:
y = mx + b

Utilizando este contexto, podemos definir el modelo de regresión lineal simple como:
(Real)
Y = B1x + B0 + epsilon
Donde: 
- B0: Intercepto o término constante
- B1: Coeficiente de la variable independiente
- epsilon: Error aleatorio o término de perturbación
    - Se estima que epsilon sigue una distribución normal con media cero y varianza constante (homocedasticidad).
    - homocedasticidad: La varianza del error es constante a lo largo de todos los niveles de la variable independiente.

Que al estimarlos obtemos:
(Estimado)
Ŷ = ^B1x + ^B0

#### El método que utilizaremos será el 
método de mínimos cuadrados ordinarios (MCO), que busca minimizar la suma de los cuadrados de las diferencias entre los valores observados y los valores predichos por el modelo.
- Esto utilizando la propiedad matemática que al elevar un número al cuadrado, se eliminan los signos negativos y se penalizan más los errores grandes que los pequeños. Haciendo que el número al cuadrado sea mayor que el número original, y que al sumarlos, se obtenga un valor positivo que represente la magnitud del error total.
- Siempre 

La fórmula para estimar los coeficientes B0 y B1 utilizando MCO es la siguiente:
- ^B1 = (Σ(xi - x̄)(yi - ȳ)) / Σ(xi - x̄)²
- ^B0 = ȳ - ^B0 = ȳ - ^B1x̄
Donde:
- xi: Valores de la variable independiente
- yi: Valores de la variable dependiente




## Ver en apunte teórico

### Residuos
### Varianza
### SCE (Suma de los cuadrados de los errores) (1.5 definición)
### Coeficiente de determinación o R² (1.6 definición)
### Coeficiente de correlación lineal (1.5 títulos)

Si el coeficiente de correlación lineal da 0 entonces no hay relación lineal entre las variables, si da 1 entonces hay una relación lineal positiva perfecta y si da -1 entonces hay una relación lineal negativa perfecta.


## Ejercicios

1. Suponga que un investigador cuenta con datos sobre la cantidad de espacio de es-
tanter ́ıa (x) dedicado a la exhibici ́on de un producto particular y los ingresos por

ventas (y) de ese producto. Es posible que el investigador desee adoptar un modelo
para el cual la l ́ınea de regresi ́on verdadera pase a trav ́es de (0, 0).
a. ¿Cu ́al ser ́ıa la ecuaci ́on de modelo m ́as apropiada para la misma?
b. Suponga que (x1, y1), . . . ,(xn, yn) son pares observados generados por el modelo
del inciso anterior y deduzca el estimador de m ́ınimos cuadrados de su coeficiente.


En el inciso C del punto 3 se debe mencionar que el valor 500 es un residuo y que está fuera de nuestro modelo de regresión lineal, por lo que no se puede predecir el valor de y para x=500. Esto se debe a que el modelo de regresión lineal solo es válido dentro del rango de los datos observados y extrapolar fuera de ese rango puede llevar a predicciones inexactas o poco confiables.


