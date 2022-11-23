from bs4 import BeautifulSoup

# 1º
with open('Clientes.xml') as f:
    data=f.read()
print(data)

#2º

Bs_data=BeautifulSoup(data, 'xml')
print(Bs_data)

