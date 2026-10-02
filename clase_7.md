# Aritmética modular

## Notación útil

### Congruencia
Dos números enteros $a$ y $b$ son congruentes módulo $n$ si tienen el mismo resto al dividir por $n$. Se escribe $a \equiv_n b$. Ej:
$$
8 \equiv_3 5 \equiv_3 2
$$
8 es congruente con módulo 3 con 5 y 2, ya que todos dejan un resto de 2 al dividir por 3.



$$ 
a \equiv_m b \iff m \mid a - b
$$
$$
a = m . k + v
\hspace{5mm} \text{con } 0 \leq v \lt m \hspace{5mm} k \in \mathbb{Z}
$$
$$
b = m . q + r
\hspace{5mm} \text{con } 0 \leq r \lt m \hspace{5mm} q \in \mathbb{Z}
$$

$$
a - b = m.k + r - (m.q + r) 
$$
$$
a - b = m.k - m.q \rightarrow a - b = m(k - q) \hspace{5mm} \text{con } k - q \in \mathbb{Z}
$$
$$
\therefore m \mid a - b
$$



### Clases de equivalencia
Dado un número entero $n$, se define la relación de equivalencia $\equiv_n$ en $\mathbb{Z}$ como:
$$
a \equiv_n b \iff a - b \equiv 0 \pmod{n}
$$
$$
\overline{a} = \overline{b} \hspace{5mm} \text{en } \mathbb{Z}_n
$$

Qué significa el overline en $\overline{a}$?
El overline en $\overline{a}$ representa la clase de equivalencia del número entero $a$ bajo la relación de congruencia módulo $n$. Es decir, $\overline{a}$ es el conjunto de todos los enteros que son congruentes con $a$ módulo $n$.
En otras palabras, $\overline{a}$ contiene todos los enteros $b$ tales que $b \equiv_n a$. Por ejemplo, si $n = 3$ y $a = 2$, entonces la clase de equivalencia $\overline{2}$ en $\mathbb{Z}_3$ sería el conjunto de todos los enteros que dejan un resto de 2 al dividir por 3, es decir, $\overline{2} = \{..., -4, -1, 2, 5, 8, ...\}$.


## Operaciones en $\mathbb{Z}_n$
Dadas dos clases de equivalencia $\overline{a}$ y $\overline{b}$ en $\mathbb{Z}_n$, se definen las siguientes operaciones:
$$
\overline{a} + \overline{b} = \overline{a + b}
$$
$$
\overline{a} \cdot \overline{b} = \overline{a \cdot b}
$$

### Deducción en clase:
Si la tabla no es simétrica quiere decir que la operación no es conmutativa. Si la tabla no es cerrada quiere decir que la operación no es cerrada. Si la tabla no tiene identidad quiere decir que la operación no tiene elemento neutro. Si la tabla no tiene inversos quiere decir que la operación no tiene inversos.

## Invertibilidad
Sea $\overline{a} \in \mathbb{Z}_n$. Se dice que $\overline{a}$ es invertible si existe $\overline{b} \in \mathbb{Z}_n$ tal que:
$$
\overline{a} \cdot \overline{b} = \overline{1}
$$

Por ejemplo, en $\mathbb{Z}_4$, $\overline{3}$ es invertible ya que $\overline{3} \cdot \overline{3} = \overline{9} = \overline{1}$.


## Propiedad de Bezout
Sea $a, b \in \mathbb{Z}$, entonces existen $x, y \in \mathbb{Z}$ tales que:
$$
a \cdot x + b \cdot y = \text{mcd}(a, b)
$$


## EMPEZAR CON LAS 4 PROPIEDADES PARA EL PARCIAL DE RELACIONES
Cómo se puede hacer para las 4 cosas que dijo y las transitividad, y esas cosas :'D

    