# Print 1 to N using Recursion

def oneToN(i, n):
  if i > n:
    return
  print(i, end=" ")
  oneToN(i+1, n)
  
n = int(input("Enter Value: "))

oneToN(1, n)