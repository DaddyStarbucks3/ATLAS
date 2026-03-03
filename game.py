# game.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any
import random


@dataclass
class AnswerRecord:
    email_id: int
    subject: str
    user_answer: bool
    correct_answer: bool
    correct: bool
    indicators: List[str]
    explanation: str


class GonePhishinGame:
    def __init__(self, emails: List[Dict[str, Any]], num_questions: int = 10, seed: int | None = None):
        if not emails:
            raise ValueError("Email list is empty.")
        if num_questions <= 0:
            raise ValueError("num_questions must be > 0")

        self._rng = random.Random(seed)
        self.emails = emails
        self.num_questions = min(num_questions, len(emails))
        self.score = 0
        self.records: List[AnswerRecord] = []

    def pick_questions(self) -> List[Dict[str, Any]]:
        return self._rng.sample(self.emails, k=self.num_questions)

    @staticmethod
    def _normalize_choice(s: str) -> str:
        return s.strip().lower()

    @staticmethod
    def parse_user_choice(raw: str) -> bool | None:
        """
        Return True for phishing, False for legit, None if invalid.
        Accepts: p/phish/phishing, l/legit, y/n (y=phish)
        """
        s = GonePhishinGame._normalize_choice(raw)
        if s in {"p", "phish", "phishing", "y", "yes"}:
            return True
        if s in {"l", "legit", "n", "no"}:
            return False
        return None

    def grade(self, email: Dict[str, Any], user_answer: bool) -> AnswerRecord:
        correct_answer = bool(email["is_phish"])
        correct = (user_answer == correct_answer)
        if correct:
            self.score += 1

        record = AnswerRecord(
            email_id=int(email["id"]),
            subject=str(email["subject"]),
            user_answer=user_answer,
            correct_answer=correct_answer,
            correct=correct,
            indicators=list(email.get("indicators", [])),
            explanation=str(email.get("explanation", "")),
        )
        self.records.append(record)
        return record
