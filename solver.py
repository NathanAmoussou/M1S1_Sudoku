from singleton_meta import SingletonMeta
from deduction_rules import DeductionRuleFactory


class SudokuSolver(metaclass=SingletonMeta):
    def __init__(self, grid):
        self.grid = grid
        self.candidates = [[set(range(1, 10)) if cell == -1 else set() for cell in row] for row in grid]
        self.initialize_candidates()
        self.rule_chain = DeductionRuleFactory.create_rule_chain()
        self.highest_rule_used = 0  # Attribut pour suivre le niveau de difficulté

    def initialize_candidates(self):
        # Supprime les candidats basés sur les valeurs initiales de la grille
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != -1:
                    self.update_candidates(i, j, self.grid[i][j])

    def update_candidates(self, row, col, value):
        # Supprime les valeurs de candidats dans les mêmes lignes, colonnes et blocs
        for k in range(9):
            self.candidates[row][k].discard(value)
            self.candidates[k][col].discard(value)
        block_row, block_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(block_row, block_row + 3):
            for j in range(block_col, block_col + 3):
                self.candidates[i][j].discard(value)

    def solve(self):
        progress = True
        while progress:
            progress = False  # Redémarre la progression au début de la boucle
            rule_used = self.rule_chain.apply(self.grid, self.candidates)
            if rule_used > 0:
                self.highest_rule_used = max(self.highest_rule_used, rule_used)
                progress = True
            if self.fill_single_candidates():
                progress = True
        # Vérifie si la grille est résolue
        return all(self.grid[i][j] != -1 for i in range(9) for j in range(9))

    def fill_single_candidates(self):
        progress = False
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == -1 and len(self.candidates[i][j]) == 1:
                    value = self.candidates[i][j].pop()
                    self.grid[i][j] = value
                    self.update_candidates(i, j, value)
                    progress = True
        return progress

    def display_grid(self):
        print("Grille de Sudoku actuelle:")
        for i, row in enumerate(self.grid):
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

    def get_difficulty(self):
        if self.highest_rule_used == 1:
            return "Facile"
        elif self.highest_rule_used == 2:
            return "Moyen"
        elif self.highest_rule_used == 3:
            return "Difficile"
        elif self.highest_rule_used == 4:
            return "Très difficile"
        else:
            return "Impossible"
