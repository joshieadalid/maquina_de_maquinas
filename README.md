# Máquina de Máquinas: Generador y Conversor de Autómatas

Un conjunto de herramientas diseñadas para facilitar la generación y conversión de Autómatas Finitos No Deterministas (NFA) basados en palabras clave. Elimina la necesidad de crear NFAs manualmente y permite la creación y conversión eficiente para un amplio conjunto de palabras clave.

## Características

- **Generador de NFA**: A partir de un archivo con palabras clave, genera un NFA que las reconoce.
  
- **Conversor de NFA a DFA**: Convierte un NFA dado a su correspondiente Autómata Finito Determinista (DFA) mostrando una tabla de transición.

## Instrucciones de Uso

### 1. Generación del NFA

1.1. Crea un archivo llamado `keywords.txt` y lista cada palabra clave en una _línea diferente_.
    Ejemplo:
    ```
    _Packed
    auto
    break
    case
    char
    const
    continue
    default
    do
    double
    else
    enum
    extern
    float
    for
    goto
    if
    int
    long
    register
    return
    short
    signed
    sizeof
    static
    struct
    switch
    typedef
    union
    unsigned
    void
    volatile
    while
    ```
    
1.2. Ejecuta el generador:
```bash
python keywords_nfa_generator.py
```
Esto producirá un archivo `nfa.txt` con la definición del NFA basada en las palabras clave.

2. Conversión de NFA a DFA
2.1. Asegúrate de contar con un archivo `nfa.txt` (ya sea generado como se indicó anteriormente o creado manualmente).
2.2. Ejecuta el conversor:
```bash
python reader.py
```
Verás la tabla de transición del DFA en la consola.
Formato del Archivo `nfa.txt`

El archivo debe respetar el siguiente formato:
```
Σ = {alfabeto}
Q = {conjunto de estados}
F = {conjunto de estados finales}
q0 = estado_inicial
estado_origen -> estado_destino : símbolo
```
Ejemplo:

```
Σ = {a, b}
Q = {q0, q1, q2}
F = {q2}
q0 = q0
q0 -> q1 : a
q1 -> q2 : b
```
Consideraciones

    Prefijos: Asegúrate de que ninguna palabra clave sea prefijo de otra. Esto podría causar ambigüedades al generar el NFA.

    Edición manual de `nfa.txt`: Aunque es posible, ten cuidado al editar el archivo manualmente. Asegúrate de seguir el formato adecuadamente para evitar errores en la conversión.
