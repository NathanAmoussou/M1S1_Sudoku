import sys

def parse_grid(input_data):
    try:
        # Convertit les strings en int
        numbers = [int(num) for num in input_data]
    except ValueError:
        print("Erreur : Toutes les entrées doivent être des entiers entre -1 et 9.")
        sys.exit(1)

    # Valide le nombre d'éléments
    if len(numbers) != 81:
        print("Erreur : Exactement 81 nombres sont requis pour former une grille de Sudoku.")
        sys.exit(1)

    # Valide chaque nombre
    for num in numbers:
        if num not in range(-1, 10):
            print("Erreur : Les nombres doivent être entre 1 et 9, ou -1 pour les cellules vides.")
            sys.exit(1)

    # Convertit une "flat list" en grille 9x9
    grid = [numbers[i:i+9] for i in range(0, 81, 9)]
    return grid

def read_grid_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().split()
            grid = parse_grid(content)
            return grid
    except FileNotFoundError:
        #print(f"Error: File '{file_path}' not found.")
        print(f"Erreur : Fichier '{file_path}' introuvable.")
        sys.exit(1)

def read_grid_from_input():
    print("Entrer les 81 nombres de la grille de Sudoku (-1 pour les cellules vides), séparés par des espaces :")
    input_data = input().strip().split()
    grid = parse_grid(input_data)
    return grid

def display_grid(grid):
    print("Grille Sudoku parsée :")
    for i, row in enumerate(grid):
        row_display = ''
        for j, num in enumerate(row):
            cell = str(num) if num != -1 else '.'
            row_display += f"{cell} "
            # Séparateurs verticaux
            if (j + 1) % 3 == 0 and j != 8:
                row_display += "| "
        print(row_display.strip())
        # Séparateurs horizontaux
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

def main():
    if len(sys.argv) > 1:
        # Si un chemin de fichier est fourni comme argument de ligne de commande
        file_path = sys.argv[1]
        grid = read_grid_from_file(file_path)
    else:
        # Lire grille via l'input utilisateur
        grid = read_grid_from_input()

    # Affiche la grille parsée
    display_grid(grid)

if __name__ == "__main__":
    main()
