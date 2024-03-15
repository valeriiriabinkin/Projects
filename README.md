# Projects
all my projects
	<v8e:Event>
		<v8e:Date>2023-08-18T20:36:01</v8e:Date>
		<v8e:EventPresentation>Транзакция. Начало</v8e:EventPresentation>
		<v8e:UserName/>
	</v8e:Event>
import xml.etree.ElementTree as ET

def split_xml(input_file, output_prefix, chunk_size=1000):
    tree = ET.parse(input_file)
    root = tree.getroot()
    chunks = [root[i:i+chunk_size] for i in range(0, len(root), chunk_size)]
    
    for i, chunk in enumerate(chunks):
        output_file = f"{output_prefix}_{i+1}.xml"
        with open(output_file, "wb") as f:
            f.write(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write(ET.tostring(chunk))

# Пример использования
split_xml("input.xml", "output", chunk_size=1000)
