def word_counter():
    word = list(input('Choose word to search for: '))
    rev_word = list(word[::-1])
    print("select dimensions n(int) and m(int): ")
    n = int(input('n: '))
    m = int(input('m: '))
    lines = []
    if len(word) > max(n,m):
        return 0

    for i in range(n):
        line = input()
        lines.append([ch for ch in line.split(' ')])

    count = 0
    #calculate horizontally
    k=0
    for i in range(n):
        for j in range(m):
            j_temp = j
            while j_temp<m and lines[i][j_temp] == word[k]:
                k+=1
                if k==len(word):
                    count+=1
                    k=0
                j_temp+=1
            k=0
            j_temp = j
            while j_temp<m and lines[i][j_temp] == rev_word[k]:
                k+=1
                if k==len(word):
                    count+=1
                    k=0
                j_temp+=1
            k=0

    #calculate vertically
    for j in range(m):
        for i in range(n):
            i_temp = i
            while i_temp < n and lines[i_temp][j] == word[k]:
                k+=1
                if k==len(word):
                    count+=1
                    k=0
                i_temp+=1
            k=0
            i_temp = i
            while i_temp < n and lines[i_temp][j] == rev_word[k]:
                k+=1
                if k==len(word):
                    count+=1
                    k=0
                i_temp+=1
            k=0

    #if the word is palindrome, it is counted twice
    if word == rev_word:
        count//=2
    return count

print(word_counter())
