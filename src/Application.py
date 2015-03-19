# ProjetPython main application 

import argparse
from db.Database import Database as DB
from util.Serializer import Serialiser as seri


def createTableInstallation(path):
    db = DB(path)
    db.creation_table_installation()
    db.disconnect(True)

def createTableEquipment(path):
    db = DB(path)
    db.creation_table_equipment()
    db.disconnect(True)

def createTable(name, path):
    db = DB(path)
    if name == "Installation":
        db.creation_table_installation()
    elif name == "Equipment":
        db.creation_table_equipment()
    elif name == "Activity":
        db.creation_table_activity()
    db.disconnect(True)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Application designed to manipulate open data about sport installations in "Les Pays de la Loire"(FR)')

    parser.add_argument("table_name",
                        type=str, 
                        choices=["Installation","Equipment","Activity"],
                        help="The name of the table you want to work with")

    parser.add_argument("-c",
                        "--creation",
                        type=str, # arg = path to the DB file
                        help="Create a table")

    #parser.add_argument("-i","--insertion",help="Insert an object into a table")
    #parser.add_argument("-s","--select", help="Select an object in a table")
    parser.add_argument("-f","--foo")
    args = parser.parse_args()

    if args.creation:
        createTable(args.table_name, args.creation)
