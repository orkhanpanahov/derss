def ededi_orta(A):
    if len(A) == 0:
        return None 
    return sum(A) / len(A)


A = [4, 8, 15, 16, 23, 42]


orta = ededi_orta(A)
print("Ədədi orta:", orta)
