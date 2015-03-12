import sqlite3

class Database:

    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def creation_table_installation(self):
        #Create table
        self.c.execute('''CREATE TABLE Installation (nameTown text, INSEECode text,
        postalCode text, placeCalled text, streetNum text, longitude real, 
        latitude real, noAccessArrang text, accessLowMobHand text, accessSensHand text,
        sizeInM2 text, caretakerAndHousing text, multiTown text, nbOfParkSpot text, 
        nbOfDisParkSpot text, specifInstall text, subwServic text, busServic text, 
        tramServic text, trainServic text, boatServic text, otherServic text, 
        nbOfSportEquip text, nbOfEquipNoteCard text, insDateUpd text)''')
        self.conn.commit()
    
    def creation_table_activity(self):
        self.c.execute('''CREATE TABLE Activity (INSEECode text ,nameTown text,
        equipementId text,nbOfIdenticalEquip text, actCode text,actName text, 
        equActivityPraticable text,equActivityPratised text, equActivitySpeCenter text,
        actLvl text)''')
        self.conn.commit()

    def creation_table_equipment(self):
        self.c.execute('''CREATE TABLE Equipment(comInsee text, comLib text,equipmentFile text,equAnneeService text,
        equNom text , equNomBatiment text)''')
        self.conn.commit()

    def insertion_installation(self, inst):
        self.c.execute('''INSERT INTO Installation VALUES(\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",
        \"{5}\",\"{6}\",\"{7}\",\"{8}\",\"{9}\",\"{10}\",\"{11}\",\"{12}\",\"{13}\",\"{14}\",\"{15}\",\"{16}\",\"{17}\",\"{18}\",\"{19}\",
        \"{20}\",\"{21}\",\"{22}\",\"{23}\",\"{24}\")'''.format(inst.nameTown, 
                                                                inst.INSEECode,
                                                                inst.postalCode, 
                                                                inst.placeCalled, 
                                                                inst.streetNum, 
                                                                inst.longitude, 
                                                                inst.latitude, 
                                                                inst.noAccessArrang, 
                                                                inst.accessLowMobHand, 
                                                                inst.accessSensHand,
                                                                inst.sizeInM2, 
                                                                inst.caretakerAndHousing, 
                                                                inst.multiTown, 
                                                                inst.nbOfParkSpot, 
                                                                inst.nbOfDisParkSpot, 
                                                                inst.specifInstall, 
                                                                inst.subwServic, 
                                                                inst.busServic, 
                                                                inst.tramServic, 
                                                                inst.trainServic, 
                                                                inst.boatServic, 
                                                                inst.otherServic, 
                                                                inst.nbOfSportEquip, 
                                                                inst.nbOfEquipNoteCard, 
                                                                inst.insDateUpd))
        self.conn.commit()

    def insertion_activity(self, act):
        self.c.execute('''INSERT INTO Activity VALUES(\"{0}\",\"{1}\",\"{2}\",\"{3}\",
        \"{4}\",\"{5}\",\"{6}\",\"{7}\",\"{8}\",\"{9}\")'''.format(act.INSEECode, 
                                                                   act.nameTown,
                                                                   act.equipementId, 
                                                                   act.nbOfIdenticalEquip,
                                                                   act.actCode,
                                                                   act.actName,
                                                                   act.equActivityPraticable,
                                                                   act.equActivityPratised,
                                                                   act.equActivitySpeCenter,
                                                                   act.actLvl))

    def insertion_equipment(self, equ):
        self.c.execute('''INSERT INTO Equipment VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", 
        \"{4}\", \"{5}\")'''.format(equ.comInsee,
                                    equ.comLib,
                                    equ.equipmentFile,
                                    equ.equAnneeService,
                                    equ.equNom,
                                    equ.equNomBatiment))
        self.conn.commit()


    

        




