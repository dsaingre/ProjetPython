# Content : Equipment.py
# Class used to represent an equipment
# Author : Dimitri SAINGRE


class Equipment :
    ''' 
    This class is used to represent an equipment
    '''
    def __init__(self, eq_num, eq_name, install_num):
        """
        Constructor with 3 parameters
        """
        self.eq_num = eq_num
        self.eq_name = eq_name
        self.install_num = install_num

    def __str__(self):
        return "Equipment num :"+self.eq_number
