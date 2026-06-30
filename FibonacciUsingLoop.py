n = int(input("Enter the Number: "))
a = 0
b = 1
print("Fabonacci Series")
for i in range(n):
  
  print(i, end=" ")
  c = a + b
  a = b
  b = c

Output: 
Enter the Number: 10
Fabonacci Series
0 1 2 3 4 5 6 7 8 9 
