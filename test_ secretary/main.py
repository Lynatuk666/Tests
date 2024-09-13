documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    for some_dict in documents:
        if doc_number in some_dict.values():
            return some_dict["name"]
    return "Документ не найден"


def get_directory(doc_number):
    for k, v in directories.items():
        if doc_number in v:
            return k
    return "Полки с таким документом не найдено"


def add(document_type, number, name, shelf_number):
    try:
        documents.append({
            "type": document_type,
            "number": number,
            "name": name
        })
        directories[f"{shelf_number}"].append(number)
        return "Добавлено"
    except Exception:
        return "Ошибка"


if __name__ == '__main__':
    pass
# print(get_name("10006"))
# get_directory("11-2")
# get_name("101")
# add('international passport', '311 020203', 'Александр Пушкин', 3)
# get_directory("311 020203")
# get_name("311 020203")
# get_directory("311 020204")
