p=input('Digite e descubra: ')
print(type(p))
print(f'{p} é um número?', p.isnumeric())
print(f'{p} tem letras e/ou numeros?', p.isalnum())
print(f'{p} tem somente letras?', p.isalpha())
print(f'{p} está em maiúsculo?', p.isupper())
print(f'{p} está em minúsculo?', p.islower())
print(f'{p} está capitalizada?', p.istitle())



