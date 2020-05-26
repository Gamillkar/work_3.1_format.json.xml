import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml')

root = tree.getroot()

def list_creation():
    data_list = []
    xml_items = root.findall('channel/item')
    for xmli in xml_items:
        for line_text in xmli:
            data_list += (line_text.text).split()

    add_data = root.findall('channel')
    for xmli in add_data:
        for line_text in xmli:
            if line_text.tag != 'item':
                data_list += (line_text.text).split()
    return data_list
def sorted_data_list():
    data_list = list_creation()
    temp_dict = {}

    for word in sorted(data_list):
        if len(word) > 6:
            max_frequently_score = data_list.count(word)
            temp_dict[word.lower()] = max_frequently_score
    max_frequently_dict = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
    max_frequently_list = list()
    for max_word, max_value in max_frequently_dict:
        max_frequently_list.append(max_word)
    print(max_frequently_dict)
    print(max_frequently_list[:10])

sorted_data_list()