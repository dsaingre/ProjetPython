#!/usr/bin/env python3
"""
Author : Dimitri Saingre - IUT Nantes - Dpt Informatique
This class is used to represent an Installation
has 29 attributes 
"""
class Installation(object):

    def __init__(self, nameInstall, numInstall, nameTown, INSEECode, postalCode,
                 placeCalled, streetNum, streetName, longitude, 
                 latitude, noAccessArrang, accessLowMobHand, accessSensHand,
                 sizeInM2, caretakerAndHousing, multiTown, nbOfParkSpot, 
                 nbOfDisParkSpot, specifInstall, subwServic, busServic, 
                 tramServic, trainServic , boatServic, otherServic, nbOfSportEquip, 
                 nbOfEquipNoteCard, insDateUpd):
        """
        Constructor ; needs 29 arguments : 
        - nameInstall : String
        - numInstall : String
        - nameTown : String
        - INSEECode : String
        - postalCode : String
        - placeCalled : String
        - streetNum : String
        - streetName : String
        - longitude : float
        - latitude : float
        - noAccessArrang : String 
        - accessLowMobHand : String
        - accessSensHand : String
        - sizeInM2 : String
        - caretakerAndHousing : String
        - multiTown : String
        - nbOfParkSpot : String
        - nbOfDisParkSpot : String
        - SpecifInstall : String
        - subwServic : String
        - busServic : String
        - tramServic : String
        - trainServic : String
        - boatServic : String
        - otherServic : String
        - nbOfSportEquip : String
        - nbOfEquipNoteCard : String
        - insDateUpd : String
        """
        self.nameInstall = nameInstall
        self.numInstall = numInstall
        self.nameTown = nameTown
        self.INSEECode = INSEECode
        self.postalCode = postalCode
        self.placeCalled = placeCalled
        self.streetNum = streetNum 
        self.streetName = streetName
        self.longitude = longitude
        self.latitude = latitude
        self.noAccessArrang = noAccessArrang
        self.accessLowMobHand = accessLowMobHand
        self.accessSensHand = accessSensHand
        self.sizeInM2 = sizeInM2
        self.caretakerAndHousing = caretakerAndHousing
        self.multiTown = multiTown 
        self.nbOfParkSpot = nbOfParkSpot
        self.nbOfDisParkSpot = nbOfDiskParkSpot
        self.specifInstall = specifInstall
        self.subwServic = subwServic
        self.busServic = busServic 
        self.tramServic = tramServic
        self.trainServic = trainServic
        self.boatServic = boatServic
        self.otherServic = otherServic
        self.nbOfSportEquip = nbOfSportEquip
        self.nbOfEquipNoteCard = nbOfEquipNoteCard
        self.insDateUpd = insDateUpd

 	"GETTERS AND SETTERS"

	def getNameInstall(self, nameInstall):
            return self.nameInstall
	
	def setNameInstall(self, nameInstall):
            self.nameInstall = nameInstall

	def getNumInstall(self):
            return self.numInstall
	
	def setNumInstall(self, numInstall):
            self.numInstall = numInstall

	def getNameTown(self):
            return self.nameTown
	
	def setNameTown(self, nameTown):
            self.nameTown = nameTown

	def getINSEECode(self):
            return self.INSEECode
	
	def setINSEECode(self, INSEECode):
            self.INSEECode = INSEECode

	def getPostalCode(self):
            return self.postalCode
	
	def setPostalCode(self, postalCode):
            self.postalCode = postalCode

        def getPlaceCalled(self):
            return self.placeCalled
	
	def setPlaceCalled(self, placeCalled):
            self.placeCalled = placeCalled

	def getStreetNum(self):
            return self.streetNum
	
	def setStreetNum(self, streetNum):
            self.streetNum = streetNum

	def getStreetName(self):
            return self.streetName
	
	def setStreetName(self, streetName):
            self.StreetName = streetName

	def getLongitude(self):
            return self.longitude
	
	def setLongitude(self, longitude):
            self.longitude = logitude

	def getLatitude(self):
            return self.latitude
	
	def setLatitude(self, latitude):
            self.latitude = latitude

	def getNoAccessArrang(self):
            return self.noAccessArrang
	
	def setNoAccessArrang(self, noAccessArrang):
            self.noAccessArrang = noAccessArrang

	def getAccessLowMobHand(self):
            return self.accessLowMobHand
	
	def setAccessLowMobHand(self, accessLowMobHand):
            self.accessLowMobHand = accessLowMobHand

	def getAccessSensHand(self):
            return self.accessSensHand
	
	def setAccessSensHand(self, accessSensHand):
            self.accessSensHand = accessSensHand

	def getSizeInM2(self):
            return self.sizeInM2
	
	def setSizeInM2(self, sizeInM2):
            self.sizeInM2 = sizeInM2

	def getCareTakerAndHousing(self):
            return self.caretakerAndHousing
	
	def setCareTakerAndHousing(self, caretakerAndHousing):
            self.careTakerAndHousing = caretakerAndHousing

	def getMultiTown(self):
            return self.multiTown
	
	def setMultiTown(self, multiTown):
            self.multiTown = multiTown

	def getNbOfParkSpot(self):
            return self.nbOfParkSpot
	
	def setNbOfParkSpot(self, nbOfParkSpot):
            self.nbOfParkSpot = nbOfParkSport

	def getNbOfDiskParkSpot(self):
            return self.nbOfDiskParkSpot
	
	def setNbOfDiskParkSpot(self, nbOfDiskParkSpot):
            self.nbOfDiskParkSpot = nbOfDiskParkSpot

	def getSpecifInstall(self):
            return self.specifInstall
	
	def setSpecifInstall(self, specifInstall):
            self.specifInstall = specifInstall

	def getSubwServc(self):
            return self.subwServc
	
	def setSubwServic(self, subwServic):
            self.subwServic = subwServic

	def getBusServic(self):
            return self.busServic
	
	def setBusServic(self, busServic):
            self.busServic = busServic

	def getTralServic(self):
            return self.tramServic
	
	def setTramServic(self, tramServic):
            self.tramServic = tramServic

	def getTrainServic(self):
            return self.trainServic
	
	def setTrainServic(self, trainServic):
            self.trainServic = TrainServic

	def getBoatServic(self):
            return self.boatServic
	
	def setBoatServic(self, boatServic):
            self.boatServic = boatServic

	def getOtherServic(self):
            return self.otherServic
	
	def setOtherServic(self, otherServic):
            self.otherServic = otherServic

	def getNbOfSportEquip(self):
            return self.nbOfSportEquip
	
	def setNnOfSportEquip(self, nbOfSportEquip):
            self.nbOfSportEquip = nbOfSportEquip

	def getNbOfEquipNoteCard(self):
            return self.nbOfEquipNoteCard
	
	def setNbOfEquipNoteCard(self, nbOfEquipNoteCard):
            self.nbOfEquipNoteCard = nbOfEquipNoteCard

	def getInsDateUpd(self):
            return self.insDateUpd
	
	def setInsDateUpd(self, insDateUpd):
            self.insDateUpd = insDateUpd

