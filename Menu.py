from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

import webbrowser

def Menu():
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
                generatePath()
                castingOfDisorderNumbers()
            elif opcion == '2':
                print('Desplegando listas ordenadas')
                printSortedLists()
            elif opcion == '3':
                print('Desplegando busquedas')
                printSearchedItems()
            elif opcion == '4':
                print('Desplegando todas')
                printSortedLists()
                
                printSearchedItems()
            elif opcion == '5':
                print('Desplegar todas a archivo')
                webbrowser.open('Reporte.html', new=2)
            else:
                print('Saliendo....')
                opcion = 6

filename = ''
    
def generatePath():
    Tk().withdraw()
    global filename
    filename = ''
    filename = askopenfilename()
    # print('La ruta cargada fue')
    # print(filename)
        
    readFile()
    listOfList()
        
    
global linesInList
linesInList = []
    
def readFile():
    a_file = open(filename, 'r')
        
    for line in a_file:
        linesInList.append(line)
    a_file.close()
    print('-----------------------------')
    print('Archivo cargado exitosamente!')
    print('-----------------------------')

global normalList
normalList = []

def listOfList():
        
    for i in range(len(linesInList)):
        normalList.append([linesInList[i]])
    # print(normalList)

        #quitando el igual
    for i, x in enumerate(normalList):
        for j, a in enumerate(x):
            if "=" in a:
                normalList[i][j] = a.replace('=', ' ')
        
    # print(normalList)
    
    deletingEqual()
    deletingDoubleComma()
    deletingTripleComma()
    deletingWhiteSpaces()
    deletingLineJumps()
    
def deletingEqual():
    for i, x in enumerate(normalList):
            for j, a in enumerate(x):
                if "   " in a:
                    normalList[i][j] = a.replace('   ', ' ')
    # print(normalList)        

def deletingDoubleComma():
    for i, x in enumerate(normalList):
        for j, a in enumerate(x):
            if "  " in a:
                normalList[i][j] = a.replace('  ', ' ')
    # print(normalList)

def deletingTripleComma():
    for i, x in enumerate(normalList):
        for j, a in enumerate(x):
            if " " in a:
                normalList[i][j] = a.replace(' ', ',')

def deletingWhiteSpaces():
    for i, x in enumerate(normalList):
        for j, a in enumerate(x):
            if ",," in a:
                normalList[i][j] = a.replace(',,', ',')    

def deletingLineJumps():
    for i, x in enumerate(normalList):
        for j, a in enumerate(x):
            if "\n" in a:
                normalList[i][j] = a.replace('\n', '')   
    # print('viendo si llega aqui')
    gettingSplit()
#-------------------------------------------



def gettingSplit():
    global splitLists
    splitLists = list()
    
    for l in normalList:
        splitLists += [x.split(',') for x in l]
        
    # print('----------------------------------------------------------------')
    # print(splitLists)
    gettingRangeToFillNewLists(splitLists)       




global indexesToArrive
indexesToArrive=[]

def gettingRangeToFillNewLists(splitLists):        

    for splitList in splitLists:
        for item in splitList:
            if item == "ORDENAR" or item == "BUSCAR":
                indexesToArrive.append(splitList.index(item))
                break
    # print('indexes ',indexesToArrive)
    gettingStringNumbers()
    # print('tiene que haber algo aqui')

    
global listWithIndexesToArrive
listWithIndexesToArrive = []
    
def gettingStringNumbers():
    for i in range(len(splitLists)):
        listWithIndexesToArrive.append([])
        for x in range(1, indexesToArrive[i]): 
                listWithIndexesToArrive[i].append(splitLists[i][x])
    # return listWithIndexesToArrive 
#----------------
global intDisorderList,disorderListToLookingFor
intDisorderList = []
disorderListToLookingFor = []

def castingOfDisorderNumbers():
        
        
    for i in range(0, len(listWithIndexesToArrive)):
        intDisorderList.append([int(x) for x in listWithIndexesToArrive[i]])
            
    for i in range(0, len(listWithIndexesToArrive)):
        disorderListToLookingFor.append([int(x) for x in listWithIndexesToArrive[i]])
    # print('int desordenada',intDisorderList,' finally')
    gettingLinesToSort()
#------------------------
global booleansResults


def gettingLinesToSort():
    lookingFor = 'ORDENAR'
    global linesToSort
    linesToSort = []
    booleansResults = [any(lookingFor in string for string in sublist)
    for sublist in splitLists
        ]
        
    linesToSort = [i for i, x in enumerate(booleansResults) if x == True]
    # print('lineas a ordenar',linesToSort)
    # print('Valores Booleanos',booleansResults)
    getSortedAndUnsorted()
#----------------------
def bubbleSort(listForSort):#Ordenamiento burbuja el cual mando a llamar desde un metodo abajo
    for j in range(len(listForSort)):
        swapped = False
        i = 0
        while i<len(listForSort)-1:
            if listForSort[i]>listForSort[i+1]:
                listForSort[i],listForSort[i+1] = listForSort[i+1],listForSort[i]
                swapped = True
            i = i+1
        if swapped == False:
            break
        
    return listForSort
