   # example/array.py

   N_MAX = 15

   def read_array():
       """Функция для ввода массива"""
       arr = []
       try:
           n = int(input("Enter number of elements (max {}): ".format(N_MAX)))
           
           if n > N_MAX:
               print("Error: number of elements cannot exceed", N_MAX)
               return [], 0
           
           if n < 0:
               print("Error: number of elements cannot be negative")
               return [], 0
           
           print("Enter elements:")
           sum = 0
           for i in range(n):
               tmp = int(input())
               sum += tmp
               arr.append(tmp)
               
           print(f"Sum of elements: {sum}")
           print(f"Average: {sum/n if n > 0 else 0}")
           
       except ValueError:
           print("Error: Please enter valid numbers")
           return [], 0

       return arr, n

   def print_array(arr, n):
       """Функция для вывода массива"""
       print("Array elements:", end=" ")
       for i in range(n):
           print(arr[i], end=" ")
       print("\nArray size:", n)

   def main():
       # Ввод массива
       arr, n = read_array()
       # Вывод массива
       print_array(arr, n)

   if __name__ == "__main__":
       main()
       #конец 
       print()