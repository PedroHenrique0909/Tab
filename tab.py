n1 = int(2)
n2 = int(2)

while n1 < 10:
    quest = int(input(f"{n1} X {n2}: "))
    if quest == n1 * n2:
        n2 = n2 + 1
    else:
        n2 = 2
    if n2 == 11:
        n1 = n1 + 1
        n2 = 2