import pytest

from expense_tracker.domain.expense import Expense


def test_creates_valid_expense():
    expense = Expense(
        amount_cents=1200,
        currency="USD",
        date="2026-03-10",
        category="food",
        merchant="Chipotle",
        note="Lunch",
    )

    assert expense.amount_cents == 1200
    assert expense.currency == "USD"
    assert expense.date == "2026-03-10"
    assert expense.category == "food"
    assert expense.merchant == "Chipotle"
    assert expense.note == "Lunch"
    assert expense.id is not None
    assert expense.created_at is not None


def test_rejects_non_positive_amount():
    with pytest.raises(ValueError, match="amount_cents must be positive"):
        Expense(
            amount_cents=0,
            currency="USD",
            date="2026-03-10",
            category="food",
            merchant="Chipotle",
        )


def test_rejects_empty_category():
    with pytest.raises(ValueError, match="category cannot be empty"):
        Expense(
            amount_cents=1200,
            currency="USD",
            date="2026-03-10",
            category="",
            merchant="Chipotle",
        )


def test_rejects_invalid_date():
    with pytest.raises(ValueError, match="date must be a valid ISO format string"):
        Expense(
            amount_cents=1200,
            currency="USD",
            date="03/10/2026",
            category="food",
            merchant="Chipotle",
        )