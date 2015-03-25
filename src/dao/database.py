# Content : Database.py
# Class used to manipulate the database (table creation, insertion .. )
# Author : Dimitri SAINGRE


import sqlite3


class Database:

    def __init__(self, path):
        """
        Constructor of Database class.
        Path : String -  path to the database file
        """
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()

    def disconnect(self, commit):
        """
        Method used to disconnect
        commit : Boolean - true if you want to commit before disconnect ; else False
        """
        if commit:
            self.conn.commit()
        self.conn.close()

    def creation_table_installation(self):
        """
        Method used to create the table installation. Erase existing table.
        """
        self.c.execute('''DROP TABLE IF EXISTS Installation''')
        self.c.execute('''CREATE TABLE Installation (install_num TEXT PRIMARY KEY,
        install_name TEXT, postal_code TEXT, town_name TEXT, street_num TEXT, 
        street_name TEXT, longitude REAL, latitude REAL, no_access_arrang TEXT, 
        access_low_mob_hand TEXT)''')
    
    def creation_table_activity(self):
        """
        Method used to create the table Activity. Erase existing table. 
        """
        self.c.execute('''DROP TABLE IF EXISTS Activity''')
        self.c.execute('''CREATE TABLE Activity (act_code TEXT,
        act_name TEXT, eq_num TEXT REFERENCES Equipment(eq_num))''')

    def creation_table_equipment(self):
        """
        Method used to create the table Equipment. Erase existing table. 
        """
        self.c.execute('''DROP TABLE IF EXISTS Equipment''')
        self.c.execute('''CREATE TABLE Equipment(eq_num TEXT PRIMARY KEY, 
        eq_name TEXT, install_num TEXT REFERENCES Installation(install_num))''')

    def insertion_installation(self, inst):
        """
        Method used to insert an Installation object into the DB
        inst : Installation - The object to insert
        """
        self.c.execute('''INSERT INTO Installation VALUES(\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",
        \"{5}\",\"{6}\",\"{7}\",\"{8}\",\"{9}\")'''.format(inst.install_num,
                                                           inst.postal_code,
                                                           inst.town_name,
                                                           inst.street_num,
                                                           inst.street_name,
                                                           inst.longitude,
                                                           inst.latitude,
                                                           inst.no_access_arrang,
                                                           inst.access_low_mob_hand,
                                                           inst.access_sens_hand))


    def insertion_activity(self, act):
        """
        Method used to insert an Activity object into the DB
        act : Activity - The object to insert
        """
        self.c.execute('''INSERT INTO Activity VALUES(\"{0}\",\"{1}\",
        \"{2}\")'''.format(act.act_code,
                           act.act_name,
                           act.eq_num))

    def insertion_equipment(self, eq):
        """
        Method used to insert an Equipment object into the DB
        equ : Equipment - The object to insert
        """
        self.c.execute('''INSERT INTO Equipment VALUES (\"{0}\", \"{1}\", 
        \"{2}\")'''.format(eq.eq_num,
                           eq.eq_name,
                           eq.install_num))


    def read_installation(self):
        """
        Method used to select all elements in Installation table.
        Return an array with Installation object
        """
        res = self.c.execute('''SELECT * FROM Installation''')
        return res.fetchall() 

    def read_equipment(self):
        """
        Method used to select all elements in Equipment table.
        Return an array with Equipment object
        """
        res = self.c.execute('''SELECT * FROM Equipment''')
        return res.fetchall()

    def read_activity(self):
        """
        Method used to select all elements in Activity table
        Return an array with Activity object
        """
        res = self.c.execute('''SELECT * FROM Activity''')
        return res.fetchall()


    def attribute_installation_to_array(self,attribute):
        """
        Method used to obtain an array which contain all elements for a given attribute
        Return an array with all the elements for the attribute given in parameters
        """
        res = self.c.execute('''SELECT {} FROM Installation'''.format(attribute))
        return res.fetchall()


    def select_installation_tuple_from_pk(self, key):
        """
        Method used to select a tuple from Installation with the primary key
        Return a tuple from Installation table
        """
        res = self.c.execute('''SELECT * FROM Installation WHERE install_num={}'''.format(key))
        return res.fetchone()
