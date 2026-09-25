import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
available_fonts = figlet.getFonts()
if len(sys.argv) == 1:
    font_name = random.choice(available_fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f","--font"] and sys.argv[2] in available_fonts:
        font_name = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
figlet.setFont(font = font_name)
text = input("Input: ")
print(figlet.renderText(text))

