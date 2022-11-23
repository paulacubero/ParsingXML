from bs4 import BeautifulSoup

# muestra la descripción de todos los poductos por consola. No de uno solo
# archivo xml de referencia en el siguiente enlace
# https://gist.github.com/Fhernd/6f2aa7527a682f76c165b91fe0e989ee
# Al Café negro le añadimos el precio 9.95


with open('CatalagoProductos.xml') as f:
    data=f.read()
#print(data)

descripcion=BeautifulSoup(data, 'xml')
#print(descripcion)

poductos=descripcion.find_all('poductos')
#print(poductos)

b_name = descripcion.find('Producto', {'ID':'100001'})
#print(b_name)

for tag in descripcion.find_all('Producto', {'ID':'100001'}):
    tag['precio'] = "9.95"
print(descripcion.prettify())


