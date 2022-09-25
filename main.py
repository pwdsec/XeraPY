# in development, still being written

# written by Tr1ppy
# https://pastebin.com/raw/y36Qcr46

import os

import requests
import platform

logo = """
\033[91m██╗  ██╗███████╗██████╗  █████╗ \033[00m\033[93m██████╗ ██╗   ██╗\033[00m
\033[91m╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗\033[00m\033[93m██╔══██╗╚██╗ ██╔╝\033[00m
 \033[91m╚███╔╝ █████╗  ██████╔╝███████║\033[00m\033[93m██████╔╝ ╚████╔╝ \033[00m
 \033[91m██╔██╗ ██╔══╝  ██╔══██╗██╔══██║\033[00m\033[93m██╔═══╝   ╚██╔╝  \033[00m
\033[91m██╔╝ ██╗███████╗██║  ██║██║  ██║\033[00m\033[93m██║        ██║ \033[00m  
\033[91m╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝\033[00m\033[93m╚═╝        ╚═╝\033[00m
                                            1.0.0"""


def pr_red(skk): print("\033[91m {}\033[00m".format(skk))


def clear_c():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def get_key():
    link = requests.get("https://pastebin.com/raw/y36Qcr46")
    link2 = link.text.replace("/raw", "").replace("https://pst.klgrth.io/paste/", "")
    key = requests.get(link.text)
    file = open(link2 + ".txt", "w")
    file.write(key.text)
    file.close()

    return key.text


def installer():
    download_url = "https://github.com/CSharpDumbass/5AfzDBW3box7HnzvYAoi210I7/raw/main/XeraX%20Installer.exe"
    req = requests.get(download_url)
    with open("XeraX Installer.exe", "wb") as outp:
        outp.write(req.content)


def main_inst():
    while True:
        user_input = input("[\033[91mX\033[00m\033[93mPY\033[00m]: ")
        if user_input == "getkey":
            print("key: " + get_key())
        elif user_input == "help":
            print("Help:\n  getkey - Get key to log into the exploit\n  Installer - download the installer.")
        elif user_input == "installer":
            installer()
        else:
            print("invalid")


if __name__ == '__main__':
    clear_c()
    pr_red(logo)
    try:
        main_inst()
    except KeyboardInterrupt:
        clear_c()
        print("Good bye")
