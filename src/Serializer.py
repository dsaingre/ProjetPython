#!/usr/bin/env python3
import json 
from Installation import Installation as Install

class Serializer(object):
    """
    Class used to serialize Installation/Equipement/Activity in different format
    """

    def __init__(self):
        self.collection = []


    def unserialize_json(self, pathname):
        """
        Method used to convert json file to Installation array
        """
        with open(pathname) as json_file:
            json_data = json.load(json_file)
            for installation in json_data["data"]:
                self.collection.append(Install(installation["ComLib"],
                                               installation["ComInsee"],
                                               installation["InsCodePostal"],
                                               installation["InsLieuDit"],
                                               installation["InsNoVoie"],
                                               installation["Longitude"],
                                               installation["Latitude"],
                                               installation["InsAccessibiliteAucun"],
                                               installation["InsAccessibiliteHandiMoteur"],
                                               installation["InsAccessibiliteHandiSens"],
                                               installation["InsEmpriseFonciere"],
                                               installation["InsGardiennee"],
                                               installation["InsMultiCommune"],
                                               installation["InsNbPlaceParking"],
                                               installation["InsNbPlaceParkingHandi"],
                                               installation["InsPartLibelle"],
                                               installation["InsTransportMetro"],
                                               installation["InsTransportBus"],
                                               installation["InsTransportTram"],
                                               installation["InsTransportTrain"],
                                               installation["InsTransportBateau"],
                                               installation["InsTransportAutre"],
                                               installation["Nb_Equipements"],
                                               installation["Nb_FicheEquipement"],
                                               installation["InsDateMaj"]))
                                

                                            
s = Serializer()
s.unserialize_json("../data/installation/installation.json")
for ins in s.collection:
    print(ins)

