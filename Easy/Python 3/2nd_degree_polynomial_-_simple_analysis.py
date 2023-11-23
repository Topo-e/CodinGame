import math

def calculer_racines_et_intersection_y(a, b, c):
    # Cas particuliers quand a est égal à zéro
    if a == 0:
        if b == 0:
            if c == 0:
                # Cas spécial : y = 0, le seul point est (0, 0)
                return [(0, 0)]
            else:
                # Cas spécial : ligne horizontale y = c
                return [(0, round(c, 2))]
        else:
            # Cas spécial : équation linéaire, croise l'axe des x à (-c/b, 0)
            x_intercept = round(-c / b, 2)
            return [(x_intercept, 0), (0, round(c, 2))]

    # Calculer le discriminant
    delta = b**2 - 4*a*c

    # Si delta < 0, pas de racines réelles
    if delta < 0:
        return [(0, round(c, 2))]

    # Si delta = 0, une seule racine réelle
    elif delta == 0:
        x_racine = round(-b / (2*a), 2)
        y_racine = round(a*x_racine**2 + b*x_racine + c, 2)
        return [(x_racine, y_racine), (0, round(c, 2))]

    # Si delta > 0, deux racines réelles
    else:
        x1 = round((-b + math.sqrt(delta)) / (2*a), 2)
        x2 = round((-b - math.sqrt(delta)) / (2*a), 2)
        y1 = round(a*x1**2 + b*x1 + c, 2)
        y2 = round(a*x2**2 + b*x2 + c, 2)
        return sorted([(x1, y1), (x2, y2), (0, round(c, 2))])

# Entrées
coefficients = list(map(float, input().split()))

# Calculer les points d'intersection
points_intersection = calculer_racines_et_intersection_y(*coefficients)

# Filtrer les résultats pour éliminer les zéros non nécessaires
points_intersection = [(round(x, 2) if x % 1 else round(x), round(y, 2) if y % 1 else round(y)) for x, y in points_intersection]

# Afficher les points d'intersection dans l'ordre croissant des abscisses
resultat = ",".join([f"({x},{y})" for x, y in sorted(points_intersection, key=lambda point: point[0])])
print(resultat)
