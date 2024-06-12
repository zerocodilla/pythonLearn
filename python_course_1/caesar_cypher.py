def encrypt(text):
    result = []
    for i in range(len(text)):
        size = 0
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                size += 1
        cur_word = []

        for k in range(len(text[i])):
            if text[i][k].isalpha():
                new_number = ord(text[i][k]) + size
                if text[i][k].islower() and new_number > ord('z'):
                    new_number = new_number - ord('z') + ord('a') - 1
                    cur_word.append(chr(new_number))
                elif text[i][k].isupper() and new_number > ord('Z'):
                    new_number = new_number - ord('Z') + ord('A') - 1
                    cur_word.append(chr(new_number))
                else:
                    cur_word.append(chr(new_number))
            else:
                cur_word.append(text[i][k])
        result.append(''.join(cur_word))

    print(*result)


text = input().split()
encrypt(text)