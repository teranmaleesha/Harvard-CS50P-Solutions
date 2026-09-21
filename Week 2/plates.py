def main():
    plate = input("Plate : ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if not (2 <= len(s) <=6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False
    has_number = False
    for c in s:
        if c.isdigit():
            if not has_number and c == '0':
                return False
            has_number = True
        elif has_number and c.isalpha():
            return False
    return True
if __name__ == "__main__":
    main()
