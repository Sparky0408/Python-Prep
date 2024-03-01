fact = lambda a: 1 if a==0 else a*fact(a-1)

result = fact (5)

print(result)