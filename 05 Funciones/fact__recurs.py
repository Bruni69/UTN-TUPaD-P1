def fact_recur(a):
    if a == 0:
        return 1
    else:
        return a*fact_recur(a-1)
                                
a=int(input("elija un numero: "))
print(f"el factorial de {a} es: {fact_recur(a)}")
