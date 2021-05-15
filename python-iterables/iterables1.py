"""Describes container Sentence and iterator SentenceIterator"""


import re

class SentenceIterator:
    """Iterator for class Sentence"""

    def __init__(self, words):
        self._words = words
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._words):
            raise StopIteration
        result = self._words[self._index]
        self._index += 1
        return result

class Sentence:
    """Describes a sentence container"""

    def __init__(self, text: str):
        self.text = text
        if not isinstance(self.text, str):
            raise TypeError("Transmitted argument is not string!")
        if self.text[-1] not in [".", "!", "?"]:
            raise ValueError("Sentence hasn't finishing sign!")

    def __repr__(self):
        return f"<Sentence(word={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def _words(self):
        """Implement lazy iterator"""
        for word in re.findall(r"\w+", self.text):
            yield word

    def __getitem__(self, idx):
        """Return word by index"""
        return self.words[idx]

    @property
    def words(self):
        """Returns list of the words"""
        return list(self._words())

    @property
    def other_chars(self):
        """Returns list of special chars"""
        return re.findall(r'[,.!?_\':;/#%*\=@"]', self.text)

if __name__ == "__main__":
    ex_sentence = Sentence("Hello, world=! It''#s me!")
    for i in ex_sentence:
        print(i)
    print(ex_sentence[1:3])
    print(ex_sentence)
    print(ex_sentence.words)
    print(ex_sentence.other_chars)
