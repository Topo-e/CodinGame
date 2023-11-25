import sys
import math

def logic_gate(input1, input2, gate_type):
    result = []

    for i, j in zip(input1, input2):
        if gate_type == "AND":
            result.append('-' if i == '_' or j == '_' else '_')
        elif gate_type == "OR":
            result.append('-' if i == '_' and j == '_' else '_')
        elif gate_type == "XOR":
            result.append('_' if (i == '_' and j == '-') or (i == '-' and j == '_') else '-')
        elif gate_type == "NAND":
            result.append('-' if i != '_' and j != '_' else '_')
        elif gate_type == "NOR":
            result.append('-' if i == '-' or j != '_' else '_')
        elif gate_type == "NXOR":
            result.append('-' if (i == '_' and j == '-') or (i == '-' and j == '_') else '_')

    # Convertir la liste en chaîne de caractères
    result_str = ''.join(result)

    # Inverse les symbole '-' et '_', cela aurait pu être fait dans les lignes ci-dessus"
    result_str = ''.join(['-' if symbol == '_' else '_' for symbol in result_str])

    return result_str

def process_signals(input_data, gate_data):
    output_data = []  # Initialise une liste vide pour stocker les résultats des sorties
    for output_name, gate_type, input_name_1, input_name_2 in gate_data:
        # Parcourt chaque ligne de gate_data, qui contient les spécifications des portes logiques

        # Trouve la valeur de données associée à input_name_1 dans input_data
        input1_data = next(data for name, data in input_data if name == input_name_1)

        # Trouve la valeur de données associée à input_name_2 dans input_data
        input2_data = next(data for name, data in input_data if name == input_name_2)

        # Applique la fonction logic_gate pour obtenir la sortie en fonction des données d'entrée et du type de porte
        output_data_value = logic_gate(input1_data, input2_data, gate_type)

        # Ajoute le résultat à la liste des résultats des sorties
        output_data.append((output_name, output_data_value))

    # Renvoie la liste complète des résultats des sorties
    return output_data

# Lecture de l'entrée, n entrées et m sorties
n = int(input())
m = int(input())

# Lecture des jeux de données d'entrée
input_data = [input().split() for _ in range(n)]

#print(input_data)

# Lecture des spécifications des portes logiques
gate_data = [input().split() for _ in range(m)]

# Appel de la fonction process_signals
results = process_signals(input_data, gate_data)

# Affichage des résultats
for signal, data in results:
    print(f"{signal} {data}")
