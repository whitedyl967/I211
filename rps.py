from random import choice


def get_computer_choice() -> str:
    return choice(["rock", "paper", "scissors"])

def standardize_rps_choice(raw: str) -> str:
    standardized = raw.strip().lower()

    if standardized not in ["rock", "paper", "scissors"]:
        return ""

    return standardized


def get_human_choice() -> str:
    while True:
        human = input("(rock/paper/scissors) >> ")

        if standardize_rps_choice(human):
            return standardize_rps_choice(human)

        print(f"Unknown: '{human}', try again.")


def beats(human: str, computer: str) -> bool:
    return (
        (human == "rock" and computer == "scissors")
        or (human == "paper" and computer == "rock")
        or (human == "scissors" and computer == "paper")
    )


def decide_winner(human: str, computer: str) -> str:
    if human == computer:
        return "tie"
    elif beats(human, computer):
        return "human"
    else:
        return "computer"

def main() -> None:
    human = get_human_choice()
    computer = get_computer_choice()

    print(f"    Computer chose: '{computer}'")

    winner = decide_winner(human, computer)

    if winner == "tie":
        print("It's a tie.")
    else:
        print(f"Winner: {winner}")

if __name__ == "__main__":
    main()
