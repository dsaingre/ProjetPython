import cherrypy as CP
import sqlite3
from mako.template import Template

class WebManager(object):
    @CP.expose
    def index(self):
        return '<a href="install" >Cliquez ici pour consulter toutes les données de la table Installation</a>'

    @CP.expose
    def install(self):
        try:
            conn = sqlite3.connect("../../DB/DB.db")
            c = conn.cursor()
            c.execute('''SELECT * FROM Installation''')
            items = c.fetchall()
            st = st.join(str(item) for item in items)
            return st
        except Exception as e:
            return "An error as occured :'("



if __name__ == "__main__":
    CP.quickstart(WebManager())
