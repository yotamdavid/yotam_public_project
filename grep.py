def search_word_in_file(word, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if word in line:
                print(line, end='')
search_word_in_file('test', 'file.txt')