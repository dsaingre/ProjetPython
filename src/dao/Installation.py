#!/usr/bin/env python3

# Content : Installation.py
# Class used to represent an installation 
# Author : Dimitri SAINGRE

class Installation(object):
    """
    This class is used to represent an Installation
    """
    def __init__(self, install_num, install_name, postal_code, town_name, street_num, 
                 street_name, longitude, latitude, no_access_arrang, 
                 access_low_mob_hand, access_sens_hand):
        """
        Constructor with 11 parameters
        """
        self.install_num = install_num
        self.install_name = install_name
        self.postal_code = postal_code
        self.town_name = town_name
        self.street_num = street_num
        self.street_name = street_name
        self.longitude = longitude
        self.latitude = latitude
        self.no_access_arrang = no_access_arrang
        self.access_low_mob_hand = access_low_mob_hand
        self.access_sens_hand = access_sens_hand

    def __str__(self):
        return "Installation num : "+self.install_num
