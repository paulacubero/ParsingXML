from bs4 import BeautifulSoup


# 1º
with open('Clientes.xml') as f:
    data=f.read()
#print(data)

#2º

Bs_data=BeautifulSoup(data, 'xml')
#print(Bs_data)

#3º
telefonos=Bs_data.find_all('telefono')
#print(telefonos)

#4º
b_name = Bs_data.find('cliente', {'ID':'C001'})
#print(b_name)

#5º
for tag in Bs_data.find_all('cliente', {'ID':'C001'}):
    tag['ciudad'] = "Madrid"

print(Bs_data.prettify())