import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def visualize_structure(path, level = 0):
    dir_path = Path(path)
    if level == 0:
            if not dir_path.exists():
                print(Fore.RED + f"Error: Path '{dir_path}' does not exist!")
                return
            if not dir_path.is_dir():
                print(Fore.RED + f"Error: Path '{dir_path}' is not a directory!")
                return

    indent = " " * level
    print(indent + Fore.CYAN + f"📂 {dir_path.name}" + Style.RESET_ALL) 

    try:
        for item in dir_path.iterdir():

            if item.is_dir():
                #print (" " * (level + 2 ) + Fore.LIGHTBLUE_EX  + f"📁 {item.name}/")
                visualize_structure(item,level + 4)
            if item.is_file():
                print (" " * (level + 2 ) + Fore.GREEN + f"📄 {item.name}")
                
    except PermissionError:
        print(Fore.YELLOW + f"⚠️ Permission Denied to access '{dir_path.name}' contents." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"🚫 An unexpected error occurred: {e}" + Style.RESET_ALL)    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Name of directory required!")
        sys.exit(1)


file = sys.argv[1]
visualize_structure(file)        