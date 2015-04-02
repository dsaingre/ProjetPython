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
from dao.database import Database as DB


lookup = TemplateLookup(directories=['web/html'])

class WebManager(object):
    """
    Class used to provide a web service to consult data
    """

    @CP.expose
    def index(self):
        """
        The index page : introduce the website, show different links to navigate
        on the website and show a random installation
        KNOWN BUGS : Activity are never found
        """
        db = DB("../DB/DB.db")
        array = db.attribute_installation_to_array("install_num")
        random.seed()
        rand_tuples = db.select_all_from_install_pk(array[random.randint(0, len(array)-1)][0])
        tmpl = lookup.get_template("index.html")
        return tmpl.render(installation=rand_tuples)

    
    @CP.expose
    def show_installation(self):
        """
        This page show all installations
        """
        db = DB("../DB/DB.db")
        items = db.read_installation()
        tmpl = lookup.get_template("result_installation.html")
        return tmpl.render(array=items, table="Installation")

    @CP.expose
    def show_activity(self):
        """
        This page show all activities
        """
        db = DB("../DB/DB.db")
        items = db.read_activity()
        tmpl = lookup.get_template("result_activity.html")
        return tmpl.render(array=items)

    @CP.expose
    def show_equipment(self):
        """
        This page show all equipments
        """
        db = DB("../DB/DB.db")
        items = db.read_equipment()
        tmpl = lookup.get_template("result_equipment.html")
        return tmpl.render(array=items)

    @CP.expose
    def search(self, installation=None, activity=None):
        """
        This page is used to search an installation/equipment/activity
        """
        #tmpl = lookup.get_template("search.html")            
        #return tmpl.render(install=installation, act=activity)
        return "not implemented yet.<br/>Return to <a href='index'>index</a>"

if __name__ == "__main__":
    CP.quickstart(WebManager()) #start the webmanager
