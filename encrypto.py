import os
import time

class colors:
    def __init__(self,inputColor):
        self.Color = inputColor
red = colors('\033[91m')
green = colors('\033[92m')
yellow = colors('\033[93m')
cyan = colors('\033[96m')

os.system("clear")
time.sleep(0.5)
print(red.Color+"═════════════════════════════════════════════════════════════════════")
print ("\033[1;33m        \    \    \. \\\.__,-“-.__.///  ./  ./    /  ")
time.sleep(0.1)
print ("\033[1;33m         \.   \`.  \`.-'“ _,=|=._ “”`-.’/  ’/   ./  ")
time.sleep(0.1)
print ("\033[1;33m          \`.  \_`-’’ //  _,=“=._  \\  ``-_/   ./   ")
time.sleep(0.1)
print ("\033[1;33m           \`-’,\=,'\\_. \ _,=“=._//,_///_./,`-'/     ")
time.sleep(0.1)
print ("\033[1;33m            \.   \.      __,-“-.__   \033[1;31m   ./   ./       ")
time.sleep(0.1)
print ("\033[1;31m        \.  \033[1;33m \`. \ `.-'“” _,=“=._ “”`-.\033[1;31m’/  .’/   ./    ")
time.sleep(0.1)
print ("\033[1;31m         \`. \033[1;31m \_`.““      _,=“=._      ``-'\033[1;31m_/  .’/      ")
time.sleep(0.1)
print ("\033[1;31m          \ `-\033[1;31m',-._   _.  _,=“=._  ,_   _.-,`-’\033[1;31m /      ")
time.sleep(0.1)
print ("\033[1;31m       \. /`,-'\033[1;33m,-._\033[1;31m”””  \ _,=“=._ /  “””\033[1;33m_.-,\033[1;31m`-,’\ ./  ")
time.sleep(0.1)
print ("\033[1;31m        \`-' \033[1;33m /    `-._ \033[1;31m “       “ \033[1;33m _.-’    \ \033[1;31m `-’/  ")
time.sleep(0.1)
print ("\033[1;31m        /)  \033[1;33m (   \033[1;31m @ \033[1;33m   \ \033[1;31m   ,-.   \033[1;33m /   \033[1;31m @ \033[1;33m   ")
time.sleep(0.1)
print ("\033[1;31m     ,-’“    \033[1;33m `-.       \ \033[1;31m /   \ \033[1;33m /       .-'   \033[1;31m  ”`-, ")
time.sleep(0.1)
print ("\033[1;31m   ,’_._      \033[1;33m   `-.____/ \033[1;31m/  _  \ \033[1;33m\____.-'     \033[1;31m    _._`,  ")
time.sleep(0.1)
print ("\033[1;31m  /,’   `.               \033[1;31m \_/ \_/             \033[1;31m   .'   `,\   ")
time.sleep(0.1)
print ("\033[1;31m /'       )                  _                  (       `\    ")
time.sleep(0.1)
print ("\033[1;31m         /   _,-’“`-.  ,++|T|||T|++.  .-'“`-,_   \            ")
time.sleep(0.1)
print ("\033[1;31m        / ,-’        \/|`|`|`|'|’|‘|\/        `-, \          ")
time.sleep(0.1)
print ("\033[1;31m       /,'            || | | | | | ||            `,\        ")
time.sleep(0.1)
print ("\033[1;31m      /'               ` | | | | | ’               `\      ")
time.sleep(0.1)
print ("\033[1;31m    $made by sordi95506  ` | | | '                        ")
time.sleep(0.1)
print (' ')
print(red.Color+"═════════════════════════════════════════════════════════════════════")
print("")
hash_file = input(cyan.Color+"Enter the file to encrypt it: ") 
#encrept file
def encrypt_file(filename, key):
    with open(hash_file, "rb") as f:
        data = f.read()

    encrypted_data = bytearray()
    for byte in data:
        encrypted_data.append(byte ^ key)

    with open(hash_file, "wb") as f:
        f.write(encrypted_data)

key = 0x12  #v5x
filename = hash_file
encrypt_file(filename, key)
#while loop 
i = 0
word = "the file make succesfuly ▓▓▓▓▓"
while i<20:
 print(green.Color+word)
 time.sleep(0.2)
 i +=1
