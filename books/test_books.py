import urllib.request

import pytest

from books import word_count

@pytest.fixture(scope="session")
def long_book():
    url = "https://www.gutenberg.org/files/2600/2600-0.txt"
    book_text = urllib.request.urlopen(url).read().decode('utf-8')
    return book_text

@pytest.mark.parametrize('word, count',  [
    ('hat', 33),
    ('freedom', 71),
    ('electricity', 1),
    ('testing', 3),
    ('Prince', 1499),
    ('internet', 0),
    ('Russia', 71),
    ('Pierre', 1260),
    (None, 566334),
])
def test_word_counts(long_book, word, count):
    assert word_count(long_book, word) == count