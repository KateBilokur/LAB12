import json

# Початкові дані про команди
teams = [
    {"Name": "Команда A", "Points": 45},
    {"Name": "Команда B", "Points": 42},
    {"Name": "Команда C", "Points": 38},
    {"Name": "Команда D", "Points": 35},
    {"Name": "Команда E", "Points": 33},
    {"Name": "Команда F", "Points": 30},
    {"Name": "Команда G", "Points": 28},
    {"Name": "Команда H", "Points": 25},
    {"Name": "Команда I", "Points": 22}
]

# Запис даних у JSON-файл
with open("teams.json", "w") as file:
    json.dump(teams, file)

# Функція для виведення вмісту JSON-файлу
def view_teams():
    with open("teams.json", "r") as file:
        teams = json.load(file)
        for team in teams:
            print(team)

# Функція для додавання нової команди
def add_team():
    try:
        name = input("Введіть назву нової команди: ")
        points = int(input("Введіть кількість набраних очок: "))

        with open("teams.json", "r") as file:
            teams = json.load(file)

        teams.append({"Name": name, "Points": points})

        with open("teams.json", "w") as file:
            json.dump(teams, file)

        print("> Команда успішно додана.")
    except ValueError:
        print("> Помилка: очки мають бути числом.")

# Функція для видалення команди
def remove_team():
    name = input("Введіть назву команди, яку потрібно видалити: ")
    with open("teams.json", "r") as file:
        teams = json.load(file)

    new_teams = [team for team in teams if team["Name"] != name]

    if len(new_teams) < len(teams):
        with open("teams.json", "w") as file:
            json.dump(new_teams, file)
        print("> Команда успішно видалена.")
    else:
        print("> Помилка: команди з такою назвою не знайдено.")

# Функція для пошуку команди за очками
def search_team():
    points = int(input("Введіть кількість очок для пошуку: "))
    with open("teams.json", "r") as file:
        teams = json.load(file)

    found_teams = [team for team in teams if team["Points"] == points]

    if found_teams:
        print("> Знайдені команди:")
        for team in found_teams:
            print(team)
    else:
        print("> Команд з такою кількістю очок не знайдено.")

# Функція для визначення місця та команд, які мають менше очок
def determine_team_position():
    try:
        points = int(input("Введіть кількість очок нової команди: "))
        with open("teams.json", "r") as file:
            teams = json.load(file)

        # Сортуємо команди за кількістю очок у зменшуваному порядку
        sorted_teams = sorted(teams, key=lambda x: x["Points"], reverse=True)
        position = 1
        for i, team in enumerate(sorted_teams, start=1):
            if points > team["Points"]:
                position = i
                break
            position = i + 1

        print(f"> Місце нової команди: {position}")

        # Визначення команд, які мають менше очок
        less_points_teams = [team for team in sorted_teams if team["Points"] < points]

        print("\n> Команди, які мають менше очок:")
        for team in less_points_teams:
            print(team)

        # Запис результатів у новий JSON-файл
        with open("result.json", "w") as file:
            json.dump({"position": position, "less_points_teams": less_points_teams}, file)

        print("> Результат записано в result.json")

    except ValueError:
        print("> Помилка: очки мають бути числом.")

# Основний цикл для діалогу з користувачем
while True:
    print("\n\t* Меню *")
    choice = input("> 1 - Перегляд даних\n> 2 - Додавання команди\n> 3 - Видалення команди\n"
                   "> 4 - Пошук команди за очками\n> 5 - Визначення місця нової команди\n> 0 - Вихід\n"
                   "> Ваш вибір: ")

    if choice == '1':
        view_teams()
    elif choice == '2':
        add_team()
    elif choice == '3':
        remove_team()
    elif choice == '4':
        search_team()
    elif choice == '5':
        determine_team_position()
    elif choice == '0':
        print("> Програма завершена.")
        break
    else:
        print("> Помилка: незареєстрована дія.")
