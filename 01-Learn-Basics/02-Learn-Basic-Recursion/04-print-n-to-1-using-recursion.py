# Print N to 1 using Recursion -- Good Question

def nToOne(i, n):
  if i < 1:
    return 
  
  print(i, end=" ")
  nToOne(i - 1, n)
  # print(n, end=" ")        # Print from 1 to N
  

n = int(input("Enter the value: "))
nToOne(n, n)