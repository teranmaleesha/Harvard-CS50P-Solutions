grocery = {}
while True:
    try:
        item = input().strip().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print()
        for item in sorted(grocery.keys()):
            print(f"{grocery[item]} {item}")
        break


