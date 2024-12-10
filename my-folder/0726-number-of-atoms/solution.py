class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]  # Stack to store atom counts at each level
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                # Push a new level for nested formulas
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                # End of a nested level, process the multiplier
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i]) if start < i else 1

                # Pop the current level and apply multiplier
                current_level = stack.pop()
                for atom, count in current_level.items():
                    stack[-1][atom] += count * multiplier
            elif formula[i].isalpha():
                # Parse an atom name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]

                # Parse the count (if any)
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if start < i else 1

                # Add to the current level
                stack[-1][atom] += count
            else:
                i += 1  # Skip unrecognized characters (shouldn't happen)

        # Merge the final level into a sorted string
        final_counts = stack.pop()
        result = ''.join(f"{atom}{final_counts[atom] if final_counts[atom] > 1 else ''}"
                        for atom in sorted(final_counts))
        return result
