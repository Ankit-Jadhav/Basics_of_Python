def extra_digit(s):
    check_digit = [char for char in s if char.isdigit()]
    print(''.join(check_digit))  
    return ''.join(sorted(set(check_digit)))
    

print(extra_digit("odjfojdof 347394dhifdif 394839fdfjidf"))
      