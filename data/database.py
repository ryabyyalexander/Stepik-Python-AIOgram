# Создаем шаблон заполнения словаря с пользователями
user_dict_template = {'page': 1,
                      'bookmarks': set()}

# Инициализируем "базу данных"
users_db = {}
user_dict: dict[int, dict[str, str | int | bool]] = {}