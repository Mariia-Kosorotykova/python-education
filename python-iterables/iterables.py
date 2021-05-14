"""This module describes iterators"""

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.words):
            raise StopIteration
        result = self.words[self.counter]
        self.counter += 1
        return result

class Sentence:
    def __init__(self, text:str):
        self.text = text
        if not isinstance(self.text, str):
            raise TypeError("Transmitted argument is not string")
        if self.text[-1] not in [".", "!", "?"]:
            raise ValueError("Sentence hasn't finishing sign ")

    def __repr__(self):
        return f"<Sentence(word={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def _words(self):
        return <lazy iterator>

    @property
    def words(self):
        return words in text

    @property
    def other_chars(self):
        return not words