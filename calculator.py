import logging

def calculate(typy_of_operation, first_number, second_number):
    if typy_of_operation == 1:
        result = first_number + second_number
        logging.info(f"Dodaje {first_number} i {second_number} ")
    elif typy_of_operation == 2:
        result = first_number - second_number
        logging.info(f"Odejmuje {first_number} i {second_number} ")

    elif typy_of_operation == 3:
        result = first_number * second_number
        logging.info(f"Mnoze {first_number} i {second_number} ")

    elif typy_of_operation == 4:
        result = first_number / second_number
        logging.info(f"Dziele {first_number} i {second_number} ")
    print("Wynik to %s" %str(result))
    return result

def getNumberFromUser():
    while 1:
        try:
            x = int(input("Proszę wprowadzić liczbę: "))
            break
        except ValueError: 
            print("Nie podales liczby! Spróbuj jeszcze raz...")
    return x


if __name__ == "__main__":   
    typy_of_operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:   "))
    first_number = getNumberFromUser()
    second_number = getNumberFromUser()

    first_calculation = int(calculate(typy_of_operation, first_number, second_number))
    if (typy_of_operation == 1 or typy_of_operation == 3):
        result=first_calculation
        while True:
            YesOrNo = input("Czy chcesz kontynuować wykonywania tego działaniez poprzez podawanie kolejnych liczb ?  ")
            if(YesOrNo == 'Y'):
                otherNumber = getNumberFromUser()
                result = calculate(typy_of_operation, result, otherNumber)
            else:
                break