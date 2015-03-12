from Serializer import Serializer as Seri
from Installation import Installation as Insta
from Database import Database as Db
from progressbar import ProgressBar as Progress

def main():
    """
    seri = Seri()
    progr = Progress()
    seri.unserialize_json_equipment("../data/equipements/equipements.json")
    db = Db("../DB/DB.db")
    for i in progr(seri.collection):
        db.insertion_equipment(i)
    """

    seri = Seri()
    progr = Progress()
    seri.unserialize_json_activity("../data/activites/activites.json")
    db = Db("../DB/DB.db")
    for i in progr(seri.collection):
        db.insertion_activity(i)

    """
    seri = Seri()
    progr = Progress()
    seri.unserialize_json_installation("../data/installation/installation.json")
    db = Db("../DB/DB.db")
    for i in progr(seri.collection):
        db.insertion_installation(i)
    """

    db.disconnect()
