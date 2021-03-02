from Operations import Operations

class Main:
    """docstring for Main."""
    def __init__(self):
        pass

    def Menu(self):
        opcion = 0
        while opcion != 6:
            print('----- Menu -----')
            print('1. Cargar archivo de entrada' +
                  '\n2. Desplegar listas ordenadas' +
                  '\n3. Desplegar búsquedas' + 
                  '\n4. Desplegar todas' +
                  '\n5. Desplegar todas a archivo' + 
                  '\n6. Salir')
            print('Opcion: ', end='' )
            opcion = input()
            
            if opcion == '1':
                print('Cargando archivo...')
                upload = Operations()
                upload.generatePath()
                listOfListObject = Operations()
                listOfListObject.listOfList()
                listOfListObject.gettingSplit()
                listOfListObject.getSortedAndUnsorted()
                
                
                
                
                
                
            elif opcion == '2':
                print('Desplegando listas ordenadas')
                # upload = Operations()
                # upload.readFile()
            elif opcion == '3':
                print('Desplegando busquedas')
            elif opcion == '4':
                print('Desplegando todas')
            elif opcion == '5':
                print('Desplegar todas a archivo')
            else:
                print('Saliendo....')
                opcion = 6


inicio = Main()
inicio.Menu()
