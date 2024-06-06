string = input("Enter String: ")
l = list(string)
frequency_char = [l.count(ele) for ele in l]
d = dict(zip(l,frequency_char))
print(d)
