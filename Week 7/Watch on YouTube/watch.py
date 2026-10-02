import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):
    pattern = r'<iframe\s+[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"'
    matches = re.search(pattern, s, re.IGNORECASE)
    if matches:
        return f"http://youtu.be/{matches.group(1)}"
    return None
if __name__ == "__main__":
    main()
