loan = float(input("How much is your initial investment?: "))
interest = float(input("Input interest rate: "))
years = 1
target = float(input("What is your target value?: "))
while loan <= target:
  loan += (loan*interest)
  print("Year", years, "is", round(loan,2))
  years += 1