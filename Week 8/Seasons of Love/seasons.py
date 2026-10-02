from datetime import date
import sys
import inflect
p = inflect.engine()
def main():
    birth_date_str = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    diff = today - birth_date
    minutes = diff.days * 1440
    words = p.number_to_words(minutes, wantlist=False)
    words = words.replace(" and", "")
    print(f"{words.capitalize()} minutes")
if __name__ == "__main__":
    main()
