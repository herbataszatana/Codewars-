def digital_root(n):
    # ...
    digits = [int(x) for x in str(n)]
    while len(digits)>1:
        sumDigits = sum(digits)
        print(sumDigits)
        digits = [int(x) for x in str(sumDigits)] 
    return int(digits[0])