from icecream import ic
from rich import print
from helper.calcs import minus, sum
from helper.prints import print_name, print_test

if __name__ == "__main__":
    ic(sum(num1=7,num2=10))
    ic(sum(num1=9,num2=50))
    ic(minus(num1=20, num2=4))
    ic(minus())
    ic(print_name()) 
    ic(print_test())
    print(print_name()) 
    print(print_test())