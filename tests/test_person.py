import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import Person

def test_get_gender():
    person_man = Person("Волков", "Владимир", "Игоревич")
    assert person_man.get_gender() == "Мужской"

    person_woman = Person("Гурьянова", "Екатерина", "Сергеевна")
    assert person_woman.get_gender() == "Женский"

def test_get_full_name():
    person = Person("Устинов", "Ипполит", "Вениаминович")
    assert person.get_full_name() == "Устинов Ипполит Вениаминович"

if __name__ == "__main__":
    pytest.main()
