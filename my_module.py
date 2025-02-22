import random

def calculator():
    def num_check(prompt):
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Enter valid number")
            return num_check(prompt)

    num1 = num_check("Add a number:\n")
    num2 = num_check("Add a second number:\n")
    operations = input("Choose an operation (Addition: +, subtraction: -, multiplication: *, division: / ):\n")
    if operations == "addition" or operations == "+":
        print(num1 + num2)
    elif operations == "subtraction" or operations == "-":
        print( num1 - num2)
    elif operations == "multiplication" or operations == "*":
        print (num1 * num2)
    elif operations == "division" or operations == "/":
        print( num1 / num2)
    else:
        print (f"Error, this is no operation.:\n"
                f"Addition =          {num1 + num2}:\n"
                f"Subtraction =       {num1 - num2}:\n"
                f"Multiplication =    {num1 * num2}:\n"
                f"Division =          {num1 / num2}")

def check(prompt, different_check):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num <= 90 and num not in different_check:
                return num
            else:
                print("You have match, please try another number 1-90")
        else:
            print("Error, please enter Valid Number to 1 - 90")


def lotto():
    different_check = set()
    user_num1 = check("Please choose numbers 1-90. First:\n", different_check)
    different_check.add(user_num1)
    user_num2 = check("Please choose numbers 1-90. Second:\n", different_check)
    different_check.add(user_num2)
    user_num3 = check("Please choose numbers 1-90. Third:\n", different_check)
    different_check.add(user_num3)
    user_num4 = check("Please choose numbers 1-90. Fourth:\n", different_check)
    different_check.add(user_num4)
    user_num5 = check("Please choose numbers 1-90. Fifth:\n", different_check)
    different_check.add(user_num5)

    print(f"Your number is = {user_num1},{user_num2},{user_num3},{user_num4},{user_num5}")
    numbers = {user_num1, user_num2, user_num3, user_num4, user_num5}
    win_num = set(random.sample(range(1, 91), 5))
    print(f"The winner numbers is: {win_num}")
    nums_match = numbers.intersection(win_num)
    match_number = len(nums_match)

    if numbers == win_num:
        print("You WIN!!!")
    elif match_number == 4:
        print(f"Amazing. You have 4 match: {match_number}")
    elif match_number == 3:
        print(f"Oh...just a little..Try now!. You have 3 match: {match_number}")
    elif match_number == 2:
        print(f"Hmm...maybe next time. You have 2 match: {match_number}")
    elif match_number == 1:
        print(f"It is bad luck. You have 1 match: {match_number}")

    else:
        print("you lose! Try again!")

    return numbers


def shopping():
    my_list = []
    while True:
        items = input("Add your items to your list or:\n "
                      "To print please press : p \n "
                      "To delete items press: D:\n"
                      "To exit press: exit:\n").lower()

        if items == "exit":
            return f"Your list is: {my_list}"
        elif items == "P".lower():
            print(my_list)
        elif items == "D".lower():
            delete = my_list.remove(input(f"Which items delete?:\n Your list is: {my_list}"))
            if delete not in my_list:
                print(f"Please select valid items from your list: {my_list}")
                print(items)
            else:
                print(delete)
        else:
            my_list.append(items)


def games():
    scoore = 0
    scoore_pc = 0
    def game():
        nonlocal scoore, scoore_pc  # Azon változók, amelyeket módosítani akarunk
        valaszt = [1, 2, 3]  # Csak számok legyenek a választásban
        valaszt_nevek = {1: "kő", 2: "papír", 3: "olló"}  # Szóképek a választásokhoz
        gep_v = random.choice(valaszt)

        jatekos_v = input("Kő =(1) , papír =(2) , vagy olló =(3)? \n"
                      "Válassz egy számot! \nKilépéshez írd: >>> exit<<<:\n").lower()

        if jatekos_v == "exit":
            print("Találkozunk később!")
            return False
        try:
            jatekos_v = int(jatekos_v)
            if jatekos_v not in ["1", "2", "3"]:
                print("Érvénytelen választás: Kő = 1, papír = 2, olló = 3")
                return True
        except ValueError:
            print("Kérlek egy érvényes számot adj meg (1, 2, 3).")
            return True

    
        print("A te választásod: ", valaszt_nevek[int(jatekos_v)])  # A választás szöveges formája
        print("A gép választása: ", valaszt_nevek[gep_v])  # A gép választásának szöveges formája

        if gep_v == int(jatekos_v):
            print("döntetlen")
        
        elif jatekos_v == 1 and gep_v == 3 or \
                jatekos_v == 3 and gep_v == 2 or \
                jatekos_v == 2 and gep_v == 1:
            scoore += 1
            print(f"Nyertél, a pontod: {scoore} a gép: {scoore_pc}")

        else:
            scoore_pc += 1
            print(f"Vesztettél a pontod: {scoore} a gép: {scoore_pc}")
        
        return True


    def new():
        newgame = input("Játszunk mégegyet? válassz: i/n\n").lower()
        if newgame == "i":
                return True
        elif newgame == "n":
            print(f"Később találkozunk! pontok: {scoore} a gép: {scoore_pc}")
            return False
        else:
            print("Kérlek válassz helyesen: i = igen, n = nem")

    while True:
        if not game():  # Ha a `game()` False-t ad vissza, kilépünk
            break
        if not new():  # Ha a `new()` False-t ad vissza, kilépünk
            break


def area ():
    leinght = int(input("Add leight:\n"))
    width = int(input("Add widht:\n"))
    area_result = leinght*width
    print( f"The area of the rectangle = {area_result} . ")



def vowels_detector():
    giv_sen = input("Please write your text!:\n")
    vowels = {"a", "e", "i", "o", "u"}
    detector = {}

    for v in vowels:
        if v in giv_sen:
            detector[v] = giv_sen.count(v)
    print(len(detector), detector)



usernames = {"hello","bello", "user"}

def usercheck():
    new_user = input("Choose an username: \n")
    if new_user not in usernames:
        usernames.add(new_user)
        print(f"Your username is: {new_user}")

    else:
        print("Username is taken, choose another:")


def password_valid():
    password = input("Enter a password:\n")
    if (any(k.isdigit() for k in password) and len(password) >=8 and
            any(k.isupper() for k in password) and any(k.islower() for k in password)):
          print("Registration is complete! ")
    else:
        print("password is Invalid, try again:")
        return password_valid()



def registration():
    return usercheck(),password_valid()
