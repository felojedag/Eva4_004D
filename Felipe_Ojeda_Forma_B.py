gestion_de_entradas=[
    {
        "nombre":"Juan",
        "tipo_de_entrada":"G",
        "codigo_de_confirmacion":"cod001"
}]


def mostrar_menú_opciones():
    print("Menú de gestión de entradas")
    print("1.- Comprar entradas")
    print("2.- Consultar comprador")
    print("3.- Cancelar compra")
    print("4.- Salir")

def validacion_codigo(codigo_de_confirmacion):
    if len(codigo_de_confirmacion)<6 or not codigo_de_confirmacion.isalnum():
        print("Código invalido")
        return False
    if any(e["codigo_de_confirmacion"].lower()==codigo_de_confirmacion.isalnum() for e in gestion_de_entradas):
            print("Este código de confirmación ya está en uso")
            return False
    return True
def comprar_entradas():
    nombre=input("Nombre de comprador: ".strip())
    if not nombre:
        print("Este campo no se puede dejar vacio")
        return
    if any(e["nombre"].lower().strip()==nombre.lower().strip() for e in gestion_de_entradas):
        print("Este nombre ya está en uso")
        return
    tipo_de_entrada=input("Tipo de entrada a comprar(G-V): ".strip().upper())
    if tipo_de_entrada not in("G","V","g","v"):
        print("El tipo de entrada a comprar ingresada es invalida")
        return
    codigo_de_confirmacion=input("Código de confirmación de entrada: ".strip())
    if not validacion_codigo(codigo_de_confirmacion):
        print("Código de confirmación invalido")
        return
    gestion_de_entradas.append({
        "nombre":nombre,
        "tipo_de_entrada":tipo_de_entrada,
        "codigo_de_confirmacion":codigo_de_confirmacion
    })
    print(f"{nombre} registrado exitosamente")
def consultar_entrada():
    nombre=input("Nombre de comprador: ".strip().lower())
    encontrado=[
        e for e in gestion_de_entradas
        if nombre in e["nombre"].lower()
    ]
    if not encontrado:
        print("El comprador no se encuentra")
    else:
        for e in gestion_de_entradas:
            print(f"Nombre de comprador: {e['nombre']} -Tipo de entrada: {e['tipo_de_entrada']} -Código de confirmación{e['codigo_de_confirmacion']}")
def cancelar_compra():
    nombre=input("Nombre de comprador para cancelar compra: ".strip().lower())
    for i,e in enumerate(gestion_de_entradas):
        if e["nombre"].lower().strip()==nombre.lower().strip():
            del gestion_de_entradas[i]
            print("¡Compra cancelada!")
            return
    else:
        print("No se pudo cancelar la compra")
            
def main():
    while True:
        mostrar_menú_opciones()
        try:
            opcion=int(input("Seleccionar una opción(1-4): "))
            if opcion==1:
                comprar_entradas()
            elif opcion==2:
                consultar_entrada()
            elif opcion==3:
                cancelar_compra()
            elif opcion==4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción valida!!")
        except ValueError:
            print("Debe ingresar una opción valida!!")

main()


