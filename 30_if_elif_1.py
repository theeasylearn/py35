'''
write a program to accept day of week (1 to 7) from user. and display days and night choghadiya
7 Days Day Choghadia:
    Monday → Amrit, Kaal, Shubh, Rog, Udveg, Chaal, Laabh, Amrit
    Tuesday → Rog, Udveg, Chaal, Laabh, Amrit, Kaal, Shubh, Rog
    Wednesday → Laabh, Amrit, Kaal, Shubh, Rog, Udveg, Chaal, Laabh
    Thursday → Shubh, Rog, Udveg, Chaal, Laabh, Amrit, Kaal, Shubh
    Friday → Chaal, Laabh, Amrit, Kaal, Shubh, Rog, Udveg, Chaal
    Saturday → Kaal, Shubh, Rog, Udveg, Chaal, Laabh, Amrit, Kaal
    Sunday → Udveg, Chaal, Laabh, Amrit, Kaal, Shubh, Rog, Udveg
7 Days Night Choghadia:
    Monday → Rog, Kaal, Laabh, Udveg, Shubh, Amrit, Chaal, Rog
    Tuesday → Kaal, Laabh, Udveg, Shubh, Amrit, Chaal, Rog, Kaal
    Wednesday → Laabh, Udveg, Shubh, Amrit, Chaal, Rog, Kaal, Laabh
    Thursday → Udveg, Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg
    Friday → Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh
    Saturday → Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh, Amrit
    Sunday → Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh
'''
day = int(input("Enter week day as number between 1 to 7"))
if day==1: #== != < > <= >=
    print("Monday")
    print("_"*100)
    print("Days choghadliya : Amrit, Kaal, Shubh, Rog, Udveg, Chaal, Laabh, Amrit")
    print("Night choghadliya : Rog, Kaal, Laabh, Udveg, Shubh, Amrit, Chaal, Rog")
elif day==2:
    print("Tuesday")
    print("_"*100)
    print("Days choghadiya : Rog, Udveg, Chaal, Laabh, Amrit, Kaal, Shubh, Rog")
    print("Night choghadiya : Kaal, Laabh, Udveg, Shubh, Amrit, Chaal, Rog, Kaal")
elif day==3:
    print("Wednesday")
    print("_"*100)
    print("Days choghadiya : Laabh, Amrit, Kaal, Shubh, Rog, Udveg, Chaal, Laabh")
    print("Night choghadiya : Laabh, Udveg, Shubh, Amrit, Chaal, Rog, Kaal, Laabh")
elif day==4:
    print("Thursday")
    print("_"*100)
    print("Days choghadiya : Shubh, Rog, Udveg, Chaal, Laabh, Amrit, Kaal, Shubh")
    print("Night choghadiya : Udveg, Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg")
elif day==5:
    print("Friday")
    print("_"*100)
    print("Days choghadiya : Chaal, Laabh, Amrit, Kaal, Shubh, Rog, Udveg, Chaal")
    print("Night choghadiya : Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh")
elif day==6:
    print("Saturday")
    print("_"*100)
    print("Days choghadiya : Kaal, Shubh, Rog, Udveg, Chaal, Laabh, Amrit, Kaal")
    print("Night choghadiya : Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh, Amrit")
elif day==7:
    print("Sunday")
    print("_"*100)
    print("Days choghadiya : Udveg, Chaal, Laabh, Amrit, Kaal, Shubh, Rog, Udveg")
    print("Night choghadiya : Shubh, Amrit, Chaal, Rog, Kaal, Laabh, Udveg, Shubh")
else:
    print("it is not valid day of week")
    
print(""" Amrit → Very auspicious (best time)
Shubh → Good time
Laabh → Gain/profit (favorable)
Chaal (Char) → Neutral (okay for routine work)
Udveg → Stressful (avoid important work)
Rog → Illness (inauspicious)
Kaal → Very inauspicious (avoid completely)
Best Choghadia to Use
-----------------------
Amrit, Shubh, Laabh
-----------------------
Avoid
Kaal, Rog, Udveg""")