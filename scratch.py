year = int(input("year"))
month =int(input("month"))
day = int(input("day"))
def bdy(year,month,day):
    sal = year - 56
    if month <= 9 and day<=15:
        print(f"your year is {sal-1} ad")
    else:
        print(f"your year is {sal } ad")
    if(month == 9 and ( day>15 and day<=32)) or (month ==10 and (day >=1 and day <18 )):
            print("your month is jan")
    elif (month == 10 and( day>17 and day<=32)) or (month ==11 and (day >= 1 and day <17)):
                    print("your month is feb")
    elif (month == 11 and( day>17 and day<=32)) or (month ==12 and (day >= 1 and day <18)):
                    print("your month is march")
    elif (month == 12 and( day>18 and day<=32)) or (month ==1 and (day >= 1 and day <17)):
                    print("your month is april")
    elif (month == 1 and( day>18 and day<=31 )) or (month == 2 and (day >=1  and day < 17)):
                    print("your month is may ")
    elif (month == 2 and( day> 18 and day<= 32)) or (month  == 3 and (day >=1  and day <= 15)):
                    print("your month is june ")
    elif (month == 3 and( day> 15 and day<= 32 )) or (month  == 4 and (day >= 1 and day < 16)):
             print("your month is july ")
    elif (month == 4 and( day>=16 and day<= 32)) or (month  == 5 and (day >= 1 and day <14)):
                    print("your month is agust ")
    elif (month == 5 and( day>14 and day<=32 )) or (month  == 6 and (day >=1 and day < 13)):
                    print("your month is sept ")
    elif (month ==  6 and( day> 14 and day<= 30)) or (month == 7 and (day >=1  and day <15)):
                    print("your month is oct")
    elif (month == 7 and( day>14 and day<=30 )) or (month  ==  8 and (day >=1  and day <16)):
                    print("your month is nov")
    elif (month == 8 and( day>14 and day<= 32)) or (month == 9 and (day >=1 and day <15)):
                    print("your month is decembeer")


    if ( month == 1 and day <18):
                    print(f"your day is {day+13}")
    if ( month == 1 and day >=18):
                    print(f"your day is {day-17}")
    if ( month == 2 and day <18):
                    print(f"your day is {day+14}")
    if ( month == 2 and day >=18):
                    print(f"your day is {day-17}")
    if ( month == 3 and day<16 ):
                    print(f"your day is {day+15}")
    if ( month == 3 and day >=16 ):
                    print(f"your day is {day-15}")
    if ( month == 4 and day <16):
                    print(f"your day is {day+16}")
    if ( month == 4 and day>=16 ):
                    print(f"your day is {day-15}")
    if ( month == 5 and day<15 ):
                    print(f"your day is {day+17}")
    if ( month == 5  and day>= 15):
                    print(f"your day is {day-14}")
    if ( month == 6  and day<14 ):
                    print(f"your day is {day+17}")
    if ( month == 6 and day>=14 ):
                    print(f"your day is {day-13}")
    if ( month == 7  and day <15 ):
                    print(f"your day is {day+17}")
    if ( month == 7 and day >= 15 ):
                    print(f"your day is {day-14}")
    if ( month == 8  and day <15 ):
                    print(f"your day is {day+16}")
    if ( month == 8  and day>=15 ):
                    print(f"your day is {day-14}")
    if ( month == 9  and day <16):
                    print(f"your day is {day+16}")
    if ( month == 9 and day>=16 ):
                    print(f"your day is {day-15}")
    if ( month == 10 and day < 18):
                    print(f"your day is {day+14}")
    if ( month == 10  and day>=18 ):
                    print(f"your day is {day-17}")
    if ( month == 11 and day<18 ):
                    print(f"your day is {day+12}")
    if ( month == 11 and day>=18):
                    print(f"your day is {day-17}")
    if ( month == 12  and day <19 ):
                    print(f"your day is {day+13}")
    if ( month == 12 and day >=19):
                    print(f"your day is {day-18}")

























bdy(year,month,day)


