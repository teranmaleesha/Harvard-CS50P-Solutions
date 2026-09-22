while True:
    fraction = input("Fraction: ")
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y or y <= 0 or x < 0:
            continue
        percentage = round((x/y) * 100)
        break
    except(ValueError, ZeroDivisionError):
     pass
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")


