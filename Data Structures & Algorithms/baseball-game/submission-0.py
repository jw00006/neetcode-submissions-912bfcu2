class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            # if + add previous two elements
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            # if d double previous score
            elif operation == "D":
                stack.append(stack[-1] * 2)
            # if c remove previous element
            elif operation == "C":
                stack.pop()
            # if an int add to stack
            else:
                stack.append(int(operation))
        return sum(stack)