print("\t\t\t\t\t-----------------")
print("\t\t\t\t\t **OPERATIONS**")
print("\t\t\t\t\t-----------------")
print("*************************************************************************")
print("==[1]==>'ADDITION'");print("==[2]==>'SUBTRACTION'")
print("==[3]==>'MULTIPLICATION'");print("==[4]==>'DIVISION")
print("==[5]==>'SQUARE ROOT'");print("==[6]==>'UNDER ROOT'");print("==[7]==>'COMMON LOGARITHM'-log10-")
print("==[8]==>'NATURAL LOGARITHM'-ln-");print("==[9]==>'FACTORIAL'");print("==[10]==>'PI'")
print("==[11]==>'PI WITH OPERATION -,+,//,* 'A,S,D,M'")
print("==[12]==>'SIN'===>OUTPUT IN RADIANS -OR- DEGRESS");print("==[13]==>'COS'===>OUTPUT IN RADIANS -OR- DEGRESS")
print("==[14]==>'TAN'===>OUTPUT IN RADIANS -OR- DEGRESS")
print("==[15]==>'SIN'==>'COS'==>'TAN'===>OUTPUT IN RADIANS -OR- DEGRESS WITH OPERATION -,+,//,*,'A,S,D,M'")
print("==[16]==>'SIN'===>INVERSE OUTPUT IN RADIANS -OR- DEGRESS");print("==[17]==>'COS'===>INVERSE OUTPUT IN RADIANS -OR- DEGRESS")
print("==[18]==>'TAN'===>INVERSE OUTPUT IN RADIANS -OR- DEGRESS")
print("==[19]==>'SIN'==>'COS'==>'TAN'===>INVERSE IN RADIANS -OR- DEGRESS WITH OPEARTION -,+,//,*,'A,S,D,M'")
print("==[20]==>'SIN'===>HYPERBOLIC OUTPUT IN RADIANS -OR- DEGRESS");print("==[21]==>'COS'===>HYPERBOLIC OUTPUT IN RADIANS -OR- DEGRESS")
print("==[22]==>'TAN'===>HYPERBOLIC OUTPUT IN RADIANS -OR- DEGRESS")
print("==[23]==>'SIN'==>'COS'==>'TAN'===>HYPERBOLIC IN RADIANS -OR- DEGRESS WITH OPERATION -,+,//,*'A,S,D,M'")
print("**************************************************************************")
select=int(input("ENTER HERE YOUR DESIRE OPTION >  1 TO 23 :<==>: "))
print("YOUR CHOISE IS THAT ==> ",select)
print("**************************************************************************")
if select == 1:
    print("\t\t___________________________")
    print("\t\t -YOUR CHOISED IS ADDITION-")
    print("\t\t___________________________")
    a=int(input("ENTER FIRST NUMBER:>: "))
    b=int(input("ENTER SECOND NUMBER:>: "))
    print("------------------------")
    c=a+b
    print("CALCULATING RESULT ==> ",c)
    print("------------------------")
elif select == 2:
    print("\t\t_______________________________")
    print("\t\t-YOUR CHOISED IS SUBTRACTION-")
    print("\t\t_______________________________")
    a=int(input("ENTER FIRST NUMBER:>: "))
    b=int(input("ENTER SECOND NUMBER:>: "))
    print("--------------------------")
    c=a-b
    print("CALCULATING RESULT ==> ",c)
    print("--------------------------")
elif select == 3:
    print("\t\t_______________________________")
    print("\t\t-YOUR CHOISED IS MULTIPLICATION-")
    print("\t\t_______________________________")
    a=int(input("ENTER FIRST NUMBER:>: "))
    b=int(input("ENTER SECOND NUMBER:>: "))
    print("--------------------------")
    c=a*b
    print("CALCULATING RESULT ==> ",c)
    print("--------------------------")
elif select == 4:
    print("\t\t__________________________")
    print("\t\t-YOUR CHOISED IS DIVISION-")
    print("\t\t__________________________")
    a=int(input("ENTER FIRST NUMBER:>: "))
    b=int(input("ENTER SECOND NUMBER:>: "))
    print("--------------------------")
    c=a/b
    print("CALCULATING RESULT ==> ",c)
    print("--------------------------")
