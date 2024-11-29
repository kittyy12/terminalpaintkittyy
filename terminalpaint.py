import os
os.system("sudo apt install python3-colorama")
import colorama
from colorama import Fore
from colorama import Style

banner = """
 ______              _           _____       _      __ 
/_  __/__ ______ _  (_)__  ___ _/ / _ \___ _(_)__  / /_
 / / / -_) __/  ' \/ / _ \/ _ `/ / ___/ _ `/ / _ \/ __/
/_/__\__/_/_/_/_/_/_/_//_/\_,_/_/_/   \_,_/_/_//_/\__/ 
  / //_(_) /_/ /___ __                                 
 / ,< / / __/ __/ // /                                 
/_/|_/_/\__/\__/\_, /                                  
               /___/                                   """
print(Fore.CYAN + banner)

choose = """
[1] Black
[2] Blue
[3] Cyan
[4] Green
[5] Magenta
[6] Red
[7] White
[8] Yellow
[9] RESET
"""

print(Fore.GREEN + choose)
print(Style.RESET_ALL)
aa = input("TerminalPaint ==> ")

if aa == '1':
    print("changing color to Black...")
    print(Fore.BLACK)
    
if aa == '2':
    print("changing color to Blue....")
    print(Fore.BLUE)

if aa == '3':
    print("changing color to Cyan....")
    print(Fore.CYAN)

if aa == '4':
    print("changing color to Green....")
    print(Fore.GREEN)

if aa == '5':
    print("changing color to Magenta.....")
    print(Fore.MAGENTA)

if aa == '6':
    print("changing color to Red.....")
    print(Fore.RED)

if aa == '7':
    print("changing color to White....")
    print(Fore.WHITE)

if aa == '8':
    print("changing color to Yellow.....")
    print(Fore.YELLOW)

if aa == '9':
    print(Style.RESET_ALL)



