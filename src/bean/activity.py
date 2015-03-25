# Content : Activity.py
# Class used to represent an activity
# Author : Dimitri SAINGRE

class Activity:
    """
    This class is used to represent an activity
    """
    def __init__(self,act_code, act_name, eq_num):
        """
        Constructor with 3 parameters
        """
        self.act_code = act_code
        self.act_name = act_name
        self.eq_num = eq_num

    def __str__(self):
        return "Activity num : "+self.act_code
