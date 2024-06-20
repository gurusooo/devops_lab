class Person:
    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic

    def get_gender(self):
        last_char = self.patronymic[-1]
        return "Женский" if last_char == 'а' else "Мужской"

    def print_info(self):
        print("Gender: " + self.get_gender())

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

def main():
    print("Here we go, lab №3! To start with, enter your name in this way: Surname GivenName Patronymic:")
    name = input()
    name_cut = name.split(" ")
    last_name = name_cut[0]
    first_name = name_cut[1]
    patronymic = name_cut[2]
    person = Person(last_name, first_name, patronymic)
    person.print_info()

if __name__ == "__main__":
    main()
