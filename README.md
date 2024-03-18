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

# Загрузка исходного XML файла
tree = ET.parse('input.xml')
root = tree.getroot()

# Определяем количество событий в каждом файле
events_per_file = 2
total_events = len(root.findall('.//{http://v8.1c.ru/eventLog}Event'))

# Разделение файла на несколько файлов
for i in range(0, total_events, events_per_file):
    # Создаем новое дерево XML
    new_root = ET.Element(root.tag, attrib=root.attrib)
    
    # Добавляем события в новое дерево
    for event in root.findall('.//{http://v8.1c.ru/eventLog}Event')[i:i+events_per_file]:
        new_root.append(event)
    
    # Создаем новое дерево для нового файла
    new_tree = ET.ElementTree(new_root)
    
    # Сохраняем новый файл
    filename = f'output_{i // events_per_file}.xml'
    new_tree.write(filename, encoding='utf-8', xml_declaration=True)
