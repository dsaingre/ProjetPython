class Equipment :
    ''' class representing an equipment
    has too many characteristics, 6 have been selected
    all of thems are Strings
    '''
    def __init__(self,comInsee,comLib,equipmentFile,equAnneeService,equNom,equNomBatiment):
        self.comInsee = comInsee
        self.comLib = comLib
        self.equipmentFile = equipmentFile
        self.equAnneeService = equAnneeService
        self.equNom = equNom
        self.equNomBatiment = equNomBatiment
        

    def __str__(self):
        return "EQUIPMENT [nom : "+self.equNom+", comLib : " + self.comLib + " , num INSEE : " + self.comInsee+" ]"