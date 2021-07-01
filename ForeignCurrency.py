#!/usr/bin/env python3
#Foreign Currency
#KBowen
import locale
gblmoney = [0.0, 0.0, 0.0, 0.0, 0.0] #keep
ctry = ["Euros (EUR)", "British Pounds (GBP)", "Yen (YEN)", "Hockey Money (CAD)", "Rubles (RUB)"] #keep

def doValuation():
    global ctry, gblmoney
    qty = 0
    cval = 0.0
    grandtotal = 0.0
    totcunits = [0, 0, 0, 0, 0] #list of 5 values
    totcval = [0.0, 0.0, 0.0, 0.0, 0.0]

    choice = getChoice()
    while choice!=0:
        if choice!=9:
            qty = getQty(ctry[choice-1])
            cval = qty * gblmoney[choice-1]
            totcunits[choice-1] = totcunits[choice-1] + qty
            totcval[choice-1] = totcval[choice-1] + cval
            grandtotal += cval
            print(ctry[choice-1] + " has a value of %s " %locale.currency(cval,grouping=True))
        elif choice ==9:
            getRates()
        else:
            print("Unknown entry: How did we get here?")
        print()
        choice = getChoice()

    print("Purchase Summary: ")
    for i in range(0,5):
        print (ctry[i] + ": " + str(totcunits[i]) + " units for a value of: %s" %locale.currency(totcval[i],grouping=True))
    print("Today's grand total is %s: "%locale.currency(grandtotal,grouping=True))
            
def getChoice():
        choice = -1
        while (choice < 0 or (choice > 5 and choice !=9)):
            try:
                choice = int(input("Select currency for valuation (1=EUR, 2=GBP, 3=JPY, 4=CAD, 5=RUB, 9=New Rates, 0=Quit): "))
                if (choice < 0 or (choice > 5 and choice !=9)):
                    print("Unknown operation: 1-5, 9 or 0 only")
                
            except ValueError:
                print("Illegal input, integers 0-5 or 0 only")
        return choice

def getQty(prompt):
    sentinel = -1
    while sentinel < 0:
        try:
            sentinel = int(input("How many " +prompt + " are you buying?: "))
            if(sentinel<=0):
                print("Positive values only.")
        except ValueError:
            print("Illegal Entry: Postive numbers only please.")
    return sentinel
            
def getRates():
    global gblmoney, ctry
    print("Please enter the currency rate per US $ for the following currencies\n")
    for i in range(0,5):
        gblmoney[i] = getOneRate(ctry[i])
    
    

def getOneRate(prompt):
    sentinel = -1
    while sentinel < 0:
        try:
            sentinel = float(input(prompt + ": "))
            if(sentinel<=0):
                print("Positive values only.")
        except ValueError:
            print("Illegal Entry: Postive numbers only please.")
    return sentinel
    
def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print("Welcome to the Currency Calculator")
    print()
    getRates()
    doValuation()
    print("Thanks for using the calculator")
    
if __name__ == "__main__":
    main()
