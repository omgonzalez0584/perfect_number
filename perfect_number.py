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

print("Determine if a number is perfect, abundant, or deficient")
while True:
    try:
        number = (input("Enter a number - (X for exit): "))
        if number.lower() == 'x':
            print("Good bye!")
            break
        else:
            result = divisors(int(number))
            print(f'{number} is a {result}')
    except Exception as e:
        print('Error , debe ingresar un numero!')


        



