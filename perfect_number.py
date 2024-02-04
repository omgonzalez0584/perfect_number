def type_of_number(lista,number):
    sum = 0
    for i in lista:
        sum += i
    
    if sum == number:
        return 'Perfect Number'
    elif sum > number:
        return 'Abundant Number'
    else:
        return 'Deficient Number'
 

def divisors(number):
    divisor_list = []
    for i in range(1,number):
        if number % i == 0:
            divisor_list.append(i)
    
    result = type_of_number(divisor_list, number)

    return result


number = int(input("Enter a number: "))
result = divisors(number)
print(f'{number} is a {result}')



