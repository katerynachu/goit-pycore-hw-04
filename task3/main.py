import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

VERT_LINE = "│   " 
FORK = "├── "     
LAST_FORK = "└── " 
SPACE = "    "


def visualize_structure(path, prefix=""):
    dir_path = Path(path)
    if prefix == "":
            if not dir_path.exists():
                print(Fore.RED + f"Error: Path '{dir_path}' does not exist!")
                return
            if not dir_path.is_dir():
                print(Fore.RED + f"Error: Path '{dir_path}' is not a directory!")
                return
            

    if prefix == "":
        
        print(Fore.CYAN + f"📦 {dir_path.name}" + Style.RESET_ALL) # Line A'    




    try:

        contents = sorted(list(dir_path.iterdir()))
        count = len(contents)
        
        for i, item in enumerate(contents):
            is_last = (i == count - 1)

            connector = LAST_FORK if is_last else FORK

            if item.is_dir():

                print(prefix + connector + Fore.BLUE + f"📁 {item.name}" + Style.RESET_ALL)

                new_prefix = prefix + (SPACE if is_last else VERT_LINE)
                visualize_structure(item,new_prefix)

            if item.is_file():
                print(prefix + connector + Fore.GREEN + f"📄 {item.name}" + Style.RESET_ALL)
                
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