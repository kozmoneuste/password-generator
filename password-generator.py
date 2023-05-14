# GitHub : kozmoneuste
import random
from pyperclip import copy
import colorama
from colorama import Back, Fore, Style
import string
colorama.init()
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
number = string.digits
symbol = "!'%?*$"
print(Fore.LIGHTCYAN_EX + """
  _____                                    _     
 |  __ \                                  | |    
 | |__) |_ _ ___ _____      _____  _ __ __| |    
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |    
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |    
 |_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|    
  / ____|                         | |            
 | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  
                    by kozmoneuste
""")
length = int(input("Password Length: "))

# Generate Password

password = lower_case + upper_case + number + symbol
password2 = "".join(random.sample(password, length))

while True:
    print(f"""
    =======================
    >>>> {password2} <<<<
    =======================
    """)
    loop = int(input("[1] Quit\n[2] Copy "))
    if loop == 1:
        break
    elif loop == 2:
        copy(password2)
        print(Fore.LIGHTRED_EX + "Copied!")
        break