elif select == 5:
    print("\t\t_______________________________")
    print("\t\t-YOUR CHOISED IS SQUARE ROOT-")
    print("\t\t_______________________________")
    a=int(input("ENTER OR WRITE FIRST NUMBER:>: "))
    b=int(input("ENTER OR WRITE SECOND NUMBER:>: "))
    print("--------------------------")
    c=a**b
    print("CALCULATING RESULT ==> ",c)
    print("--------------------------")
elif select == 6:
    print("\t\t_____________________________")
    print("\t\t-YOUR CHOISED IS UNDER ROOT-")
    print("\t\t_____________________________")
    a=int(input("ENTER OR WRITE VALUE OF UNDER ROOT :>: "))
    print("--------------------------")
    c=a**0.5
    print("CALCULATING RESULT ==> ",c)
    print("--------------------------")
elif select==7:
    print("\t\t___________________________________________")
    print("\t\t-YOUR CHOISED IS COMMON LOGARITHM-log10-")
    print("\t\t___________________________________________")
    import math
    a=int(input("ENTER HERE Log VALUE :>:"))
    b=math.log10(a)
    print("-------------------------------")
    print("CALCULATING RESULT ==> ",b)
    print("-------------------------------")
elif select==8:
    print("\t\t_________________________________________")
    print("\t\t-YOUR CHOISED IS NATURAL LOGARITHM-ln-")
    print("\t\t_________________________________________")
    import math
    a=int(input("ENTER HERE ln VALUE :>:"))
    b=math.log(a)
    print("-------------------------------")
    print("CALCULATING RESULT ==> ",b)
    print("-------------------------------")
elif select==9:
    print("\t\t_____________________________")
    print("\t\t-YOUR CHOISED IS FACTORIAL")
    print("\t\t_____________________________")
    import math
    a=int(input("ENTER HERE FACTORAIL VALUE :>:"))
    b=math.factorial(a)
    print("-------------------------------")
    print("CALCULATING RESULT ==> ",b)
    print("-------------------------------")
elif select==10:
    print("\t\t_______________________")
    print("\t\t-YOUR CHOISED IS PI-")
    print("\t\t_______________________")
    import math
    a=int(input("ENTER HERE 'PI' VALUE :>:"))
    b=math.pi*a
    print("-------------------------------")
    print("CALCULATING RESULT ==> ",b)
    print("-------------------------------")
