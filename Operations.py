from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


class Operations:
    
    def __init__(self):
        pass
    
    
    filename = ''
    
    def generatePath(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        global filename
        filename = ''
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        print('La ruta cargada fue')
        print(filename)
        
        operate = Operations()
        operate.readFile()
        
    
    global linesInList
    linesInList = []
    
    def readFile(self):
        a_file = open(filename, 'r')
        
        for line in a_file:
            linesInList.append(line)
        a_file.close()
        print('*****************************')
        print('Archivo cargado exitosamente!')
        print('*****************************')
        
        
        
    #---------
    global normalList
    normalList = []
    
    def listOfList(self):
        
        for i in range(len(linesInList)):
            normalList.append([linesInList[i]])
        print(normalList)

        #quitando el igual
        for i, x in enumerate(normalList):
            for j, a in enumerate(x):
                if "=" in a:
                    normalList[i][j] = a.replace('=', ' ')
        
        print(normalList)
        cleaningLists = Operations()
        cleaningLists.deletingEqual()
        cleaningLists.deletingDoubleComma()
        cleaningLists.deletingTripleComma()
        cleaningLists.deletingWhiteSpaces()
        cleaningLists.deletingLineJumps()
    
    def deletingEqual(self):
        for i, x in enumerate(normalList):
            for j, a in enumerate(x):
                if "   " in a:
                    normalList[i][j] = a.replace('   ', ' ')
        print(normalList)
    

    def deletingDoubleComma(self):
        for i, x in enumerate(normalList):
            for j, a in enumerate(x):
                if "  " in a:
                    normalList[i][j] = a.replace('  ', ' ')
        print(normalList) 

    def deletingTripleComma(self):
        for i, x in enumerate(normalList):
            for j, a in enumerate(x):
                if " " in a:
                    normalList[i][j] = a.replace(' ', ',')

    def deletingWhiteSpaces(self):
        for i, x in enumerate(normalList):
            for j, a in enumerate(x):
                if ",," in a:
                    normalList[i][j] = a.replace(',,', ',')

    def deletingLineJumps(self):
        for i, x in enumerate(normalList):
            for j, a in enumerate(x):
                if "\n" in a:
                    normalList[i][j] = a.replace('\n', '')

    global splitLists
    
    
    
    def gettingSplit(self):
        splitLists = list()
        for l in normalList:
            splitLists += [x.split(',') for x in l]
        
        print('----------------------------------------------------------------')
        print(splitLists)
        gettingRangeToFillNewListsObject = Operations()
        gettingRangeToFillNewListsObject.gettingRangeToFillNewLists(splitLists)
        

    global indexesToArrive
    indexesToArrive=[]
    
    def gettingRangeToFillNewLists(self, splitLists):        
         
        
        for splitList in splitLists:
            for item in splitList:
                if item == "ORDENAR" or item == "BUSCAR":
                    indexesToArrive.append(splitList.index(item))
                    break
        print('indexes ',indexesToArrive)
        gettingStringNumbersObject = Operations()
        gettingStringNumbersObject.gettingStringNumbers(splitLists)
    
    global listWithIndexesToArrive
    listWithIndexesToArrive = []
    
    def gettingStringNumbers(self, splitLists):
        
        castingOfDisorderNumbersObject = Operations()
        for i in range(len(splitLists)):
            listWithIndexesToArrive.append([])
            for x in range(1, indexesToArrive[i]): 
                listWithIndexesToArrive[i].append(splitLists[i][x])
        # return listWithIndexesToArrive 
        castingOfDisorderNumbersObject.castingOfDisorderNumbers(listWithIndexesToArrive, splitLists)
        
        
    
    
    global intDisorderList,disorderListToLookingFor
    intDisorderList = []
    disorderListToLookingFor = []
    
    def castingOfDisorderNumbers(self, listWithIndexesToArrive, splitLists):
        
        
        for i in range(0, len(listWithIndexesToArrive)):
            intDisorderList.append([int(x) for x in listWithIndexesToArrive[i]])
            
        for i in range(0, len(listWithIndexesToArrive)):
            disorderListToLookingFor.append([int(x) for x in listWithIndexesToArrive[i]])
        print('int desordenada',intDisorderList,' finally')
        gettingLinesToSortObject = Operations()
        gettingLinesToSortObject.gettingLinesToSort(splitLists)
    
    global booleansResults
    global linesToSort
    linesToSort = []
    
    def gettingLinesToSort(self, splitLists):
        lookingFor = 'ORDENAR'
        
        booleansResults = [any(lookingFor in string for string in sublist)
        for sublist in splitLists
        ]
        
        linesToSort = [i for i, x in enumerate(booleansResults) if x == True]
        print('lineas a ordenar',linesToSort)
        print('Valores Booleanos',booleansResults)
    #-----------------
    global sortedAndUnsorted
    sortedAndUnsorted = []
        
    def getSortedAndUnsorted(self):
        
        
        for i in range(len(intDisorderList)):
            sortedAndUnsorted.append(ordenamientoBurbuja(intDisorderList[i]))
        
        print(sortedAndUnsorted)
    #------------------
    def ordenamientoBurbuja(self, listForSort):#Ordenamiento burbuja el cual mando a llamar desde un metodo abajo
        for j in range(len(listForSort)):
            #initially swapped is false
            swapped = False
            i = 0
            while i<len(listForSort)-1:
                #comparing the adjacent elements
                if listForSort[i]>listForSort[i+1]:
                    #swapping
                    listForSort[i],listForSort[i+1] = listForSort[i+1],listForSort[i]
                    #Changing the value of swapped
                    swapped = True
                i = i+1
            #if swapped is false then the listForSortt is sorted
            #we can stop the loop
            if swapped == False:
                break
        
        return listForSort
    #---------------------
    
    
    






