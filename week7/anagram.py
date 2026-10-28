s1 = "listen"
s2 = "silent"

# frequyency = {}

# def get_frequency():

l = list(s2)

for ch in s2:
    if ch in l:
        l.remove(ch)
    else:
        print("Anagram")
        break
else:
    print("Not an Anagram")