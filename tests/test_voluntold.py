import pytest

from voluntold import __version__
from voluntold.voluntold import pick, n_groups, groups_of


def test_version():
    assert __version__ == "0.1.0"


def test_pick_one(names):
    actual = pick(1, names)
    assert len(actual) == 1
    assert names.__contains__(actual[0])


def test_pick_two(names):
    actual = pick(2, names)
    assert len(actual) == 2
    assert names.__contains__(actual[0])
    assert names.__contains__(actual[1])


def test_group_of(names):
    actual = groups_of(2, names)
    assert len(actual) == 6
    assert names.__contains__(actual[0][0])


def test_n_groups(names):
    actual = n_groups(7, names)
    assert len(actual) == 7
    assert len(actual[-1]) == 1

    assert names.__contains__(actual[0][0])


@pytest.fixture
def names():
    return [
        "Fred",
        "Velma",
        "Daphne",
        "Shaggy",
        "Scooby",
        "Scrappy",
        "Flim Flam",
        "Vincent",
        "Barney",
        "Wilma",
        "Betty",
        "Bam Bam",
    ]
