N_MAX = 15

def read_array():
    """Функция для ввода массива"""
    arr = []
    n = int(input("Enter number of elements (max {}): ".format(N_MAX)))
    
    if n > N_MAX:
        print("Error: number of elements cannot exceed", N_MAX)
        return [], 0
    
    print("Enter elements:")
    for i in range(n):
        tmp = int(input())
        arr.append(tmp)
    
    return arr, n

def print_array(arr, n):
    """Функция для вывода массива"""
    print("Array:", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    # Ввод массива
    arr, n = read_array()
    if n > 0:
        # Вывод массива
        print_array(arr, n)

if __name__ == "__main__":
    main() 