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
