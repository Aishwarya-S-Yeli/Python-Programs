Principle = float(input("Enter Principle:"))
Rate = float(input("Enter Rate:"))
Time = float(input("Enter Time(n Years):"))
Simple_interest = (Principle * Rate * Time) / 100
Amount = Principle * (pow((1 + Rate / 100), Time)) 
Compound_interest = Amount - Principle 
print("Simple Interest:", Simple_interest)
print("Compound Interest:", Compound_interest) 
