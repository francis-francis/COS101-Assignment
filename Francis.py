p =float(input("Enter initial principal:"))

r =float(input("Enter initial rate :"))

t =float(input("Enter number of times per time period "))

n =float(input("Enter number of time period elapsed:"))

SI = p *(1 + r * t)
CI = p *(1 +r/n) ** n * t
print("YUSUF AND SONS COMPANY")
print(f'simple intrest : {SI}')
print(f'Compound intrest : {CI}')
