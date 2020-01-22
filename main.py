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
    if answer == 'r':
        if opp == 'r':
            return 'draw'
        if opp == 'p':
            return 'lose'
        if opp == 's':
            return 'win'
    if answer == 'p':
        if opp == 'r':
            return 'win'
        if opp == 'p':
            return 'draw'
        if opp == 's':
            return 'lose'
    if answer == 's':
        if opp == 'r':
            return 'lose'
        if opp == 'p':
            return 'win'
        if opp == 's':
            return 'draw'

def again():
    ans = input("Do you want to play again? (y/n): ")
    if ans == 'y':
        main()

def main():
    answer = ask_user()
    opp = gen_opp()
    winner = compare(answer, opp)
    if winner == 'draw':
        print("draw")
        again()
    if winner == 'win':
        print("You win!")
        again()
    if winner == 'lose':
        print("You lose.")
        again()

if __name__ == "__main__":
    main()