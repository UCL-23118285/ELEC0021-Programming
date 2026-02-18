"""Utilities for working with a tiny purchase leaderboard.

This module defines a Purchase class that computes the total spend per user for a given
country and prints a ranked list of the top spenders.

Examples:
    >>> purchases = parse_purchases(["alice,UK,10.0", "bob,UK,5.0"])
    >>> totals = total_spend_by_user(purchases, "UK")
    >>> top_users(totals, limit=1)
    [('alice', 10.0)]
"""


class Purchase:
    """Represents a single purchase made by a user in a given country.

    Stores the user name, country, and spend amount. Supports country filtering
    and fee application, and exposes the user name and current amount via properties.

    Examples:
        >>> p = Purchase("alice", "UK", 10.0)
        >>> p.user()
        'alice'
        >>> p.amount()
        10.0
    """

    def __init__(self, user: str, country: str, amount: float) -> None:
        """Initialise a Purchase instance.

        Args:
            user: name of the user making the purchase.
            country: country in which the purchase was made.
            amount: spend amount; must be non-negative.

        Raises:
            ValueError: If user is empty or amount is below zero.

        Examples:
            >>> p = Purchase("alice", "UK", 10.0)
            >>> p.user()
            'alice'
            >>> p.amount()
            10.0
        """
        if not user.strip():
            raise ValueError("user must be non-empty")
        if amount < 0:
            raise ValueError("amount must be non-negative")

        self._user = user.strip()
        self._country = country.strip()
        self._amount = float(amount)

    def is_in_country(self, country: str) -> bool:
        """Return True if this purchase was made in the given country, False otherwise.

        Examples:
            >>> p = Purchase("alice", "UK", 10.0)
            >>> p.is_in_country("UK")
            True
            >>> p.is_in_country("FR")
            False
        """
        return self._country == country

    def apply_fee(self, fee: float) -> None:
        """Add a fee to the purchase amount, mutating internal state.

        Raises:
            ValueError: If fee is negative.

        Examples:
            >>> p = Purchase("alice", "UK", 10.0)
            >>> p.apply_fee(0.25)
            >>> p.amount()
            10.25
        """
        if fee < 0:
            raise ValueError("fee must be non-negative")
        self._amount += fee

    def user(self) -> str:
        """Return the user id/name for this purchase.

        Examples:
            >>> p = Purchase("alice", "UK", 10.0)
            >>> p.user()
            'alice'
        """
        return self._user

    def amount(self) -> float:
        """Return the purchase amount including any applied fees.

        Examples:
            >>> p = Purchase("alice", "UK", 10.0)
            >>> p.amount()
            10.0
        """
        return self._amount


def parse_purchases(lines: list[str]) -> list[Purchase]:
    """Parse CSV-like lines into Purchase objects.

    Args:
        lines: a list of strings, each with comma-separated user, country, and amount fields.

    Returns:
        A list of Purchase objects created from the parsed lines.

    Raises:
        ValueError: If a line contains a non-numeric amount or an empty user name.

    Examples:
        >>> purchases = parse_purchases(["alice,UK,10.0", "bob,FR,5.0"])
        >>> len(purchases)
        2
        >>> purchases[0].user()
        'alice'
    """
    purchases: list[Purchase] = []
    for line in lines:
        user, country, amount_str = [part.strip() for part in line.split(",")]
        purchases.append(Purchase(user=user, country=country, amount=float(amount_str)))
    return purchases


def total_spend_by_user(purchases: list[Purchase], country: str) -> dict[str, float]:
    """Aggregate total spend per user for a given country.

    Args:
        purchases: a list of Purchase objects to aggregate over.
        country: only purchases matching this country are included.

    Returns:
        A dict mapping each user name to their total spend in the given country.

    Examples:
        >>> purchases = parse_purchases(["alice,UK,10.0", "alice,UK,2.0", "bob,FR,5.0"])
        >>> total_spend_by_user(purchases, "UK")
        {'alice': 12.0}
    """
    totals: dict[str, float] = {}
    for purchase in purchases:
        if purchase.is_in_country(country):
            user = purchase.user()
            totals[user] = totals.get(user, 0.0) + purchase.amount()
    return totals


def top_users(totals: dict[str, float], limit: int) -> list[tuple[str, float]]:
    """Return the top users by total spend.

    Args:
        totals: a dict mapping user names to their total spend.
        limit: the maximum number of users to return.

    Returns:
        A list of (user, total) tuples sorted by descending spend, then alphabetically by name,
        truncated to at most limit entries.

    Examples:
        >>> top_users({"alice": 12.0, "bob": 8.5}, limit=1)
        [('alice', 12.0)]
        >>> top_users({"alice": 12.0, "bob": 8.5}, limit=2)
        [('alice', 12.0), ('bob', 8.5)]
    """
    return sorted(totals.items(), key=lambda item: (-item[1], item[0]))[:limit]


def main() -> None:
    """Script entry point.

    Parses a set of hard-coded purchase records, applies a £0.25 fee to Alice's first
    purchase (bringing her total to £12.25), then prints the top UK spenders in
    descending order of spend.

    Examples:
        $ python lab_4.py
        1. alice: £12.25
        2. bob: £8.50
    """
    raw_lines = [
        "alice,UK,10.0",
        "bob,UK,3.5",
        "alice,UK,2.0",
        "carla,FR,100.0",
        "bob,UK,5.0",
    ]

    purchases = parse_purchases(raw_lines)
    purchases[0].apply_fee(0.25)

    totals = total_spend_by_user(purchases, country="UK")
    leaders = top_users(totals, limit=3)

    for rank, (user, total) in enumerate(leaders, start=1):
        print(f"{rank}. {user}: £{total:.2f}")


if __name__ == "__main__":
    main()