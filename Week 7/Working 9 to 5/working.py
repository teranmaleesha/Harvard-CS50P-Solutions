import re
import sys
def main():
    print(convert(input("Hours: ")))
def convert(s):
    # Regex pattern: HH:MM AM/PM to HH:MM AM/PM
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)\s+to\s+([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)$"
    match = re.search(pattern, s.strip())
    if not match:
        raise ValueError("Invalid format")
    h1, m1, p1, h2, m2, p2 = match.groups()
    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"
    h1 = convert_hour(int(h1), p1)
    h2 = convert_hour(int(h2), p2)
    return f"{h1:02d}:{m1} to {h2:02d}:{m2}"
def convert_hour(hour, period):
    if period == "AM":
        return 0 if hour == 12 else hour
    else:  # PM
        return 12 if hour == 12 else hour + 12
if __name__ == "__main__":
    main()
