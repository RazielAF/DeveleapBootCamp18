def main(word, parts):
    print(word)
    print(parts)
    part_list = parts.split(",")
    used_words = []  # new list to keep track of used words
    for i in range(0, len(word)):
        first_p = word[:i]
        print(f"first: {first_p}")
        second_p = word[i:]
        print(f"second {second_p}")
        if first_p in part_list and second_p in part_list and first_p != second_p:
            # check if both parts are in part_list and neither has been used before
            if first_p not in used_words and second_p not in used_words:
                used_words.extend([first_p, second_p])
                return [first_p, second_p]
    return []
