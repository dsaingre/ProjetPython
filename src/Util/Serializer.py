#!/usr/bin/env python3
import json 
from Installation import Installation as Install
from Activity import Activity as Acty
from Equipment import Equipment as Equip

class Serializer(object):
    """
    Class used to serialize Installation/Equipement/Activity in different format
    """

    def __init__(self):
        self.collection = []


    def unserialize_json_installation(self, pathname):
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

    def unserialize_json_activity(self, pathname):
        """
        Method used to convert json file to Activity array
        """
        with open(pathname) as json_file:
            json_data = json.load(json_file)
            for activity in json_data["data"]:
                self.collection.append(Acty(activity["ComInsee"],
                                            activity["ComLib"],
                                            activity["EquipementId"],
                                            activity["EquNbEquIdentique"],
                                            activity["ActCode"],
                                            activity["ActLib"],
                                            activity["EquActivitePraticable"],
                                            activity["EquActivitePratique"],
                                            activity["EquActiviteSalleSpe"],
                                            activity["ActNivLib"]))


    def unserialize_json_equipment(self, pathname):
        """
        Method used to convert json file to Equipment array
        """
        with open(pathname) as json_file:
            json_data = json.load(json_file)
            for equipment in json_data["data"]:
                self.collection.append(Equip(equipment["ComInsee"],
                                             equipment["ComLib"],
                                             equipment["EquipementFiche"],
                                             equipment["EquAnneeService"],
                                             equipment["EquNom"].replace('"',"'"),
                                             equipment["EquNomBatiment"]))

                                            

