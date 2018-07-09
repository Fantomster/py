integers = range(8)
squared = ( i * i for i in integers)
negated = ( -i for i in squared)
print(list(negated))