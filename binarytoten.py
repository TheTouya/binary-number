
def turn_to_ten(number, base):
    count = 0
    sum = 0
    main_list = []
    for x in number:
        main_list.append(int(x))
    for x in reversed(main_list):
        times = base ** count
        sum += times * x
        count += 1
    return sum
number = str(input("please enter the number : "))
base = int(input("enter the base : "))
final = turn_to_ten(number,base)
print(final)