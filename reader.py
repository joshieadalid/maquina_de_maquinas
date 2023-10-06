import re  # Importa el módulo de expresiones regulares

def read_nfa(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    nfa = {
        'Σ': set(),
        'Q': set(),
        'F': set(),
        'δ': {},
        'q0': None  # Agregar esto para el estado inicial
    }

    for line in lines:
        line = line.strip()
        print(f"Processing line: '{line}'")  # Para depuración
        if line.startswith('Σ'):
            nfa['Σ'] = set(line[line.find('{') + 1:line.find('}')].replace(' ', '').split(','))
        elif line.startswith('Q'):
            nfa['Q'] = set(line[line.find('{') + 1:line.find('}')].replace(' ', '').split(','))
        elif line.startswith('F'):
            nfa['F'] = set(line[line.find('{') + 1:line.find('}')].replace(' ', '').split(','))
        elif re.match(r'^q0\s*=\s*\w+$', line):  # Usar una expresión regular para determinar si la línea define el estado inicial
            nfa['q0'] = line.split('=')[1].strip()  # Asignar el estado inicial
        elif '->' in line:
            src, rest = line.split('->')
            dest, symbols = rest.split(':')
            src, dest = src.strip(), dest.strip()
            symbols = symbols.strip().split(',')

            if src not in nfa['δ']:
                nfa['δ'][src] = {}
            for symbol in symbols:
                if symbol not in nfa['δ'][src]:
                    nfa['δ'][src][symbol] = set()
                nfa['δ'][src][symbol].add(dest)

    return nfa



def transition(nfa, state_subset, symbol):
    """Dado un conjunto de estados y un símbolo, devuelve el conjunto de estados al que se puede llegar"""

    result = set()

    for state in state_subset:
        if state in nfa['δ'] and symbol in nfa['δ'][state]:
            result = result.union(nfa['δ'][state][symbol])

    return result


def construct_dfa_table(nfa):
    alphabet = list(nfa['Σ'])
    initial_state = {nfa['q0']}  # Usar el estado inicial del NFA
    explored_states = {frozenset(initial_state)}
    queue = [initial_state]
    table = []

    while queue:
        current_state = queue.pop(0)
        row = [current_state]

        for c in alphabet:
            next_state = transition(nfa, current_state, c)
            row.append(next_state)
            if frozenset(next_state) not in explored_states:
                explored_states.add(frozenset(next_state))
                queue.append(next_state)

        table.append(row)

    # Calcular el ancho máximo de cada columna
    column_widths = [max(len(str(row[i])) for row in table) for i in range(len(alphabet) + 1)]
    header_widths = [len("Estados")] + [len(c) for c in alphabet]
    column_widths = [max(column_widths[i], header_widths[i]) for i in range(len(column_widths))]

    # Imprimir la tabla con columnas alineadas
    print(
        " ".join(["Estados".ljust(column_widths[0])] + [c.ljust(column_widths[i + 1]) for i, c in enumerate(alphabet)]))
    for row in table:
        print(" ".join([str(s).ljust(column_widths[i]) for i, s in enumerate(row)]))

    return table


# Ejemplo de uso:
nfa = read_nfa("nfa.txt")
print(nfa)
construct_dfa_table(nfa)
