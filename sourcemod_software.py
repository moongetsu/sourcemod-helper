import colorama
import os
import shutil
import platform
from colorama import Fore, Style

colorama.init(autoreset=True)

print(Fore.RED + """
███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗███╗   ███╗ ██████╗ ██████╗     ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝████╗ ████║██╔═══██╗██╔══██╗    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  ██╔████╔██║██║   ██║██║  ██║    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  ██║╚██╔╝██║██║   ██║██║  ██║    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗██║ ╚═╝ ██║╚██████╔╝██████╔╝    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
""" + Style.RESET_ALL)

print("Salut, te rog sa selectezi optiunea pe care o doresti:")
print("1. Compileaza un plugin.")

user_choice = input("Introdu un numar: ")

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def choose_version():
    version = input("Cu ce versiune de sourcemod doresti sa compilezi plugin-ul?\n1. 1.11\n2. 1.10\n3. 1.9\n")
    clear_console()
    if version == "1":
        version_dir = "1.11"
    elif version == "2":
        version_dir = "1.10"
    elif version == "3":
        version_dir = "1.9"
    else:
        print("Numar invalid. Te rog sa alegi un numar corect.")
        return choose_version()
    return version_dir

def compile_sp_file(version_dir, sp_file_path):
    os.chdir(f"sourcemod compiler/{version_dir}")
    os.system(f"spcomp.exe {sp_file_path}")
    smx_file_name = os.path.basename(sp_file_path).split(".")[0] + ".smx"
    smx_file_path = os.path.join(os.getcwd(), "compiled", smx_file_name)
    os.chdir("../..")
    return smx_file_path

def main():
    version_dir = choose_version()

    sp_file_name = input("Te rog sa introduci numele plugin-ului (fara .sp la final): ")
    sp_file_path = os.path.join(os.getcwd(), sp_file_name + ".sp")
    while not os.path.isfile(sp_file_path):
        sp_file_name = input("Numele nu este valid. Te rog sa introduci numele plugin-ului (fara .sp la final): ")
        sp_file_path = os.path.join(os.getcwd(), sp_file_name + ".sp")

    smx_file_path = compile_sp_file(version_dir, sp_file_path)

    smx_file_name = os.path.basename(smx_file_path).split(".")[0] + ".smx"
    shutil.copy2(smx_file_path, smx_file_name)
    print(f"{smx_file_name} a fost compilat cu succes!")

if __name__ == "__main__":
    main()