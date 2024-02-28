import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_liste =  figlet.getFonts()
text = figlet

if len(sys.argv) == 1:
    text = input("Input: ")
    chosen_font = random.choice(font_liste)
    figlet.setFont(font=chosen_font)
    text = figlet.renderText(text)
elif len(sys.argv) == 3:
    if sys.argv[1] in ("-f" , "--font"):
        if sys.argv[2] not in font_liste:
            print(f"Invalid font: {sys.argv[2]}")
            sys.exit("Invalid usage")
        else:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            text = figlet.renderText(text)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

print("Output: \n"+text)
sys.exit()

