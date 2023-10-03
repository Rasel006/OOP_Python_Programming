def sum(num1, num2,num3):
    result=num1 + num2 + num3
    return result
total = sum(99,11,5) 
print('total', total)   

# args

def all_sum(num1,num2,*numbers):
    print(numbers)
    sum=0

    for num in numbers:
        print(num)
        sum = sum+num
    return sum;

total = all_sum(45,46,89,11,81)
print('all sum', total)

def do_a_lot(*args):
    print(args)
    