#-----------------
global sortedAndUnsorted
sortedAndUnsorted = []

def getSortedAndUnsorted():
    for i in range(len(intDisorderList)):
        sortedAndUnsorted.append(bubbleSort(intDisorderList[i]))
        
    # print(sortedAndUnsorted)

def printSortedLists():#Este metodo hay que mandarlo a llamar en la parte de "Mostrar listas ordenadas"
    global linesToReport
    linesToReport = []
    
    print('-----------------------------------------------------------------------------------------')
    for i in range(len(linesToSort)):
        print(splitLists[linesToSort[i]][0],':',', '.join(map(str,sortedAndUnsorted[i])))
    print('-----------------------------------------------------------------------------------------')
    
    for i in range(len(linesToSort)):
        linesToReport+=[(splitLists[linesToSort[i]][0],':',', '.join(map(str,sortedAndUnsorted[i])))]
    gettingLinesToSearch()
#---------------
def gettingLinesToSearch():#funcion que obtiene cuales tienen la palabra ordenar y obtiene los indices de las sublistas
    word = 'BUSCAR'
    global booleansResults2
    booleansResults2 = [any(word in string for string in sublist)
    for sublist in splitLists
    ]
    
    
    global linesToSearch
    linesToSearch = []
    linesToSearch = [i for i, x in enumerate(booleansResults2) if x == True]
    # print('Filas',linesToSearch)
    # print(booleansResults2)
    gettingIndexOfNumbersToSearch(splitLists)
#-------------------------------
def gettingIndexOfNumbersToSearch(splitLists):
    global indexOfNumbersToSearch
    indexOfNumbersToSearch=[]
    
    for splitList in splitLists:
        for item in splitList:
            if item=="BUSCAR":
                indexOfNumbersToSearch.append(splitList.index(item)+1)
    # print('Index Numbers ',indexOfNumbersToSearch)
    gettingNumbersAndCast()
#---------------
def gettingNumbersAndCast():
    global stringNumbersToSearch
    stringNumbersToSearch = []
    for i in range(len(linesToSearch)):
        stringNumbersToSearch.append(splitLists[linesToSearch[i]][indexOfNumbersToSearch[i]])
    
    # print(len(splitLists))
    global intNumbersToSearch
    intNumbersToSearch = [int(x) for x in stringNumbersToSearch]
    
    # print('Numeros a buscar',intNumbersToSearch)
    lookingForNumbersIndex()
#-----------------------------------------------
def lookingForNumbersIndex():
    global searchedItem
    searchedItem = []
    for i in range(len(linesToSearch)):
        searchedItem.append([])
        found = False
        for j in range(len(disorderListToLookingFor[linesToSearch[i]])):
            if intNumbersToSearch[i] == disorderListToLookingFor[linesToSearch[i]][j]:
                searchedItem[i].append(j+1)
                found = True
        if not found:
            searchedItem[i].append("NO ENCONTRADO")
    # print(searchedItem)
#------------------------------------------------
def printSearchedItems():
    print('-----------------------------------------------------------------------------------------')
    for i in range(len(linesToSearch)):
        print('BUSCAR',intNumbersToSearch[i],'EN',splitLists[linesToSearch[i]][0],':',', '.join(map(str, searchedItem[i])))
    print('-----------------------------------------------------------------------------------------')
    
    global forReports
    forReports = []
    for i in range(len(linesToSearch)):
        forReports += [(['BUSCAR',intNumbersToSearch[i],'EN',splitLists[linesToSearch[i]][0],':',', '.join(map(str, searchedItem[i]))])]
    # print('--------------------------------------------')
    # print(forReports)
    reportingFiles(forReports)
    
    

def reportingFiles(forReports):
    with open('Reporte.html', 'w') as report:
        report.write('<!DOCTYPE html>')
        report.write('<html lang="en">')
        report.write('<head>')
        
        report.write('<meta charset="UTF-8">')
        report.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
        report.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
        report.write('<title>Reporte de datots</title>')
        
        report.write('<head>')
        report.write('<body bgcolor="turquoise">')
        report.write('<h1 align="center">Reporte de datos</h1>')
        report.write('<hr>')
        report.write('<hr>')
        report.write('<table>')
        
        report.write('<h2 style="color:#0946D9";>Listas a ordenar')
        
        for lineToReport in linesToReport:
            report.write(f'<tr><td>{lineToReport}</td></tr>') 
        
        report.write('</table>')
        
        
        report.write('<hr>')
        #---------------------------------------------------------
        
        report.write('<table>')
        
        report.write('<h2 style="color:#0946D9";>Busqueda de datos')
        
        for forReport in forReports:
            report.write(f'<tr><td>{forReport}</td></tr>') 
        
        report.write('</table>')
        
        
        report.write('</body>')
        report.write('</html>')








Menu()
