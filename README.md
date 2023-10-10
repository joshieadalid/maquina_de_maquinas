# Máquina de Máquinas: Generador y Conversor de Autómatas

Un conjunto de herramientas diseñadas para facilitar la generación y conversión de Autómatas Finitos No Deterministas (NFA) basados en palabras clave. Elimina la necesidad de crear NFAs manualmente y permite la creación y conversión eficiente para un amplio conjunto de palabras clave.

---

## Demostración de uso

### 1. Convertir listas de palabras a NFA
Convierte una lista a un nfa que funciona como una búsqueda de palabras en una cadena.
```python
words = ["hola", "adios"]
nfa = words2nfa(words)
```

### 2. Guardar y cargar un NFA desde un archivo JSON

```python
# Guardar NFA en archivo JSON
save_nfa(nfa, "my_nfa.json")

# Cargar NFA desde archivo JSON
loaded_nfa = load_nfa("my_nfa.json")
```

### 3. Convertir un NFA a texto y viceversa
Para usarse en texto hardcodeado, o del texto obtenido de la lectura de un archivo.

```python

# Convertir NFA a texto
nfa_text = nfa2text(nfa)
print(nfa_text)

# Convertir texto a NFA
text_nfa = text2nfa(nfa_text)
```

### 4. Convertir un NFA a un DFA (Algoritmo de subconjuntos)

```python
dfa = nfa2dfa(nfa)
```

### 5. Imprimir un DFA en formato de tabla (visualización)

```python
print_dfa(dfa)
```

### 6. Guardar un DFA en formato JSON (para su uso posterior)

```python
save_dfa(dfa, "my_dfa.json")
```

### 7. Guardar un DFA en formato CSV (para visualizar en Excel)

```python
save_dfa2csv(dfa, "my_dfa.csv")
```
### Extra: NFA en formato legible a JSON (Ejemplo 3).
```python
nfa_text = """
Σ = {w, e, b, a, y}
Q = {1, 2, 3, 4, 5, 6, 7, 8}
F = {4, 8}
q0 = 1
1 -> 1 : w,e,b,a,y
1 -> 2 : w
1 -> 5 : e
2 -> 3 : e
3 -> 4 : b
5 -> 6 : b
6 -> 7 : a
7 -> 8 : y
"""
```
Nótese la declaración múltiple de símbolos para una misma transición.
**Formato alternativo**
```python
nfa_text = """
Σ = {e, b, y, a, w}
Q = {3, 1, 7, 8, 4, 6, 2, 5}
F = {8, 4}
q0 = 1
1 -> 1, 2 : w
1 -> 1, 5 : e
1 -> 1 : b
1 -> 1 : a
1 -> 1 : y
2 -> 3 : e
3 -> 4 : b
5 -> 6 : b
6 -> 7 : a
7 -> 8 : y
"""
```
Cabe a mencionar que el formato permite una descripción concisa con la "multitransición".
