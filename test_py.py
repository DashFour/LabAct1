from random import choices as chc

letter_list, int_rank = [], []
num = 2
for i in range(65, 91):
    letter_list.append(chr(i))
    int_rank.append(num)
    num += 1

def get_count_after(letter: str):
    count = 0
    while True:
        item = chc(letter_list, weights=int_rank, k=1)[0]
        if item == letter:
            print(item, end=" ")
            print(f'\nletter {letter} found after {count} iterations')
            break
        else:
            print(item, end=" ")
            count += 1

for i in letter_list:
    get_count_after(i)
