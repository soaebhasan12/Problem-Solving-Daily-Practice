# Print Linearly from N to 1 Using Backtrack

def nToOneBacktrack(i, n):
  if i < 1:
    return
  
  print(i)
  nToOneBacktrack(i - 1, n)
  
  # nToOneBacktrack(i - 1, n)
  # print(i)                        # This pair print from 1 to N
  
n = int(input("Enter the Value: "))
nToOneBacktrack(n, n)