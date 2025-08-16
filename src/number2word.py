from constants import UNDER20, TENS, ABOVE100


def number_to_words(num):
    try:
        if num < 0 :
            print("Negative numbers are not supported.")
        if num == 0:
            return UNDER20[0]
        if num < 20:
            return UNDER20[num]
        if num < 100:
            return TENS[num // 10] + ('' if num % 10 == 0 else ' ' + UNDER20[num % 10])
        if num < 1000:
            return UNDER20[num // 100] + ' ' + ABOVE100[1] + ('' if num % 100 == 0 else ' and ' + number_to_words(num % 100))
        return "Number too large to convert"

    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
    except Exception:
        print(f"An error occurred")


if __name__ == "__main__":
    while True:
        try:
            print("-"*20)
            print("| Welcome to the Number to Words Converter!")
            print("| Type 'exit' to quit the program.")
            print("-"*5)
            user_input = input("Number: ")
            if user_input.lower() == 'exit':
                break
            number = int(user_input)
            if number < 0:
                print("Negative numbers are not supported.")
            else:
                print(f"Output: {number_to_words(number)}")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
