import sys

count = 0
for line in sys.stdin:
    print(line)
    count += 1

# print goes to sys.stdout
print(count)