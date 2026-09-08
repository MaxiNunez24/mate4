# Clase inicial
## Conceptos a repasar
- Límites
- Funciones
- Cociente incremental
- Derivadas
- Cuando una función es derivable (Cociente Incremental)
- Pares ordenados
- Gráficas de funciones
- Circunferencias



## Conceptos nuevos
- Plano en R³
- Suma de funciones: 
  - (f + g)(x) = f(x) + g(x)
- Curvas de nivel para cada valor de nuestra función vamos cortando y viendo la forma de la gráfica, es decir, para cada valor de z vamos a tener una curva de nivel. Pudiendo ser circunferencia o elipse.

### Límite y continuidad
Se dice que una función f(x,y) tiene límite L cuando (x,y) tiende a (x0,y0) si para todo ε>0 existe δ>0 tal que si 0<√((x-x0)²+(y-y0)²)<δ entonces |f(x,y)-L|<ε.

- La distancia es siempre positiva, por lo que no es necesario poner el valor absoluto en la distancia.
- Epsilon es la distancia que queremos que esté la función respecto al límite es un valor chiquito.
- Delta es la distancia que queremos que esté el punto respecto al punto donde queremos que se acerque la función.

La diferencia |f(x,y)-L|<ε es la distancia entre los números f(x,y) y L, en el plano cartesiano es la distancia entre los puntos (x,y,f(x,y)) y (x0,y0,L).

- Límites iterados: Desarmar el límite fijando una variable y dejando que la otra se acerque al valor deseado, y luego hacer lo mismo con la otra variable. Si los límites iterados son iguales, entonces el límite existe y es igual a ese valor. Si los límites iterados son diferentes, entonces el límite no existe.


### Reglas útiles para límites
- |a| ≤ b = -b ≤ a ≤ b
Ejemplo:
  - Lim(x,y) -> (0,0) (5x²y) / (x² + y²)
  - | (5x²y) / (x² + y²) | = 5 |y| (x² / x² + y²)  
    - (x² / x² + y²) <= 1
  - | (5x²y) / (x² + y²) | <= 5 |y| 
  - Lim(x,y) -> (0,0) -5 < y < 5 = 0