message = "Just one small positive thought in the morning can change your whole day"
char_count_dict = {}
for char in message:
    if char not in char_count_dict:
        char_count_dict[char] = 1
    else:
        char_count_dict[char] += 1
print(char_count_dict)

