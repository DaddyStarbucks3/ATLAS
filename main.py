from data import EMAILS
from game import GonePhishinGame


def print_email(email: dict) -> None:
    print("\n" + "=" * 70)
    print(f"Subject : {email['subject']}")
    print(f"From    : {email['from_name']} <{email['from_email']}>")
    print(f"To      : {email['to']}")
    print("-" * 70)
    print(email["body"])
    print("=" * 70)


def prompt_choice() -> bool:
    while True:
        raw = input("Phishing or Legit? [p/l] (or 'q' to quit game): ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            raise KeyboardInterrupt
        parsed = GonePhishinGame.parse_user_choice(raw)
        if parsed is None:
            print("Invalid input. Type 'p' for phishing or 'l' for legit.")
            continue
        return parsed


def show_feedback(record) -> None:
    print("\nResult:", "✅ Correct" if record.correct else "❌ Incorrect")
    print(f"Answer: {'PHISHING' if record.correct_answer else 'LEGIT'}")

    if record.indicators:
        print("\nKey indicators:")
        for i, ind in enumerate(record.indicators, start=1):
            print(f"  {i}. {ind}")

    if record.explanation:
        print("\nWhy:")
        print(f"  {record.explanation}")


def show_summary(game: GonePhishinGame) -> None:
    total = len(game.records)
    if total == 0:
        print("\nNo questions were answered.")
        return

    print("\n" + "#" * 70)
    print(f"Final Score: {game.score}/{total} ({(game.score / total * 100):.1f}%)")
    print("#" * 70)

    missed = [r for r in game.records if not r.correct]
    if missed:
        print("\nReview (missed questions):")
        for r in missed:
            ua = "PHISHING" if r.user_answer else "LEGIT"
            ca = "PHISHING" if r.correct_answer else "LEGIT"
            print(f"- [{r.email_id}] {r.subject} | You: {ua} | Correct: {ca}")
    else:
        print("\nPerfect run. The phish fear you now. 🐟🎣")


def show_instructions() -> None:
    print("\nINSTRUCTIONS")
    print("-" * 70)
    print("1. Choose 'Start Game' from the menu.")
    print("2. Read each email carefully.")
    print("3. Type 'p' if you think the email is phishing.")
    print("4. Type 'l' if you think the email is legitimate.")
    print("5. The game will score your answers and show feedback.")
    print("6. Type 'q' during the game if you want to quit early.")


def play_game() -> None:
    print("\nStarting Gone Phishin'...")
    print("Classify each email as phishing or legit.")
    print("Tip: look for urgency, weird domains, and credential grabs.\n")

    game = GonePhishinGame(EMAILS, num_questions=10)

    try:
        for idx, email in enumerate(game.pick_questions(), start=1):
            print(f"\nQuestion {idx}/{game.num_questions}")
            print_email(email)
            user_answer = prompt_choice()
            record = game.grade(email, user_answer)
            show_feedback(record)

        print("\nGame complete.")
        show_summary(game)

    except KeyboardInterrupt:
        print("\n\nYou exited the game early.")
        show_summary(game)


def main_menu() -> str:
    print("\n" + "=" * 70)
    print("GONE PHISHIN' — MAIN MENU")
    print("=" * 70)
    print("1. Start Game")
    print("2. View Instructions")
    print("3. Exit")
    return input("Enter your choice (1-3): ").strip()


def main() -> None:
    while True:
        choice = main_menu()

        if choice == "1":
            play_game()
            print("\nReturning to main menu...")

        elif choice == "2":
            show_instructions()
            print("\nReturning to main menu...")

        elif choice == "3":
            print("\nThanks for playing Gone Phishin'. Goodbye.")
            break

        else:
            print("\nInvalid menu choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
