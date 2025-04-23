import operator
a=[('Pasta',300),('Sandwich',120),('Maggi',60),('Pizza',420),('Milkshake',190),('Pie',200)]
print("Sorted by price= ",sorted(a, key=operator.itemgetter(1)))
