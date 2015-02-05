#!/usr/bin/env python3
import json 
from Installation import Installation as I

class Serializer(object):
    """
    Class used to serialize Installation/Equipement/Activity in different format
    """

    def unserialize_json(pathname):
        """
        Method used to convert json file to Installation array
        """
        with open(pathname) as json_file:
            json_data = json.load(json_file)
            collection = []
            for installation in json_data["data"]:
                collection.append(I(installation["insNom"], 
            
serializer.unserialize_json("../data/installation/installation.json")
