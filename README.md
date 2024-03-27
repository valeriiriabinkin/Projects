select isnull(tdb.[Db],tcr.[Cr]) acct, isnull(ob_db,0) ob_db, isnull(ob_cr,0) ob_cr
from 
(select [Счет по дебету] [Db], SUM([Приведенная сумма]) as ob_db from [СПБ Клиринг] group by [Счет по дебету]) tdb
full join 
(select [Счет по кредиту] [Cr], SUM([Приведенная сумма]) as ob_cr from [СПБ Клиринг] group by [Счет по кредиту]) tcr on tdb.[Db] = tcr.[Cr]
order by acct;



import xml.etree.ElementTree as ET

# Функция для чтения XML файла по частям и сохранения каждой части в отдельный файл
def split_xml(input_file, events_per_file):
    event_count = 0
    file_count = 0
    current_events = []

    # Итеративно обрабатываем каждый элемент XML из входного файла
    for event, element in ET.iterparse(input_file):
        if element.tag.endswith('Event'):  # Проверяем, если это элемент события
            current_events.append(element)

            # Если набрали нужное количество событий, сохраняем в файл
            if len(current_events) == events_per_file:
                # Создаем новое дерево XML
                root = ET.Element('EventLog')
                for event_elem in current_events:
                    root.append(event_elem)

                # Создаем дерево XML и сохраняем его в файл
                tree = ET.ElementTree(root)
                filename = f'output_{file_count}.xml'
                tree.write(filename, encoding='utf-8', xml_declaration=True)
                
                # Очищаем список текущих событий и увеличиваем счетчик файлов
                current_events = []
                file_count += 1

        # Удаляем обработанный элемент из памяти, чтобы избежать переполнения
        element.clear()

    # Сохраняем оставшиеся события в последний файл
    if current_events:
        root = ET.Element('EventLog')
        for event_elem in current_events:
            root.append(event_elem)
        tree = ET.ElementTree(root)
        filename = f'output_{file_count}.xml'
        tree.write(filename, encoding='utf-8', xml_declaration=True)

# Пример использования функции
split_xml('input.xml', events_per_file=2)


import xml.etree.ElementTree as ET

def process_large_xml(file_path):
    with open(file_path, 'rb') as f:
        context = ET.iterparse(f, events=('start', 'end'))

        # Перебор событий
        for event, elem in context:
            if event == 'end' and elem.tag == 'Event':  # Проверяем, если это конец элемента <Event>
                # Ваша обработка элемента <Event> здесь
                print(ET.tostring(elem))  # Пример вывода, замените на свою обработку

                # Удаление элемента, чтобы освободить память
                elem.clear()

# Пример использования
process_large_xml('large_file.xml')


tree = ET.parse(xml_file_path)
    root = tree.getroot()
    for event in root.findall('.//Event'):
        date = event.find('Date').text
        event_presentation = event.find('EventPresentation').text
        user_name = event.find('UserName').text if event.find('UserName') is not None else None

import xml.etree.ElementTree as ET

def split_large_xml(input_file, events_per_file):
    # Итеративно обрабатываем каждый элемент XML из входного файла
    context = ET.iterparse(input_file, events=('start', 'end'))
    event_count = 0
    file_count = 0
    current_events = []

    for event, elem in context:
        if event == 'end' and elem.tag.endswith('Event'):  # Проверяем, если это конец элемента <Event>
            current_events.append(elem)

            # Если набрали нужное количество событий, сохраняем в файл
            if len(current_events) == events_per_file:
                # Создаем новое дерево XML
                root = ET.Element('EventLog')
                for event_elem in current_events:
                    root.append(event_elem)

                # Создаем дерево XML и сохраняем его в файл
                tree = ET.ElementTree(root)
                filename = f'output_{file_count}.xml'
                tree.write(filename, encoding='utf-8', xml_declaration=True)
                
                # Очищаем список текущих событий и увеличиваем счетчик файлов
                current_events = []
                file_count += 1

    # Сохраняем оставшиеся события в последний файл
    if current_events:
        root = ET.Element('EventLog')
        for event_elem in current_events:
            root.append(event_elem)
        tree = ET.ElementTree(root)
        filename = f'output_{file_count}.xml'
        tree.write(filename, encoding='utf-8', xml_declaration=True)

# Пример использования
input_file = 'large_file.xml'
events_per_file = 1000  # Укажите желаемое количество событий в каждом файле
split_large_xml(input_file, events_per_file)


def load_xml_files_to_sql_server(folder_path, connection_string, events_per_file):
    # Получаем список XML файлов в указанной папке
    xml_files = [f for f in os.listdir(folder_path) if f.endswith('.xml')]

    # Подключаемся к базе данных
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Для каждого XML файла в папке
    for xml_file in xml_files:
        # Разбиваем файл на более мелкие с использованием функции split_large_xml
        split_large_xml(os.path.join(folder_path, xml_file), events_per_file)
        
        # Загружаем данные из каждого разделенного XML файла в базу данных
        for i in range(len(xml_files)):
            filename = f'output_{i}.xml'
            tree = ET.parse(filename)
            root = tree.getroot()

            for event in root.findall('.//Event'):
                date = event.find('Date').text
                event_presentation = event.find('EventPresentation').text
                user_name = event.find('UserName').text if event.find('UserName') is not None else None

                # SQL запрос для вставки данных
                sql_insert = "INSERT INTO YourTableName (Date, EventPresentation, UserName) VALUES (?, ?, ?)"
                cursor.execute(sql_insert, (date, event_presentation, user_name))

            # Фиксация изменений
            conn.commit()

    # Закрываем соединение
    conn.close()
