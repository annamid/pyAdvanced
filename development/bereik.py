class MijnClass :

    varOpenbaar = "dit is openbaar toegankelijk"
    __varPrive = "deze is privé"
    
    #ik mag er wel bij van binnenuit
    def Voorbeeld (self) :
        print( self.__varPrive)

        waardeA = "Tijdelijk"
        print("waardeA is:", waardeA)
        #vanaf dit punt stopt de functie en betsaad waardeA niet meer

    def AndereFunctie(self) :
        #waardeA bestaad ALLEEN binnen functie "voorbeeld"
        #print( waardeA ) > geeft error

        #vanaf dit punt voeg ik een nieuwe variable toe aan de instantie van deze class
        self.nieuweVariable = "deze variable is nieuw"


InstClass = MijnClass()
print( InstClass.varOpenbaar ) 
InstClass.varOpenbaar = "veranderd"

#mag er niet bij van buitenaf:
#print( instClass.__varPrive)

InstClass.Voorbeeld()
InstClass.AndereFunctie()

#vanaf dit punt bestaad "instClass.nieuweVariable" wel
print( "bestaat de variable 'nieuweVariable' al?", InstClass.nieuweVariable )