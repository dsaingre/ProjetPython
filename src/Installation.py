#!/usr/bin/env python3
"""
Author : Dimitri Saingre - IUT Nantes - Dpt Informatique
This class is used to represent an Installation
has 29 attributes 
"""
class Installation(object):

    def __init__(self, nameInstall, numInstall, nameTown, INSEECode, postalCode,
                 placeCalled, streetNum, streetName, location, longitude, 
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
        - location : GEO_Location
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
        self.location = location
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
        self.trainServic = train
        self.boatServic = boadServic
        self.otherServic = otherServic
        self.nbOfSportEquip = nbOfSportEquip
        self.nbOfEquipNoteCard = nbOfEquipNoteCard
        self.insDateUpd = insDateUpd

        
        

        
                 
