

'''

Day 2 : Count Character Occurrences using Python

'''

def count_charachters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
word = input("Enter your string: ")
print(count_charachters(word))

