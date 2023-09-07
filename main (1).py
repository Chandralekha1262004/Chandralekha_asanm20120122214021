#1.1 Implement a recursive function to calculate the factorial of a given number. 
def fact_rec(n):
  if n ==0 Or n==￼1:
    return 1
   else :
       return n*fact_rec(n-1)


number = int(input("Enter the value:"))
result =  fact_rec(number)