import math


x = 0.5
epsilon = 0.001


sin_x = math.sin(x)
n = 1
term = sin_x 
P = 0


while abs(term) >= epsilon:
    P += term
    n += 1
    term = ((-1) ** (n + 1)) * (sin_x ** n) / math.factorial(n)


print(f"Cəmin təqribi qiyməti (ε = {epsilon} dəqiqliklə): {P:.5f}")
