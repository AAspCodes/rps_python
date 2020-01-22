def ask_user():
    prompt = "Rock, Paper, or Sciccors? r/p/s: "
    while True:
        answer = input(prompt)
        if answer in ["r", "p", "s"]:
            break
        else:
            print("thats not an option")
    return answer
