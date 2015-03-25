# ProjetPython main application 

import argparse
from db.Database import Database as DB
from util.Serializer import Serializer as Seri
from progressbar.progressbar import ProgressBar

def create_table(table_name, db_path):
    db = DB(db_path)
    if table_name == "Installation":
        db.creation_table_installation()
    elif table_name == "Equipment":
        db.creation_table_equipment()
    elif table_name == "Activity":
        db.creation_table_activity()
    db.disconnect(True)

def insertion_json_file(table_name, db_path, json_file):
    db = DB(db_path)
    progress = ProgressBar()
    s = Seri()
    if table_name == "Installation":
        s.unserialize_json_installation(json_file)
        for item in progress(s.collection):
            db.insertion_installation(item)
    elif table_name == "Equipment":
        s.unserialize_json_equipment(json_file)
        for item in progress(s.collection):
            db.insertion_equipment(item)
    elif table_name == "Activity":
        s.unserialize_json_activity(json_file)
        for item in progress(s.collection):
            db.insertion_activity(item)
    db.disconnect(True)

def read_database(table_name, db_path):
    db = DB(db_path)
    if table_name == "Installation":
        res = db.read_installation()
        print(res)
    elif table_name == "Equipment":
        res = db.read_equipment()
        print(res)
    elif table_name == "Activity":
        res = db.read_activity()
        print(res)
    db.disconnect(True)
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Application designed to manipulate open data about sport installations in "Les Pays de la Loire"(FR)')

    parser.add_argument("table_name",
                        type=str, 
                        choices=["Installation","Equipment","Activity"],
                        help="The name of the table you want to work with")

    parser.add_argument("DB_path",
                        type=str,
                        help="The path to the data base file")

    parser.add_argument("-c",
                        "--creation",
                        action="store_true",
                        help="Create a table")

    parser.add_argument("-jsi", 
                        "--json-insertion", 
                        type=str,
                        help="Insert the content of a json file into the table. Need the path to the json file")

    parser.add_argument("-r",
                        "--read", 
                        action="store_true",
                        help="read all database")
    args = parser.parse_args()

    if args.creation:
        create_table(args.table_name, args.DB_path)
    if args.json_insertion:
        insertion_json_file(args.table_name, args.DB_path, args.json_insertion)
    if args.read:
        read_database(args.table_name, args.DB_path)
