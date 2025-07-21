def get_word_count(text):
    count = len(text.split())
    return count

def get_character_count(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered not in char_dict:
            char_dict[lowered] = 1
        else:
            char_dict[lowered] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dictionary(dict):
    sorted_list = []
    for key in dict:
        if key.isalpha():
            sorted_list.append({"char": key, "num": dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list