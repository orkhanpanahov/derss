import math

# Verilmiş dəyərlər
x = 0.8
epsilon = 0.001

# Cəmi saxlamaq üçün dəyişən
P = 0
n = 1  # Başlayırıq -x ilə
term = -x  # İlk termin

while abs(term) >= epsilon:
    P += term
    n += 1
    term = -x**n / math.factorial(n)

# Nəticəni çap et
print(f"Ədədi cəmin təqribi qiyməti (ε = {epsilon} dəqiqliklə): {P:.5f}")
