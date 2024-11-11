from parser import read_grid_from_file, read_grid_from_input
from solver import SudokuSolver

def main():
    # Lis la grille depuis un fichier ou un input
    import sys
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        initial_grid = read_grid_from_file(file_path)
    else:
        initial_grid = read_grid_from_input()

    # Crée ou ré-initialise l'instance du SudokuSolver
    solver = SudokuSolver(initial_grid)

    # Affiche la grille initiale
    solver.display_grid()

    # Résous la grille
    if solver.solve():
        print("Sudoku correctement résolu !")
        solver.display_grid()
        difficulty = solver.get_difficulty()
        print(f"Niveau de difficulté : {difficulty}")
    else:
        print("Résolution impossible avec les règles de déduction implémentées.")
        # Demande un d'input une valeur
        prompt_user_input(solver)
        # Ré-initialise le "solver" avec la grill à jour
        solver = SudokuSolver(solver.grid)
        # Essaye de résoudre à nouveau
        if solver.solve():
            print("Sudoku correctement résolu après l'input !")
            solver.display_grid()
        else:
            print("Résolution impossible même après l'input utilisateur.\nLa difficulté est probablement Impossible où l'input était faux.")

def prompt_user_input(solver):
    # Trouver la "cell" avec le moins de candidats
    min_candidates = 10
    cell = None  # Initialiser la "cell" pour éviter UnboundLocalError
    for i in range(9):
        for j in range(9):
            if solver.grid[i][j] == -1 and len(solver.candidates[i][j]) < min_candidates:
                min_candidates = len(solver.candidates[i][j])
                cell = (i, j)
    if cell is None or min_candidates == 10:
        print("Pas de cellules vides trouvées.")
        return
    i, j = cell
    print(f"Entrer une valeur pour la cellule ({i+1}, {j+1}) parmi les candidats {solver.candidates[i][j]} :")
    while True:
        try:
            value = int(input("Votre entrée : "))
            if value in solver.candidates[i][j]:
                solver.grid[i][j] = value
                solver.update_candidates(i, j, value)
                break
            else:
                print(f"Entrée invalide. Essayer parmi {solver.candidates[i][j]}.")
        except ValueError:
            print("Entrer un entier valide.")

if __name__ == "__main__":
    main()
