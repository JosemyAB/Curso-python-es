print("Datos persona 1")

nombreP1 = input("Nombre primera persona:")
edadP1 = int(input("Edad primera persona:"))
nombreP2 = input("Nombre primera persona:")
edadP2 = int(input("Edad primera persona:"))

BONIFICACION=20

edad_total = edadP1 + edadP2;

print(edad_total)
texto = "La persona 1 ({0}) tiene {1} años"
print(texto.format(nombreP1, edadP1))