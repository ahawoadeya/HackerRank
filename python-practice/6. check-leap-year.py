def is_leap_year(year):
    leap = False
    
    if(1900 <= year <= pow(10, 5)):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    leap = True
            else:
                leap = True
    
    return leap


year = int(input())
print(is_leap_year(year))