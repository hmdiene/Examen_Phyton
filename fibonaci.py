def suite(n):
    table = [1,1]
    k = 1
    while max(table) <= n:
        table.append( table[k-1] + table[k] )
        k += 1
    table.pop()
    
    return table[1:]

print(suite(6))