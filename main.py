print("--------zadanie1-------------")
txt1 = "Python 2023"
txt2 = txt1
txt3 = txt2

print(txt1 == txt2)
print(txt2 == txt3)

print(type(txt1), hex(id(txt1)))
print(type(txt2), hex(id(txt2)))
print(type(txt3), hex(id(txt3)))

string3 = "Java 11"
print(txt1 == txt2)
print(txt2 == txt3)

print(type(txt1), hex(id(txt1)))
print(type(txt2), hex(id(txt2)))
print(type(txt3), hex(id(txt3)))


print()
print()
print()
print("--------zadanie2-------------")

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Select opereation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        nextCalculation= input("Let's do next calculation? (yes/no):")
        if nextCalculation == 'no':
            break

    else:
        print("Invalid Input")
print()
print()
print()
print("--------zadanie3-------------")


pytanie = input("Podaj imię i nazwisko:")
print(pytanie)


print()
print("--------------------------------------------")
print()


print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print("1.sluchanie muzyki")
print("2.czytanie ksiazek")
print("3.podrozowanie")
choice1 = input("wybierz odp")
if choice1 in ('1','2','3'):
    if choice1 == '1':
        answer1 = 'sluchanie muzyki'
    elif choice1 =='2':
        answer1 = 'czytanie ksiazek'
    elif choice1 == '3':
        answer1 = 'podrozowanie'
print(answer1)

print()
print("--------------------------------------------")
print()

print("W jakich okolicznościach czytasz książki najczęściej?")
print("1.podczas podróży")
print("2.w ogóle nie czytam")
print("3.podczas pracy/nauki (to ich element)")
choice2 = input("wybierz odp")
if choice2 in ('1','2','3'):
    if choice2 == '1':
        answer2 = 'podczas podróży'
    elif choice2 =='2':
        answer2 = 'w ogóle nie czytam'
    elif choice2 == '3':
        answer2 = 'podczas pracy/nauki (to ich element)'
    else:
        print("nie ma takiej odpowiedzi")
print(answer2)

print()
print("--------------------------------------------")
print()


print("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
print("1.chęć poszerzenia wiedzy")
print("2.fakt, że czytanie jest modne")
print("3.odczuwam presję rodziny/środowiska, żeby czytać")
choice3 = input("wybierz odp")
if choice3 in ('1','2','3'):
    if choice3 == '1':
        answer3 = 'chęć poszerzenia wiedzy'
    elif choice3 =='2':
        answer3 = 'fakt, że czytanie jest modne'
    elif choice3 == '3':
        answer3 = 'odczuwam presję rodziny/środowiska, żeby czytać'
     else:
        print("nie ma takiej odpowiedzi")
print(answer3)

print()
print("--------------------------------------------")
print()


print("Po książki w jakiej formie sięgasz najczęściej?")
print("1.papierowej (tradycyjnej)")
print("2.e-booki (książki elektroniczne) na komputerze")
print("3.e-booki na tablecie/telefonie")
choice4 = input("wybierz odp")
if choice4 in ('1','2','3'):
    if choice4 == '1':
        answer4 = 'papierowej (tradycyjnej)'
    elif choice4 =='2':
        answer4 = 'e-booki (książki elektroniczne) na komputerze'
    elif choice4 == '3':
        answer4 = 'e-booki na tablecie/telefonie'
    else:
        print("nie ma takiej odpowiedzi")
print(answer4)

print()
print("--------------------------------------------")
print()



print("Ile książek czytasz średnio w ciągu roku?")
print("1.0")
print("2.2 lub 3")
print("3.powyżej 10")
choice5 = input("wybierz odp")
if choice5 in ('1','2','3'):
    if choice5 == '1':
        answer5 = '0'
    elif choice5 =='2':
        answer5 = '2 lub 3'
    elif choice5 == '3':
        answer5 = 'powyżej 10'
    else:
        print("nie ma takiej odpowiedzi")
print(answer5)

print()
print("--------------------------------------------")
print()



print("Jak często średnio czytasz książki?")
print("1.codziennie")
print("2.raz na kilka miesięcy")
print("3.wcale")
choice6 = input("wybierz odp")
if choice6 in ('1','2','3'):
    if choice6 == '1':
        answer6 = 'codziennie'
    elif choice6 =='2':
        answer6 = 'raz na kilka miesięcy'
    elif choice6 == '3':
        answer6 = 'wcale'
    else:
        print("nie ma takiej odpowiedzi")
print(answer6)

print()
print("--------------------------------------------")
print()


print("o jakie gatunki książek sięgasz najczęściej? ")
print("1.kryminały/thrillery")
print("2.naukowe")
print("3.historyczne")
choice7 = input("wybierz odp")
if choice7 in ('1','2','3'):
    if choice7 == '1':
        answer7 = 'kryminały/thrillery'
    elif choice7 =='2':
        answer7 = 'naukowe'
    elif choice7 == '3':
        answer7 = 'historyczne'
    else:
        print("nie ma takiej odpowiedzi")
print(answer7)




