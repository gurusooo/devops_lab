import pytest

from main import Person

def test_get_gender():
    person_man = Person("Волков", "Владимир", "Игоревич")
    assert person_man.get_gender() == "Мужской"

    person_woman = Person("Гурьянова", "Екатерина", "Сергеевна")
    assert person_woman.get_gender() == "Женский"

if __name__ == "__main__":
    pytest.main()
