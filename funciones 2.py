                                                                                                                                                                                                        
def registrar_consumo():
    print("Registro de consumo de café")
    print("---------------------------")
    
    jugador = input("Nombre del jugador: ")
    edad = input("Edad del jugador: ")
    while not validar_edad(edad):
        edad = input("error, ingrese nuevamente su edad: ")
        
    equipo = input("Equipo del jugador: ")
    viernes = input("Consumo de café el viernes: ")
    sabado = input("Consumo de café el sábado: ")
    domingo = input("Consumo de café el domingo: ")
    while not validar_consumo_minimo(viernes, sabado, domingo):
        print("El consumo total mínimo de café debe ser al menos 3 tazas en los 3 días.")
        viernes = input("Consumo de café el viernes: ")
        sabado = input("Consumo de café el sábado: ")
        domingo = input("Consumo de café el domingo: ")
    
    id_consumo = generar_id()
    
    input("\nRegistro guardado. Presione Enter para continuar.")

def listar_consumos():
    print("Listado de consumos de café")
    print("---------------------------")
    input("\nPresione Enter para continuar.")

def imprimir_hoja_consumo():
    print("Imprimir hoja de consumo por equipo")
    print("-----------------------------------")
    print("Equipos disponibles:")
    for idx, equipo in enumerate(equipo, start=1):
        print(f"{idx}. {equipo}")
    
    seleccion = input("\nSeleccione el número de equipo para generar el archivo CSV: ")
    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(equipo):
            equipo_seleccionado = equipo[seleccion - 1]

            print(f"Archivo CSV generado para {equipo_seleccionado}")
        else:
            print("Selección inválida.")
    except ValueError:
        print("Selección inválida.")

    input("\nPresione Enter para continuar.")

def buscar_consumo_por_id():
    print("Buscar consumo por ID")
    print("")
    id_buscar = input("Ingrese el ID del consumo a buscar: ")
    input("\nPresione Enter para continuar.")

def main():
    while True:
        print("Sistema de gestión de consumo de café - Hackaton")
        print("------------------------------------------------")
        print("1. Registrar consumo")
        print("2. Listar todos los consumos")
        print("3. Imprimir hoja de consumo por equipo")
        print("4. Buscar un consumo por ID")
        print("5. Salir del programa")
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            registrar_consumo()
        elif opcion == '2':
            listar_consumos()
        elif opcion == '3':
            imprimir_hoja_consumo()
        elif opcion == '4':
            buscar_consumo_por_id()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            input("opcion erronea, intentelo nuevamente.")

if __name__ == "__main__":
    main()
