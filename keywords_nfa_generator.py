def generate_nfa_from_keywords(filename):
    with open(filename, 'r') as file:
        keywords = [line.strip() for line in file.readlines() if line.strip()]

    # Paso 2: Generar el alfabeto
    alphabet = set()
    for word in keywords:
        for char in word:
            alphabet.add(char)

    # Paso 3: Crear estados
    states = ["q0"]  # Estado inicial
    for word in keywords:
        for i in range(len(word)):
            state_name = f"q_{word[:i+1]}"
            if state_name not in states:
                states.append(state_name)

    # Paso 4: Crear transiciones
    transitions = []

    for word in keywords:
        src = "q0"
        for i in range(len(word)):
            dest = f"q_{word[:i+1]}"
            transitions.append((src, word[i], dest))
            src = dest

    # Paso 5: Determinar estados finales
    final_states = [f"q_{word}" for word in keywords]

    # Escribir al archivo
    with open("nfa.txt", 'w') as file:
        file.write("Σ = {" + ", ".join(sorted(alphabet)) + "}\n")
        file.write("Q = {" + ", ".join(states) + "}\n")
        file.write("F = {" + ", ".join(final_states) + "}\n")
        file.write("q0 = q0\n")  # El estado inicial es q0

        for transition in transitions:
            file.write(f"{transition[0]} -> {transition[2]} : {transition[1]}\n")

    print("NFA definition written to nfa.txt")


# Uso:
generate_nfa_from_keywords("keywords.txt")
