"""A word frequency counter module.

Classes:
    Counter: Counts occurrences of words and provides frequency queries.

Examples:
    >>> c = Counter()
    >>> c.add("hello", 3)
    >>> c.count("hello")
    3
"""

class Counter:
    """Counts occurrences of words and provides frequency queries.

    Attributes:
        words: A dictionary mapping words to their counts.

    Examples:
        >>> c = Counter()
        >>> c.add("hello", 3)
        >>> c.count("hello")
        3
    """

    words: dict[str, int]

    def __init__(self) -> None:
        """Initialises an empty counter.

        Examples:
            >>> c = Counter()
            >>> c.words
            {}
        """
        self.words = {}

    def add(self, item: str, n: int = 1) -> None:
        """Increases the stored count for a word by the repetition count.

        Args:
            item: The word to add to the counter.
            n: The number of times to add the word. Defaults to 1.

        Raises:
            ValueError: If n is less than 1.

        Examples:
            >>> c = Counter()
            >>> c.add("hello")
            >>> c.add("hello", 3)
            >>> c.words["hello"]
            4
        """
        if n < 1:
            raise ValueError("Repetition count is less than 1")
        self.words[item] = self.words.get(item, 0) + n


    def count(self, item: str) -> int:
        """Returns the stored count for a word.

        Args:
            item: The word to look up.

        Returns:
            The number of times the word has been added, or 0 if never added.

        Examples:
            >>> c = Counter()
            >>> c.add("hello", 2)
            >>> c.count("hello")
            2
            >>> c.count("world")
            0
        """
        return self.words.get(item, 0)


    def most_common(self) -> tuple[str, int]:
        """Returns the most common word and its count.

        In the case of a tie, returns the word that comes first alphabetically.

        Returns:
            A tuple of (word, count) where word is the most common word.

        Raises:
            ValueError: If the counter is empty.

        Examples:
            >>> c = Counter()
            >>> c.add("the", 3)
            >>> c.add("cat", 3)
            >>> c.most_common()
            ('cat', 3)
        """
        if not self.words:
            raise ValueError("Counter is empty")
        highest = max(self.words.values())
        highest_list = []
        for key, value in self.words.items():
            if value == highest:
                highest_list.append(key)
        highest_list = sorted(highest_list)
        return highest_list[0], highest


def main():
    counter = Counter()

    string = "The cat in the hat sat on the cat. Poor cat.".lower()

    for word in string.split():
        counter.add(word.strip(".,!?"))

    print(counter.count("the"))
    print(counter.count("cat"))
    print(counter.most_common())

if __name__ == "__main__":
    main()
