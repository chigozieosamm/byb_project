user_number = int(input("Please insert any number "))
inputed_numbers = []
inputed_numbers.append(user_number)
while user_number != -1:
    user_number = int(input("Please insert any number "))
    inputed_numbers.append(user_number)
    if user_number == -1:
        inputed_numbers.pop(-1)
        print((sum(inputed_numbers))/len(inputed_numbers))
        break

    # CO24010013890 Chigozie Osammor