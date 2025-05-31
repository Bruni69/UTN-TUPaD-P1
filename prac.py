#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.

def palindromo(palabra):
    if len(palabra) <= 1:
        return "true"
    else:
        palabra_min=palabra.lower()
        if palabra[0] != palabra[-1]:
            return false
        return palabra_min(s[1:-1])
print(palindromo)
palabra="madaM"