
def total_salary(path:str) -> tuple:

    total_salary = 0
    total_developers = 0
    average_salary = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                total_developers +=1
                split_file = line.rstrip().split(",")
                if len(split_file) == 2 :
                        try:
                            total_salary += int(split_file[1])
                        except ValueError:
                            print(f"Data error'{split_file[1]}'")
                else:
                        print('Problem with data format ')
        if total_developers > 0:
                average_salary = total_salary / total_developers
        return total_salary,average_salary           
    except FileNotFoundError:
        print(f"Error .File with path: '{path}' not found")
        return (0, 0)
    except Exception as e:
        print(f"Oops ,unexpected error just happened {e}")
        return (0, 0)
    

def main():
    total, average = total_salary('task1/salary.txt') 
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == '__main__':
    main() 
