#!/usr/bin/env python3

# Content : Installation.py
# Class used to represent an installation 
# Author : Dimitri SAINGRE

class Installation(object):
    """
    This class is used to represent an Installation
    """
    def __init__(self, install_num, postal_code="", town_name="", street_num="", 
                 street_name="", longitude="", latitude="", no_access_arrang="", 
                 access_low_mob_hand="", access_sens_hand=""):
        """
        Constructor with 11 parameters
        """
        self.install_num = install_num
        try:
            self.address = self.constr_address([street_num,street_name,postal_code,town_name])
        except TypeError as e:
            self.address = ""
            print("An error as occured ({}), address value has been set to \"\"".format(e))
        self.longitude = longitude
        self.latitude = latitude
        self.no_access_arrang = no_access_arrang
        self.access_low_mob_hand = access_low_mob_hand
        self.access_sens_hand = access_sens_hand

    def constr_address(self,array):
        """
        Method used for the construction of an adress (string) from an array which contain all adress elements
        return a string containing the adress
        """
        return " ".join(list(filter(lambda x: x != None, array)))

    def __str__(self):
        return "Installation num : "+self.install_num
