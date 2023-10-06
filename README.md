# maquina_de_maquinas
Traductor de NFA a FSM
Autómata Generador para Palabras Clave

Este repositorio contiene herramientas para generar y convertir Autómatas Finitos No Deterministas (NFA) a partir de un conjunto de palabras clave. A diferencia de métodos manuales, este enfoque automatizado permite generar autómatas de manera eficiente y precisa para un conjunto amplio de palabras clave.
Herramientas incluidas:

    Generador de NFA a partir de Palabras Clave: Toma un archivo con palabras clave y genera un NFA que reconoce esas palabras clave.
    Conversor de NFA a DFA: Dado un NFA en formato específico, genera una tabla de transición para su correspondiente Autómata Finito Determinista (DFA).

Cómo usar:
1. Generador de NFA:

    Coloque sus palabras clave en un archivo llamado keywords.txt, con una palabra clave por línea.
    Ejecute el script de generación:

    bash
```
    python generate_nfa_from_keywords.py
```
    El script generará un archivo nfa.txt con la definición del NFA para las palabras clave.

2. Conversor de NFA a DFA:

    Asegúrese de tener un archivo nfa.txt con la definición de su NFA (ya sea generado o creado manualmente).
    Ejecute el script de conversión:

    bash
```
    python reader.py
```
    El script mostrará la tabla de transición del DFA correspondiente en la consola.

Formato del archivo nfa.txt:

El archivo debe seguir el siguiente formato:

makefile

Σ = {alfabeto}
Q = {conjunto de estados}
F = {conjunto de estados finales}
q0 = estado_inicial
estado_origen -> estado_destino : símbolo

Por ejemplo:

less

Σ = {a, b}
Q = {q0, q1, q2}
F = {q2}
q0 = q0
q0 -> q1 : a
q1 -> q2 : b

Consideraciones:

    Asegúrese de que ninguna palabra clave sea prefijo de otra, ya que podría causar ambigüedades en la generación del NFA.
    La herramienta está diseñada principalmente para generar NFAs a partir de palabras clave. Si bien es posible editar y adaptar el archivo nfa.txt manualmente, asegúrese de seguir el formato adecuadamente para evitar errores.
