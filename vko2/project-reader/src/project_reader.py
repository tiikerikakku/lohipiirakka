from urllib import request
from project import Project
from toml import loads

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        a = loads(content)
        # print(a)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        # return Project("Test name", "Test description", [], [])
        return Project(a['tool']['poetry']['name'], a['tool']['poetry']['description'], a['tool']['poetry']['dependencies'], a['tool']['poetry']['group']['dev']['dependencies'], a['tool']['poetry']['authors'], a['tool']['poetry']['license'])
