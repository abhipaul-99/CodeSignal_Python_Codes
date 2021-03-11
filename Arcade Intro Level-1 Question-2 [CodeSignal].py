def centuryFromYear(year):

    if(year%100==0):

        c = year/100

        return c

    else:

        c= (year//100)+1

        return c
