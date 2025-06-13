def pattern1(n):
    for row in range(n):
        # for colums in each row
        for col in range(n-row):
            print('#',end=' ')
        print('')
# by default end = '\n'
pattern1(5)