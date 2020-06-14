#PokemonXPCalc is a python program created by Camden Harper to calculate the xp need to get to the defined level.
#Erratic XP Group (n <= 50) Formula: N/A
#Erratic XP Group (50 <= n <= 68) Formula: N/A
#Erratic XP Group (68<= n <= 98) Formula: N/A
#Erratic XP Group (98 <= n <= 100) Formula: N/A
#Fast XP Group Formula: 4n^3 / 5.
#Medium Fast XP Group Formula: n^3.
#Medium Slow XP Group Formula: 6/5n^3 - 15n^2 + 100n - 140.
#Slow XP Group Formula: 5n^3 / 4.

wlv = 0
clv = 0
cxp1 = 0
cxp2 = 0
wxp = 0
test = "null"
xpgrp = 0

def erratic():
    try:
        wlv = int(input("Enter Wanted Level: "))
        clv = int(input("Enter Current Level: "))
        cxp1 = int(input("Enter Current XP: "))
        if clv <= 50:
            cxp2 = cxp1 + clv**3*(100-clv) / 50
        if clv >= 50 and clv <= 68:
            cxp2 = cxp1 + clv**2*(150-clv) / 100
        if clv >= 68 and clv <= 98:
            clv**3*(1911-10*clv/3) / 500
        if clv >= 98 and clv <= 100:
            clv**3*(160-clv) / 100

        if wlv <= 50:
            wxp = wlv**3*(100-wlv) / 50
        if wlv >= 50 and wlv <= 68:
            wlv**2*(150-wlv) / 100
        if wlv >= 68 and wlv <= 98:
            wlv**3*(1911-10*wlv/3) / 500
        if wlv >= 98 and wlv <= 100:
            wlv**3*(160-wlv) / 100

        print(cxp2)
        print(wxp - cxp2)
    except:
        pass

def fast():
    try:
        wlv = int(input("Enter Wanted Level: "))
        clv = int(input("Enter Current Level: "))
        cxp1 = int(input("Enter Current XP: "))
        cxp2 = cxp1 + (4 * ((clv**3) / 5))
        wxp = 4 * ((wlv**3) / 5)
        print(cxp2)
        print(wxp - cxp2)
    except:
        pass

def medium_fast():
    try:
        wlv = int(input("Enter Wanted Level: "))
        clv = int(input("Enter Current Level: "))
        cxp1 = int(input("Enter Current XP: "))
        cxp2 = cxp1 + clv**3
        wxp = wlv**3
        print(cxp2)
        print(wxp - cxp2)
    except:
        pass

def medium_slow():
    try:
        wlv = int(input("Enter Wanted Level: "))
        clv = int(input("Enter Current Level: "))
        cxp1 = int(input("Enter Current XP: "))
        cxp2 = cxp1 + 6/5*clv**3 - 15*clv**2 + 100*clv-140
        wxp = 6/5*wlv**3 - 15*wlv**2 + 100*wlv-140
        print(cxp2)
        print(wxp - cxp2)
    except:
        pass

def slow():
    try:
        wlv = int(input("Enter Wanted Level: "))
        clv = int(input("Enter Current Level: "))
        cxp1 = int(input("Enter Current XP: "))
        cxp2 = cxp1 + 5*clv**3 / 4
        wxp = 5*wlv**3 / 4
        print(cxp2)
        print(wxp - cxp2)
    except:
        pass

def main():
    print("(1) Erratic \n(2) Fast \n(3) Medium Fast \n(4) Medium Slow \n(5) Slow")
    xpgrp = int(input("Enter XP Group Number: "))
    if xpgrp == 1:
        print("The Erratic XP Group has not been implemented yet....sorry :(")
        #erratic()
    if xpgrp == 2:
        fast()
    if xpgrp == 3:
        medium_fast()
    if xpgrp == 4:
        medium_slow()
    if xpgrp == 5:
        slow()

main()