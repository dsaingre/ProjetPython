#!/usr/bin/env python3

# Content :  Serializer.py 
# Class used to serialize or to unserialize data in different formats
# Author : Dimitri SAINGRE 

import json 
from bean.installation import Installation as Install
from bean.activity import Activity as Acty
from bean.equipment import Equipment as Equip


class Serializer(object):
    """
    Class used to serialize Installation/Equipement/Activity in different format
    """

    def __init__(self):
        """
        Constructor
        """
        self.collection = []


    def unserialize_json_installation(self, pathname):
        """
        Method used to convert json file to Installation array
        """
        try:
            with open(pathname) as json_file:
                json_data = json.load(json_file)
                for installation in json_data["data"]:
                    self.collection.append(Install(installation["InsNumeroInstall"],
                                                   installation["InsCodePostal"],
                                                   installation["ComLib"],
                                                   installation["InsNoVoie"],
                                                   installation["InsLibelleVoie"],
                                                   installation["Longitude"],
                                                   installation["Latitude"],
                                                   installation["InsAccessibiliteAucun"],
                                                   installation["InsAccessibiliteHandiMoteur"],
                                                   installation["InsAccessibiliteHandiSens"]))
        except FileNotFoundError as e:
            print("An error as occured ({}), nothing as been done".format(e))

    def unserialize_json_activity(self, pathname):
        """
        Method used to convert json file to Activity array
        """
        try:
            with open(pathname) as json_file:
                json_data = json.load(json_file)
                for activity in json_data["data"]:
                    self.collection.append(Acty(activity["ActCode"],
                                                activity["ActLib"],
                                                activity["EquipementId"]))
        except FileNotFoundError as e:
            print("An error as occured ({}), nothing as been done".format(e))


    def unserialize_json_equipment(self, pathname):
        """
        Method used to convert json file to Equipment array
        """
        try:
            with open(pathname) as json_file:
                json_data = json.load(json_file)
                for equipment in json_data["data"]:
                    self.collection.append(Equip(equipment["EquipementId"],
                                                 equipment["EquNom"].replace('"',"'"),
                                                 equipment["InsNumeroInstall"]))
        except FileNotFoundError as e:
            print("An error as occured ({}), nothing as been done".format(e))
