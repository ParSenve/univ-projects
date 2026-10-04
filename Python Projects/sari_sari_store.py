#Running total 
total_price=0

print("Theodore Skye G. Demonteverde | INF26B | Introduction To Computing FINAL Project")
print("=-=MAWARI-TAI! Sari-Sari Store!=-=")
#Loop for price input, ends when 0 is input
while True:
    item_price = int(input("Enter item price: ₱"))
    if item_price==0:
        break
    elif item_price<0:
        print("Please enter a positive number!")
        continue
    else:
        total_price=total_price+item_price
        print("Item added! Total is now ₱", total_price, "| Input '0' to continue to payment.")
        continue

#Prints the subtotal
print("\n Your subtotal is: ", total_price, "\n=-=-=-=-=-=-=-=-=-=-=")
#Checks if the subtotal is 200 or more and applies a discount, nothing happens if it isn't
if total_price >= 200:
    total_price=total_price-(total_price*0.05)
    print("You have reached the minimum threshold for a discount! \n Your discounted total is now: ", +total_price)

#Loop for cash, keeps going if under the total, if equal or more than total, calculates change if any
while True:
    user_cash = int(input("Input Cash: ₱"))
    if user_cash<total_price:
        print("Insufficient Cash!")
        continue
    else:
        user_change=user_cash-total_price
        break
#Prints user receipt
print("\n==User Receipt==")
print("Subtotal: ₱",total_price)
print("Cash Given: ₱", user_cash)
print("Change: ₱",user_change)
print("-=-=-=-=-=-=-=-=-=-=-=-=- \nThank you for shopping at MAWARI-TAI!") 

'''
START
SET total_price as '0'
REPEAT until user enters '0'
    INPUT item_price
    IF item_price is '0', STOP 
    ELSE IF item_price < 0
        DISPLAY "Please enter a positive number!"
    ELSE
        total_price=total_price+item_price
        DISPLAY "Item added! Total is now ₱" AND total_price
    ENDIF
DISPLAY total_price
IF total_price >= 200
    total_price=total_price-(total_price*0.05)
    DISPLAY "You have reached the minimum threshold for a discount!" AND total_price
    REPEAT
        INPUT user_cash
        IF user_cash<total_price
            DISPLAY "Insufficient Cash!"
        ELSE 
            user_change=user_cash-total_price
            STOP loop
        ENDIF
DISPLAY total_price
DISPLAY user_price
DISPLAY user_change
DISPLAY "Thank you for shopping!"
END
'''