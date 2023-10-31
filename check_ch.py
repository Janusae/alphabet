string = 'the quick brown fox umps over a lazy dgjo'.replace(" " , "")
list_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0
for i in list_one :
    if i not in string :
        count += 1
        print(F"({i}) is not in sentence")
if count == 0 :
    print("""True
The sentence has all the character""")
