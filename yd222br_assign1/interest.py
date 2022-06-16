S=int(input("Initial savings:"))
P=int(input("in percentages:"))
S2=round((S*(1+P/100)**5))
print("The value of your savings after 5 years is: ", S2)