elif select==11:
    print("\t\t_________________________________________________________")
    print("\t\t-YOUR CHOISED IS PI WITH OPERATION -,+,//,8 'A,S,D,M'")
    print("\t\t________________________________________________________")
    a=str(input("WHAT YOU WANT 'PI' WITH OPEARTION -,+,//,* 'A,S,D,M' ENTER HERE:>:"))
    if a=='+'or a=='A'or a=='a'or a=='ADDITION'or a=='addition'or a=='ADD'or a=='add':
        print("\t\t**********************************")
        print("\t\t-CHOISED IS 'PI' WITH ADDITION-")
        print("\t\t**********************************")
        import math
        a=int(input("ENTER HERE 'PI' VALUE :>:"))
        b=int(input("ENTER HERE 'ADDITION' VALUE:>:"))
        c=math.pi*a+b
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",c)
        print("-------------------------------")
    elif a=='-'or a=='subtraction'or a=='SUBTRACTION'or a=='sub'or a=='SUB'or a=='s'or a=='S':
        print("\t\t**************************************")
        print("\t\t-CHOISED IS 'PI' WITH SUBTRACTION-")
        print("\t\t**************************************")
        import math
        a=int(input("ENTER HERE 'PI' VALUE :>:"))
        b=int(input("ENTER HERE 'SUBTRACTION' VALUE:>:"))
        c=math.pi*a-b
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",c)
        print("-------------------------------")
    elif a=='/'or a=='//'or a=='DIVISION'or a=='division'or a=='div'or a=='DIV'or a=='d'or a=='D':
        print("\t\t**********************************")
        print("\t\t-CHOISED IS 'PI' WITH DIVISION-")
        print("\t\t**********************************")
        import math
        a=int(input("ENTER HERE 'PI' VALUE :>:"))
        b=int(input("ENTER HERE 'DIVISION' VALUE:>:"))
        c=math.pi*a/b
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",c)
        print("-------------------------------")
    elif a=='*'or a=='MULTPLYCATION'or a=='multplycation'or a=='multply'or a=='MULTPLY'or a=='m'or a=='M':
        print("\t\t***************************************")
        print("\t\t-CHOISED IS 'PI' WITH MULTPLICATION-")
        print("\t\t***************************************")
        import math
        a=int(input("ENTER HERE 'PI' VALUE :>:"))
        b=int(input("ENTER HERE 'MULTPLY' VALUE:>:"))
        c=math.pi*a*b
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",c)
        print("-------------------------------")
    else:
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!____")
        print("WRONG OPERATION IN PI WITH OPERATION")
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!____")
elif select==12:
    print("\t\t___________________________________________________")
    print("\t\t-CHOISED IS 'SIN' OUTPUT IN RADIANS -OR- DEGRESS-")
    print("\t\t___________________________________________________")
    a=str(input("WHAT YOU WANT 'SIN' OUTPUT IN RADIANS OR DEGRESS ENTER HERE:>:"))
    if a=='radians'or a=='RADIANS'or a=='rad'or a=='RAD'or a=='R'or a=='r':
        print("\t\t***************************************")
        print("\t\t-CHOISED IS 'SIN' OUTPUT IN RADIANS-")
        print("\t\t***************************************")
        import math
        a=int(input("ENTER HERE 'SIN' VALUE :>:" ))
        b=math.sin(math.radians(a))
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",b)
        print("-------------------------------")
    elif  a=='degress'or a=='DEGRESS'or a=='deg'or a=='DEG'or a=='d'or a=='D':
        print("\t\t**************************************")
        print("\t\t-CHOISED IS 'SIN' OUTPUT IN DEGRESS-")
        print("\t\t**************************************")
        import math
        a=int(input("ENTER HERE 'SIN' VALUE :>:" ))
        b=math.sin(math.degrees(a))
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",b)
        print("-------------------------------")
    else:
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!______")
        print("WRONG VALUE SIN OUTPUT IN RADIANS OR DEGRESS ")
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!______")
elif select==13:
    print("\t\t___________________________________________________")
    print("\t\t-CHOISED IS 'COS' OUTPUT IN RADIANS -OR- DEGRESS-")
    print("\t\t___________________________________________________")
    a=str(input("WHAT YOU WANT 'COS' OUTPUT IN RADIANS OR DEGRESS ENTER HERE:>:"))
    if a=='radians'or a=='RADIANS'or a=='rad'or a=='RAD'or a=='R'or a=='r':
        print("\t\t***************************************")
        print("\t\t-CHOISED IS 'COS' OUTPUT IN RADIANS-")
        print("\t\t***************************************")
        import math
        a=int(input("ENTER HERE 'COS' VALUE :>:" ))
        b=math.cos(math.radians(a))
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",b)
        print("-------------------------------")
    elif  a=='degress'or a=='DEGRESS'or a=='deg'or a=='DEG'or a=='d'or a=='D':
        print("\t\t****************************************")
        print("\t\t-CHOISED IS 'COS' OUTPUT IN DEGRESS-")
        print("\t\t****************************************")
        import math
        a=int(input("ENTER HERE 'COS' VALUE :>:" ))
        b=math.cos(math.degrees(a))
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",b)
        print("-------------------------------")
    else:
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!_____")
        print("WRONG VALUE COS OUTPUT IN RADIANS OR DEGRESS ")
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!_____")
elif select==14:
    print("\t\t___________________________________________________")
    print("\t\t-CHOISED IS 'TAN' OUTPUT IN RADIANS -OR- DEGRESS-")
    print("\t\t___________________________________________________")
    a=str(input("WHAT YOU WANT 'TAN' OUTPUT IN RADIANS OR DEGRESS ENTER HERE:>:"))
    if a=='radians'or a=='RADIANS'or a=='rad'or a=='RAD'or a=='R'or a=='r':
        print("\t\t***************************************")
        print("\t\t-CHOISED IS 'TAN' OUTPUT IN RADIANS-")
        print("\t\t***************************************")
        import math
        a=int(input("ENTER HERE 'TAN' VALUE :>:" ))
        b=math.tan(math.radians(a))
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",b)
        print("-------------------------------")
    elif  a=='degress'or a=='DEGRESS'or a=='deg'or a=='DEG'or a=='d'or a=='D':
        print("\t\t****************************************")
        print("\t\t-CHOISED IS 'TAN' OUTPUT IN DEGRESS-")
        print("\t\t****************************************")
        import math
        a=int(input("ENTER HERE 'TAN' VALUE :>:" ))
        b=math.tan(math.degrees(a))
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",b)
        print("-------------------------------")
    else:
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!_____")
        print("WRONG VALUE TAN OUTPUT IN RADIANS OR DEGRESS ")
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!_____")
elif select==15:
    print("\t\t____________________________________________________________________________________________________")
    print("\t\t-CHOISED IS 'SIN','COS','TAN', OUTPUT IN RADIAN -OR- DEGRESS WITH OPERATIONS -,+,//,* 'A,S,D,M'-")
    print("\t\t____________________________________________________________________________________________________")
    a=str(input("WHAT YOU WANT TO CALCULATE 'SIN','COS','TAN', ENTER HERE:>:"))
    if a=='si'or a=='SI'or a=='sin'or a=='SIN'or a=='S'or a=='s':
        a=str(input("WHAT YOU WANT SIN OUTPUT IN RADIANS OR DEGRESS ENTER HERE:>:"))
        if a == 'radians' or a == 'Radians' or a == 'R' or a == 'r' or a == 'RADIANS' or a == 'rad' or a == 'RAD':
            print("\t\t******************************************")
            print("\t\t-CHOISED IS 'SIN' OUTPUT IN RADIANS-")
            print("\t\t******************************************")
            a=str(input("WHAT YOU WANT 'PI' WITH OPEARTION -,+,//,* 'A,S,D,M' ENTER HERE:>:"))
            if a=='+'or a=='A'or a=='a'or a=='ADDITION'or a=='addition'or a=='ADD'or a=='add':
                print("\t\t**********************************************************")
                print("\t\t-CHOISED IS 'SIN' OUTPUT IN RADIANS WITH ADDITION-")
                print("\t\t**********************************************************")
                import math
                a=int(input("ENTER HERE 'SIN' VALUE :>:"))
                b=int(input("ENTER HERE 'ADDITION' VALUE:>:"))
                c=math.sin(math.radians(a+b))
                print("-------------------------------")
                print("CALCULATING RESULT ==> ",c)
                print("-------------------------------")
        elif a=='-'or a=='subtraction'or a=='SUBTRACTION'or a=='sub'or a=='SUB'or a=='s'or a=='S':
            print("\t\t**************************************")
            print("\t\t-CHOISED IS 'SIN' WITH SUBTRACTION-")
            print("\t\t**************************************")
            import math
            a=int(input("ENTER HERE 'PI' VALUE :>:"))
            b=int(input("ENTER HERE 'SUBTRACTION' VALUE:>:"))
            c=math.sin(math.radians(a-b))
            print("-------------------------------")
            print("CALCULATING RESULT ==> ",c)
            print("-------------------------------")
    elif a=='/'or a=='//'or a=='DIVISION'or a=='division'or a=='div'or a=='DIV'or a=='d'or a=='D':
        print("\t\t**********************************")
        print("\t\t-CHOISED IS 'PI' WITH DIVISION-")
        print("\t\t**********************************")
        import math
        a=int(input("ENTER HERE 'PI' VALUE :>:"))
        b=int(input("ENTER HERE 'DIVISION' VALUE:>:"))
        c=math.pi*a/b
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",c)
        print("-------------------------------")
    elif a=='*'or a=='MULTPLYCATION'or a=='multplycation'or a=='multply'or a=='MULTPLY'or a=='m'or a=='M':
        print("\t\t***************************************")
        print("\t\t-CHOISED IS 'PI' WITH MULTPLICATION-")
        print("\t\t***************************************")
        import math
        a=int(input("ENTER HERE 'PI' VALUE :>:"))
        b=int(input("ENTER HERE 'MULTPLY' VALUE:>:"))
        c=math.pi*a*b
        print("-------------------------------")
        print("CALCULATING RESULT ==> ",c)
        print("-------------------------------")
    else:
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!____")
        print("WRONG OPERATION IN PI WITH OPERATION")
        print("____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!____")