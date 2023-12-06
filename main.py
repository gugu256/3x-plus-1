print("3x+1 Solver\n")

a = int(input("a = "))
b = int(input("b = ")) + 1
for x in range(a, b):
    print(f"\nTrying {x}")
    y = (x+1-1) # don't ever question this
    z = 0
    while True:
        z += 1
        if y % 2 == 0:
            y = y / 2
        else:
            y = 3 * y + 1
        print(f"Change #{z} | x = {y}")
        if y == 4:
            print("Reached loop.")
            break