def prime_checker(number):
    number_list =[2,3,4,5,6,7,8,9]
    is_prime = True
    for i in number_list:
        if(i==number):
            continue
        elif(number % i == 0):
            is_prime = False
            break        
    if(is_prime):
        print(f"Number {number} is a Prime Number")
    else:
        print(f"Number {number} is Not a Prime Number")

n = int(input("Check this number: "))
prime_checker(number=n)
