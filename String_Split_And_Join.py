# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    res = line.split(" ")
    newRes = "-".join(res)
    return newRes

line = input().strip()
result = split_and_join(line)
print(result)

# strip method removes leading and trailing whitespace