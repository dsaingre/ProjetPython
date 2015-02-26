import sqlite3

class DataBase(object):

    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.c = conn.cursor()

    def disconnect(self):
        self.conn.close()

    def creationTableInstallation(self):
        #Create table
        self.c.execute('''CREATE TABLE Installation (nameTown text, INSEECode text,
        postalCode text, placeCalled text, streetNum text, longitude real, 
        latitude real, noAccessArrang text, accessLowMobHand text, accessSensHand text,
        sizeInM2 text, caretakerAndHousing text, multiTown text, nbOfParkSpot text, 
        nbOfDisParkSpot text, specifInstall text, subwServic text, busServic text, 
        tramServic text, trainServic text, boatServic text, otherServic text, 
        nbOfSportEquip text, nbOfEquipNoteCard text, insDateUpd text)''')
        
        self.conn.commit()

    def insertionInstallation(self, install):
        self.c.execute('''INSERT INTO Installation VALUES({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10})''')
        




