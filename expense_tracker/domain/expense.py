from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Optional
from uuid import uuid4


@dataclass
class Expense:
    amount_cents: int
    currency: str
    date: str
    category: str
    merchant: str
    note: Optional[str] = None
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def __post_init__(self) -> None:
        if self.amount_cents <= 0:
            raise ValueError("amount_cents must be positive")

        if not self.category or not self.category.strip():
            raise ValueError("category cannot be empty")

        try:
            date.fromisoformat(self.date)
        except ValueError as exc:
            raise ValueError("date must be a valid ISO format string") from exc