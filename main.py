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
    converter = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    print(f'You played {converter[answer]}')
    print(f'The computer played {converter[opp]}')


def main():
    answer = ask_user()
    opp = gen_opp()
    tell_user(answer, opp)
    winner = compare(answer, opp)
    if winner is None:
        print("It's a draw!")
    elif winner:
        print('You win!')
    else:
        print("You lose.")
    again()


if __name__ == "__main__":
    main()
