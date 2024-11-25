articulos = {'Pan':1.40, 'Huevos':2.30, 'Cebolla':0.85, 'Aceite':4.35}
articulo = input('¿Qué articulo quieres? ').title()
unidades = float(input('¿Cuántas unidades? '))
if articulo in articulos:
    print(unidades, 'unidades de', articulo, 'valen', articulos[articulo]*unidades, '€')
else: 
    print("Lo siento, el articulo ", articulo, "no está disponible.")