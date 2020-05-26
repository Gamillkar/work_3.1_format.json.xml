import json

with open('newsafr.json', encoding='utf-8') as file:
    read = json.load(file)

def list_creation():
    data_list = []
    items_file = read['rss']["channel"]
    for teg, text in items_file.items():
        if teg == "items":
            for value in text:
                basic_data =  value.values()
                for word in basic_data:
                    data_list += word.split()
        else:
            data_list += text.split()
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
