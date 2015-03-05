from Serializer import Serializer as Seri
from Installation import Installation as Insta
from Database import Database as Db

def main():
    seri = Seri()
    seri.unserialize_json("../data/installation/installation.json")
    db = Db("../DB/DB.db")
    for i in seri.collection:
        db.insertionInstallation(i)
    db.disconnect()
