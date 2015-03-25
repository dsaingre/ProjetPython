# Content : WebManager.py
# Class used to manage the web service
# Author : Dimitri SAINGRE

import cherrypy as CP
import sqlite3
import sys
import os
import random
from mako.template import Template
from mako.lookup import TemplateLookup

dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir + "/../dao")

from database import Database as DB

lookup = TemplateLookup(directories=['html'])

class WebManager(object):

    @CP.expose
    def index(self):
        db = DB("../../DB/DB.db")
        array = db.attribute_installation_to_array("install_num")
        random.seed()
        rand_index = random.randint(0, len(array)-1)
        rand_tuple = db.select_installation_tuple_from_pk(array[rand_index][0])
        tmpl = lookup.get_template("index.html")
        return tmpl.render(installation=rand_tuple)

    @CP.expose
    def show_installation(self):
        db = DB("../../DB/DB.db")
        items = db.read_installation()
        tmpl = lookup.get_template("result_installation.html")
        return tmpl.render(array=items, table="Installation")

    @CP.expose
    def show_activity(self):
        db = DB("../../DB/DB.db")
        items = db.read_activity()
        tmpl = lookup.get_template("result_activity.html")
        return tmpl.render(array=items)

    @CP.expose
    def show_equipment(self):
        db = DB("../../DB/DB.db")
        items = db.read_equipment()
        tmpl = lookup.get_template("result_equipment.html")
        return tmpl.render(array=items)

if __name__ == "__main__":
    CP.quickstart(WebManager())
