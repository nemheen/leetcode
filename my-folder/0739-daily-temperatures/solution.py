class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize the result list with zeros
        stack = []  # Create a stack to store indices of temperatures

        for i in range(n):
            # While the stack is not empty and the current temperature is greater than
            # the temperature at the index stored in the stack, update the result
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()  # Get the index from the stack
                result[j] = i - j  # Calculate the number of days to wait
            stack.append(i)  # Push the current index onto the stack

        return result
