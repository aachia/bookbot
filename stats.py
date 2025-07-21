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