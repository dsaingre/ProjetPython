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
        try:
            self.conn = sqlite3.connect(path)
            self.c = self.conn.cursor()
        except sqlite3.OperationalError as e:
            print("An error as occured : {}".format(e))

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
        address TEXT, longitude REAL, latitude REAL, no_access_arrang TEXT, 
        access_low_mob_hand TEXT, access_sens_hand TEXT)''')
    
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
        \"{5}\",\"{6}\")'''.format(inst.install_num,
                                   inst.address,
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


    def select_all_from_install_pk(self, key):
        """
        Method used to select all installations and associate equipments from installation primary key
        Return an array containing installations and equipment
        """
        try:
            res = self.c.execute(
                '''SELECT * FROM Installation 
                LEFT JOIN Equipment ON Installation.install_num=Equipment.install_num 
                LEFT JOIN Activity ON Equipment.eq_num=Activity.eq_num 
                WHERE Installation.install_num={}'''.format(key))
            return res.fetchall()
        except sqlite3.OperationalError as e:
            print("An error with database as occured : {}".format(e))
