import random


def ask_user():
    prompt = "Rock, Paper, or Scissors? r/p/s: "
    while True:
        answer = input(prompt)
        if answer in ["r", "p", "s"]:
            break
        else:
            print("That's not an option.")
    return answer


def gen_opp():
    return random.choice(["r", "p", "s"])

def compare(answer, opp):
    if answer == opp:
        return
    elif answer == 'r':
        return opp == 's'
    elif answer == 'p':
        return opp == 'r'
    else:
        return opp == 'p'


def again():
    ans = input("Do you want to play again? (y/n): ")
    if ans == 'y':
        main()


def tell_user(answer, opp):
    print(f'You played {answer}')
    print(f'The computer played {opp}')


def main():
    answer = ask_user()
    opp = gen_opp()
    tell_user(answer, opp)
    winner = compare(answer, opp)
    if winner is None:
        print('draw')
    elif winner:
        print('win')
    else:
        print("lose")
    again()


if __name__ == "__main__":
    main()