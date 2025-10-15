
def get_cats_info(path:str)-> list :
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.rstrip().split(',')
                if len(parts) == 3:
                    cat_info = {
                        "id": parts[0],
                        "name":parts[1],
                        "age":parts[2]
                    }
                    cats_list.append(cat_info)

    except FileNotFoundError:
        print(f"Error .File with path: '{path}' not found")
        return []
    return cats_list







def main():
    cats_info = get_cats_info("task2/cats_info.txt")
    print(cats_info)


if __name__ == '__main__':
    main() 