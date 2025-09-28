def validate(pushed, popped):
    pushed = list(map(int, pushed.split()))
    popped = list(map(int, popped.split()))

    stack = []
    poped_index = 0
    for elem in pushed:
        stack.append(elem)
        while len(stack) > 0 and stack[-1] == popped[poped_index]:
            stack.pop()
            poped_index += 1
    return len(stack) == 0
