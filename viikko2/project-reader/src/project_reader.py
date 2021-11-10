from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        
        olio = toml.loads(content)
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(olio['tool']['poetry']['name'], 
                       olio['tool']['poetry']['description'], 
                       olio['tool']['poetry']['dependencies'], 
                       olio['tool']['poetry']['dev-dependencies'])
