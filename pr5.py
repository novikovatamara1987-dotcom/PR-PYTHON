users = []

for number in range(1, 3):
    print(f"\nПользователь {number}")
    login = input("Логин: ").strip()
    password = input("Пароль: ").strip()
    full_name = input("ФИО (фамилия, имя, отчество): ").strip()
    email = input("E-mail: ").strip()

    users.append([login, password, full_name, email])

letter = input("\nВведите букву, с которой должен начинаться логин: ").strip()

if len(letter) != 1:
    print("Нужно ввести ровно одну букву.")
else:
    search_letter = letter.casefold()

    # Выводятся только фамилии подходящих пользователей.
    for user in users:
        login = user[0]
        full_name = user[2]
        name_parts = full_name.split()

        if login.casefold().startswith(search_letter) and name_parts:
            print(name_parts[0])
