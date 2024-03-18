<?xml version="1.0" encoding="UTF-8"?>
<v8e:EventLog xmlns:v8e="http://v8.1c.ru/eventLog" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<v8e:Event>
		<v8e:Date>2023-08-18T20:35:58</v8e:Date>
		<v8e:EventPresentation>Сеанс. Начало</v8e:EventPresentation>
		<v8e:UserName/>
	</v8e:Event>
	<v8e:Event>
		<v8e:Date>2023-08-18T20:36:00</v8e:Date>
		<v8e:EventPresentation>Сеанс. Завершение</v8e:EventPresentation>
		<v8e:UserName/>
	</v8e:Event>



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
