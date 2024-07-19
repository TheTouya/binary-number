
def turn_to_ten(number, base):
    count = 0
    sum = 0
    main_list = []
    for x in number:
        main_list.append(int(x))
    if any(number >= base for number in main_list) :
        print("This number has a dgit which is bigger than the base.")
    else:
     for x in reversed(main_list):
         times = base ** count
         sum += times * x
         count += 1
     print(sum)
number = str(input("please enter the number : "))
base = int(input("enter the base : "))
turn_to_ten(number,base)
