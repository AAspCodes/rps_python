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


def main():
    answer = ask_user()
    opp = gen_opp()


if __name__ == "__main__":
    main()
