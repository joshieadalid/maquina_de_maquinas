import json
import re
import csv

def load_nfa(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    nfa = {'Σ': set(data['Σ']), 'Q': set(data['Q']), 'F': set(data['F']),
        'δ': {state: {symbol: set(destinations) for symbol, destinations in transition.items()} for state, transition in
              data['δ'].items()}, 'q0': data['q0']}

    return nfa


def save_nfa(nfa, filename):
    data = {'Σ': list(nfa['Σ']), 'Q': list(nfa['Q']), 'F': list(nfa['F']),
        'δ': {state: {symbol: list(destinations) for symbol, destinations in transition.items()} for state, transition
              in nfa['δ'].items()}, 'q0': nfa['q0']}

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def save_dfa(dfa, filename):
    data = {'Σ': list(dfa['Σ']), 'Q': [",".join(list(state)) for state in dfa['Q']],
        'F': [",".join(list(state)) for state in dfa['F']], 'δ': {
            ",".join(list(state)): {symbol: ",".join(list(destinations)) for symbol, destinations in transition.items()}
            for state, transition in dfa['δ'].items()}, 'q0': ",".join(list(dfa['q0']))}

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def save_dfa2csv(dfa, filename="dfa.csv"):
    """
    Convert a Deterministic Finite Automaton (DFA) to a CSV file.

    Parameters:
        - dfa: A dictionary representing the DFA.
        - filename: Name of the CSV file to write to.

    Returns:
        - None (writes to a file)
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header with the symbols of the alphabet
        writer.writerow([''] + list(dfa['Σ']))

        # Write transitions for each state
        for state, transitions in dfa['δ'].items():
            row = [state]
            for symbol in dfa['Σ']:
                # Append the destination state or an empty string if no transition for the symbol
                row.append(transitions.get(symbol, ''))
            writer.writerow(row)

def transition(nfa, state_subset, symbol):
    """Dado un conjunto de estados y un símbolo, devuelve el conjunto de estados al que se puede llegar"""

    result = set()

    for state in state_subset:
        if state in nfa['δ'] and symbol in nfa['δ'][state]:
            result = result.union(nfa['δ'][state][symbol])

    return result


def words2nfa(words):
    """
    Convert a list of words into a Non-deterministic Finite Automaton (NFA).

    Parameters:
        - words: List of words to be recognized by the NFA.

    Returns:
        - A dictionary representing the NFA.
    """
    # Initialize NFA structure
    nfa = {
        'Σ': set(),  # Symbols
        'Q': set(),  # States
        'F': set(),  # Final states
        'δ': {},  # Transition function
        'q0': 'q_initial'  # Initial state
    }

    nfa['Q'].add('q_initial')

    for word in words:
        current_state = 'q_initial'

        for i, symbol in enumerate(word):
            # Update the set of symbols
            nfa['Σ'].add(symbol)

            # Construct the next state based on the word being completed
            next_state = f"{word[:i + 1]}"

            # Add next state to the set of states
            nfa['Q'].add(next_state)

            # Update the transition function
            if current_state not in nfa['δ']:
                nfa['δ'][current_state] = {}
            if symbol not in nfa['δ'][current_state]:
                nfa['δ'][current_state][symbol] = [next_state]
            else:
                nfa['δ'][current_state][symbol].append(next_state)

            current_state = next_state

        # Mark the final state for the word as a final state
        nfa['F'].add(current_state)

    return nfa


def text2nfa(text):
    lines = text.splitlines()

    nfa = {'Σ': set(), 'Q': set(), 'F': set(), 'δ': {}, 'q0': None}

    for line in lines:
        line = line.strip()
        if line.startswith('Σ'):
            symbols = line[line.find('{')+1:line.find('}')].split(',')
            nfa['Σ'] = set([sym.strip() for sym in symbols])
        elif line.startswith('Q'):
            states = line[line.find('{')+1:line.find('}')].split(',')
            nfa['Q'] = set([state.strip() for state in states])
        elif line.startswith('F'):
            final_states = line[line.find('{')+1:line.find('}')].split(',')
            nfa['F'] = set([state.strip() for state in final_states])
        elif '->' in line:
            src, rest = line.split('->')
            dest, symbols = rest.split(':')
            src = src.strip()
            dest = dest.strip()
            symbols = symbols.strip().split(',')

            if src not in nfa['δ']:
                nfa['δ'][src] = {}
            for symbol in symbols:
                symbol = symbol.strip()
                if symbol in nfa['Σ']:  # Verificar que el símbolo esté en el alfabeto
                    if symbol not in nfa['δ'][src]:
                        nfa['δ'][src][symbol] = [dest]
                    else:
                        nfa['δ'][src][symbol].append(dest)
        elif re.match(r'^q0\s*=\s*\w+$', line):  # Determinar si la línea define el estado inicial
            nfa['q0'] = line.split('=')[1].strip()

    json_data = {'Σ': list(nfa['Σ']), 'Q': list(nfa['Q']), 'F': list(nfa['F']), 'δ': nfa['δ'], 'q0': nfa['q0']}
    return json_data


def nfa2text(nfa):
    lines = []

    # Add alphabet
    lines.append("Σ = {" + ", ".join(nfa["Σ"]) + "}")
    # Add states
    lines.append("Q = {" + ", ".join(nfa["Q"]) + "}")
    # Add final states
    lines.append("F = {" + ", ".join(nfa["F"]) + "}")
    # Add start state
    lines.append("q0 = " + nfa["q0"])

    # Add transitions
    for state, transitions in nfa["δ"].items():
        for symbol, destinations in transitions.items():
            destinations_str = ", ".join(destinations)
            lines.append(f"{state} -> {destinations_str} : {symbol}")

    return "\n".join(lines)


def nfa2dfa(nfa):
    alphabet = list(nfa['Σ'])
    initial_state = {nfa['q0']}
    explored_states = {frozenset(initial_state)}
    queue = [initial_state]
    dfa_transitions = []

    while queue:
        current_state = queue.pop(0)
        transitions = {}

        for c in alphabet:
            next_state = transition(nfa, current_state, c)
            transitions[c] = next_state
            if frozenset(next_state) not in explored_states:
                explored_states.add(frozenset(next_state))
                queue.append(next_state)

        dfa_transitions.append((current_state, transitions))

    dfa = {'Σ': nfa['Σ'], 'Q': [",".join(sorted(state)) for state, _ in dfa_transitions],
        'F': [",".join(sorted(state)) for state in explored_states if state & set(nfa['F'])],
        'δ': {",".join(sorted(state)): {symbol: ",".join(sorted(dest)) for symbol, dest in transitions.items()} for
              state, transitions in dfa_transitions}, 'q0': ",".join(sorted(initial_state))}

    return dfa


def print_dfa(dfa_json):
    states = dfa_json['Q']
    alphabet = dfa_json['Σ']

    # Calcular el ancho máximo de cada columna
    column_widths = [max(len(state) for state in states)]
    for symbol in alphabet:
        column_widths.append(max(len(dfa_json['δ'][state][symbol]) for state in states))

    header_widths = [len("Estados")] + [len(c) for c in alphabet]
    column_widths = [max(column_widths[i], header_widths[i]) for i in range(len(column_widths))]

    # Imprimir la tabla con columnas alineadas
    separator = "+".join(['-' * (width + 2) for width in column_widths])
    print(separator)
    print("| " + " | ".join(
        ["Estados".ljust(column_widths[0])] + [c.ljust(column_widths[i + 1]) for i, c in enumerate(alphabet)]) + " |")
    print(separator)

    for state in states:
        transitions = [dfa_json['δ'][state][symbol] for symbol in alphabet]
        print("| " + " | ".join([state.ljust(column_widths[0])] + [trans.ljust(column_widths[i + 1]) for i, trans in
                                                                   enumerate(transitions)]) + " |")
        print(separator)
