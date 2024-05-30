c1 = []
c2 = []
def encrypt(s, key1, key2):
    n = len(key1)
    st = ''
    table = list(s)
    count2, count3, count = 0, 0, 0
    for i in range(len(table) + len(key2)): 
        count1 = i%n
        if count1 == 0:
            count2 += 1
        for k in range(len(key2)):
            if count2 < key2[k][0]:
                break
            elif count2 > key2[k][0]:
                continue
            elif count2 == key2[k][0] and count1 + 1 == key2[k][1]:
                table.insert(i, '∑')                                   # символ ∑ будет блокировать ячейку таблицы и
    table = [''.join(table[i:i+n]) for i in range(0, len(table), n)]   #будет пропускаться при составлении зашифрованной строки
    for t in table:
        print(t)
    for q in range(n):
        for j in range(n):
            if key1[j] == q + 1:
                for t in table:
                    if len(t) >= j + 1 and t[j] != '∑':
                        st += t[j]
                        count += 1
                        count3 += 1
                    elif len(t) >= j + 1 and t[j] == '∑':
                        count += 1
                c1.append(count)
                c2.append(count3)
                count, count3 = 0, 0
            else:
                continue
            break
    return st

def decrypt(s, key1, key2):
    n = len(key1)
    st = ''
    table1 = list(s)
    table2, table = [], []
    count = 0
    for i in range(n):
        if c1[i] > c2[i]:
            for a in range(len(key2)):
                if key2[a][1] == (key1.index(i + 1) + 1):
                    table1.insert(key2[a][0] - 1,'∑')
            table2.append(''.join(table1[0:c1[i]]))
            del table1[0:c1[i]]
        else:
            table2.append(''.join(table1[0:c1[i]]))
            del table1[0:c1[i]]
    for k in range(n):
        for x in range(n):
            if k == key1.index(x + 1):
                table.append(table2[x])
    for q in range(max(c1)):
        for t in table:
            if q + 1 > len(t):
                continue
            elif t[q] == '∑':
                continue
            else:
                st += t[q]
    return st

s = input("Введите сообщение: ")
key_input1 = input("Введите ключ (числа разделены пробелами): ")
key1 = [int(k) for k in key_input1.split()]
key_input2 = input("Введите ключ усложнения (числа разделены пробелами и состовляют пары: ряд-ячейка): ")
key2_intermediate = [int(k) for k in key_input2.split()]
key2 = []
for k in range(0, len(key2_intermediate), 2):
    key2.append(key2_intermediate[k:k+2])
key2.sort()
s = encrypt(s, key1, key2)
print("Зашифрованный текст:", s)
s = decrypt(s, key1, key2)
print("Расшифрованный текст:", s)
