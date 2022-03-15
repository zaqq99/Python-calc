choice = '0'


def addition():
    # print(choice)
    if choice == '1':
        print("Addition")
        numbers = float(input("Enter the numbers: "))
        length = 0
        answers = 0
        while numbers != 0:
            answers = answers + numbers
            length += 1
            numbers = float(input("Enter another number (0 to calculate): "))
        return [answers, length]
    else:
        print("Dodawanie")
        numbers = float(input("Wprowadź liczby: "))
        length = 0
        answers = 0
        while numbers != 0:
            answers = answers + numbers
            length += 1
            numbers = float(
                input("Wprowadź kolejne liczby (Naciśnij 0 aby zakończyć): "))
        return [answers, length]


def substraction():
    if choice == '1':
        print("Substraction")
        numbers = float(input("Enter the numbers: "))
        length = 0
        answers = 0
        while numbers != 0:
            answers = numbers - answers
            length += 1
            numbers = float(input("Enter another number (0 to calculate): "))
        return [answers, length]
    else:
        print("Odejmowanie")
        numbers = float(input("Wprowadź liczby: "))
        length = 0
        answers = 0
        while numbers != 0:
            answers = numbers - answers
            length += 1
            numbers = float(
                input("Wprowadź kolejne liczby (Naciśnij 0 aby zakończyć): "))
        return [answers, length]


def multiplication():
    if choice == '1':
        print("Multiplication")
        numbers = float(input("Enter the numbers: "))
        length = 0
        answers = 1
        while numbers != 0:
            answers = numbers * answers
            length += 1
            numbers = float(input("Enter another number (0 to calculate): "))
        return [answers, length]
    else:
        print("Mnożenie")
        numbers = float(input("Wprowadź liczby: "))
        length = 0
        answers = 1
        while numbers != 0:
            answers = numbers * answers
            length += 1
            numbers = float(
                input("Wprowadź kolejne liczby (Naciśnij 0 aby zakończyć): "))
        return [answers, length]


def division():
    if choice == '1':
        print("Division")
        numbers = float(input("Enter the numbers: "))
        length = 0
        answers = 1
        while numbers != 0:
            answers = numbers / answers
            length += 1
            numbers = float(input("Enter another number (0 to calculate): "))
        return [answers, length]
    else:
        print("Dzielenie")
        numbers = float(input("Wprowadź liczby: "))
        length = 0
        answers = 1
        while numbers != 0:
            answers = numbers / answers
            length += 1
            numbers = float(
                input("Wprowadź kolejne liczby (Naciśnij 0 aby zakończyć): "))
        return [answers, length]


def average():
    if choice == '1':
        print("Average")
        numbers = float(input("Enter the numbers: "))
        length = 0
        answers = 0
        while numbers != 0:
            answers = numbers + answers
            length += 1
            numbers = float(input("Enter another number (0 to calculate): "))
        return [answers/length, length]
    else:
        print("Średnia")
        numbers = float(input("Wprowadź liczby: "))
        length = 0
        answers = 0
        while numbers != 0:
            answers = numbers + answers
            length += 1
            numbers = float(
                input("Wprowadź kolejne liczby (Naciśnij 0 aby zakończyć): "))
        return [answers/length, length]


def calc():
    print("Hello, I'm zaqq. This is my calculator in Python.")
    print(
        "Choose what you want to do.\nPress [1] for addition.\nPress [2] for substraction.\nPress [3] for multiplication.\nPress [4] for division.\nPress [5] for average.\nPress [6] for quit.")
    char = input()
    list = []
    while True:
        if char == '1':
            print(choice)
            list = addition()
            print('Answers = ', list[0], ' total inputs: ', list[1])
            calc()
        elif char == '2':
            list = substraction()
            print('Answers = ', list[0], ' total inputs: ', list[1])
            calc()
        elif char == '3':
            list = multiplication()
            print('Answers = ', list[0], ' total inputs: ', list[1])
            calc()
        elif char == '4':
            list = division()
            print('Answers = ', list[0], ' total inputs: ', list[1])
            calc()
        elif char == '5':
            list = average()
            print('Answers = ', list[0], ' total inputs: ', list[1])
            calc()
        elif char == '6':
            print("Bye! I'll miss you!")
            exit()
        else:
            print('Invalid character!')
            exit()


def calcP():
    print("Cześć, Jestem zaqq. Oto mój kalkulator napisany w Pythonie.")
    print(
        "Wybierz co chcesz zrobić.\nNaciśnij [1] - Dodawanie.\nNaciśnij [2] - Odejmowanie.\nNaciśnij [3] - Mnożenie.\nNaciśnij [4] - Dzielenie.\nNaciśnij [5] - Średnia.\nNaciśnij [6] - Wyjście.")
    char = input()
    list = []
    while True:
        if char == '1':
            list = addition()
            print('Odpowiedź = ', list[0], ' Ilość operacji: ', list[1])
            calcP()
        elif char == '2':
            list = substraction()
            print('Odpowiedź = ', list[0], ' Ilość operacji: ', list[1])
            calcP()
        elif char == '3':
            list = multiplication()
            print('Odpowiedź = ', list[0], ' Ilość operacji: ', list[1])
            calcP()
        elif char == '4':
            list = division()
            print('Odpowiedź = ', list[0], ' Ilość operacji ', list[1])
            calcP()
        elif char == '5':
            list = average()
            print('Odpowiedź = ', list[0], ' Ilość operacji ', list[1])
            calcP()
        elif char == '6':
            print("Żegnaj! Będę tęsknić!")
            exit()
        else:
            print('Błędny znak!')
            exit()


def Choice():
    print("Press 1 to continue in English. \nNaciśnij 2 aby kontynuować po polsku.")
    global choice
    choice = input()
    while True:
        if choice == '1':
            calc()
        elif choice == '2':
            calcP()
        else:
            print("Wrong input. \nWprowadziłeś zły znak.")
            choice = input()


Choice()
