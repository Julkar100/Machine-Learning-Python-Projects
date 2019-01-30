print(" The cost of token :")
cost=int(input())
print("Cash Avaialabe right now :")
cash=int(input())
change=cash-cost
a2k=int(change/2000)
change=change%2000
a5h=int(change/500)
change=change%500
a1h=int(change/100)
change=change%100
a5t=int(change/50)
change=change%50
a1t=int(change/10)
change=change%10
print("\n\n\n\n")
print("2000 notes"+str(a2k))

print("500 notes"+str(a5h))

print("100 notes"+str(a1h))

print("50 notes"+str(a5t))

print("10 notes"+str(a1t))

print("1 Re Coins"+str(change))


