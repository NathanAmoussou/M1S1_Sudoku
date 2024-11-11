from abc import ABC, abstractmethod

class DeductionRule(ABC):
    def __init__(self, rule_number, successor=None): # Pour la "Chain of Responsability"
        self.rule_number = rule_number
        self.successor = successor

    @abstractmethod
    def apply(self, grid, candidates):
        """
        Essaye d'appliquer les règles de déduction sur la grille.

        Returns:
            progress (bool): True si la grille a changée, False sinon.
        """
        pass

class DirectSolve(DeductionRule):
    def __init__(self, successor=None):
        super().__init__(rule_number=1, successor=successor)

    def apply(self, grid, candidates):
        progress = False
        for i in range(9):
            for j in range(9):
                if grid[i][j] == -1 and len(candidates[i][j]) == 1:
                    value = candidates[i][j].pop()
                    grid[i][j] = value
                    self.update_candidates(grid, candidates, i, j, value)
                    progress = True
        if progress:
            return self.rule_number
        elif self.successor:
            return self.successor.apply(grid, candidates)  # Passe au successeur
        else:
            return 0  # Pas de progrès ni de successeur

    @staticmethod
    def update_candidates(grid, candidates, row, col, value):
        # Supprime les valeurs des candidats dans les mêmes lignes, colonnes et blocs
        for k in range(9):
            candidates[row][k].discard(value)
            candidates[k][col].discard(value)
        block_row, block_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(block_row, block_row + 3):
            for j in range(block_col, block_col + 3):
                candidates[i][j].discard(value)


class LockedCandidate(DeductionRule):
    def __init__(self, successor=None):
        super().__init__(rule_number=2, successor=successor)

    def apply(self, grid, candidates):
        progress = False
        for num in range(1, 10):
            # Vérifie chaque bloc
            for block_row in range(0, 9, 3):
                for block_col in range(0, 9, 3):
                    # Collecte les positions où num est candidat du bloc
                    positions = []
                    for i in range(block_row, block_row + 3):
                        for j in range(block_col, block_col + 3):
                            if num in candidates[i][j]:
                                positions.append((i, j))
                    if not positions:
                        continue
                    # Vérifie si les candidats sont dans la même ligne
                    rows = {pos[0] for pos in positions}
                    if len(rows) == 1:
                        row = rows.pop()
                        for col in range(9):
                            if not (block_col <= col < block_col + 3) and num in candidates[row][col]:
                                candidates[row][col].remove(num)
                                progress = True
                    # Vérifie si les candidats sont dans la même colonne
                    cols = {pos[1] for pos in positions}
                    if len(cols) == 1:
                        col = cols.pop()
                        for row in range(9):
                            if not (block_row <= row < block_row + 3) and num in candidates[row][col]:
                                candidates[row][col].remove(num)
                                progress = True
        if progress:
            return self.rule_number
        elif self.successor:
            return self.successor.apply(grid, candidates)
        else:
            return 0


class NakedPair(DeductionRule):
    def __init__(self, successor=None):
        super().__init__(rule_number=3, successor=successor)

    def apply(self, grid, candidates):
        progress = False
        units = self.get_all_units()
        for unit in units:
            # Trouve toutes les "cells" avec exactement deux candidats
            pairs = [(cell, candidates[cell[0]][cell[1]]) for cell in unit if len(candidates[cell[0]][cell[1]]) == 2]
            # Check pour les "naked pairs"
            seen = {}
            for cell, candidate_set in pairs:
                candidate_tuple = tuple(sorted(candidate_set))
                if candidate_tuple in seen:
                    # "Naked pair"" trouvée
                    other_cell = seen[candidate_tuple]
                    # Élimine ces candidats des autres "cells" de l'unité
                    for target_cell in unit:
                        if target_cell != cell and target_cell != other_cell:
                            if candidates[target_cell[0]][target_cell[1]].intersection(candidate_set):
                                candidates[target_cell[0]][target_cell[1]] -= candidate_set
                                progress = True
                else:
                    seen[candidate_tuple] = cell
        if progress:
            return self.rule_number
        elif self.successor:
            return self.successor.apply(grid, candidates)
        else:
            return 0

    @staticmethod
    def get_all_units():
        units = []
        # Lignes
        for i in range(9):
            units.append([(i, j) for j in range(9)])
        # Colonnes
        for j in range(9):
            units.append([(i, j) for i in range(9)])
        # Blocs
        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                unit = []
                for i in range(block_row, block_row + 3):
                    for j in range(block_col, block_col + 3):
                        unit.append((i, j))
                units.append(unit)
        return units

class HiddenPair(DeductionRule):
    def __init__(self, successor=None):
        super().__init__(rule_number=4, successor=successor)

    def apply(self, grid, candidates):
        progress = False
        units = self.get_all_units()
        for unit in units:
            # Compte les occurences de chaque candidat dans une unité
            candidate_positions = {}
            for num in range(1, 10):
                positions = [cell for cell in unit if num in candidates[cell[0]][cell[1]]]
                if len(positions) == 2:
                    candidate_positions.setdefault(frozenset(positions), []).append(num)
            # Vérifie les "hidden pairs"
            for cells, nums in candidate_positions.items():
                if len(nums) == 2:
                    nums_set = set(nums)
                    for cell in cells:
                        i, j = cell
                        if candidates[i][j] != nums_set:
                            candidates[i][j] = nums_set
                            progress = True
        if progress:
            return self.rule_number
        elif self.successor:
            return self.successor.apply(grid, candidates)
        else:
            return 0

    @staticmethod
    def get_all_units():
        # Ré-utilise la même méthode de NakedPair
        return NakedPair.get_all_units()


class DeductionRuleFactory:
    @staticmethod
    def create_rule_chain():
        # Instantiate deduction rules and link them
        # Instancie règles de déduction et les lie
        hidden_pair = HiddenPair()
        naked_pair = NakedPair(successor=hidden_pair)
        locked_candidate = LockedCandidate(successor=naked_pair)
        direct_solve = DirectSolve(successor=locked_candidate)
        return direct_solve  # Début de la chaîne
