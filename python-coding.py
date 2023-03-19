def dirReduc(plan):
    opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    stack = []
    for direction in plan:
        if stack and opposites[direction] == stack[-1]:
            stack.pop()
        else:
            stack.append(direction)
    return stack
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
