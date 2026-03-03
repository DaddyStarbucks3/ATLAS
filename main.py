# main.py
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
        raw = input("Phishing or Legit? [p/l] (or 'q' to quit): ").strip()
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
    print("\n" + "#" * 70)
    print(f"Final Score: {game.score}/{total} ({(game.score/total*100):.1f}%)")
    print("#" * 70)

    # Review missed items
    missed = [r for r in game.records if not r.correct]
    if missed:
        print("\nReview (missed questions):")
        for r in missed:
            ua = "PHISHING" if r.user_answer else "LEGIT"
            ca = "PHISHING" if r.correct_answer else "LEGIT"
            print(f"- [{r.email_id}] {r.subject} | You: {ua} | Correct: {ca}")
    else:
        print("\nPerfect run. The phish fear you now. 🐟🎣")


def main() -> None:
    print("GONE PHISHIN' — Terminal Edition")
    print("Classify each email as phishing or legit.")
    print("Tip: look for urgency, weird domains, and credential grabs.\n")

    # 20 available; ask 10 by default (change if you want)
    game = GonePhishinGame(EMAILS, num_questions=10)

    try:
        for idx, email in enumerate(game.pick_questions(), start=1):
            print(f"\nQuestion {idx}/{game.num_questions}")
            print_email(email)
            user_answer = prompt_choice()
            record = game.grade(email, user_answer)
            show_feedback(record)

        show_summary(game)

    except KeyboardInterrupt:
        print("\n\nExited early. No shame. Even SOC analysts take lunch. 🙂")
        show_summary(game)


if __name__ == "__main__":
    main()
