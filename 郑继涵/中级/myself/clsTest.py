def fabonic(n):
    if n<1:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fabonic(n-1)+fabonic(n-2)

print(fabonic(8))