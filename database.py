import jsonpickle


class Database:
    DATA_FILE_NAME = "data.json"
    DATA_FILE = open(DATA_FILE_NAME, "r+")

    def __init__(self):
        self.projects = self._load_projects()

    def _store(self):
        j = jsonpickle.encode(self.projects, Database.DATA_FILE)
        Database.DATA_FILE.seek(0)
        Database.DATA_FILE.truncate()
        Database.DATA_FILE.write(j)

    def _load_projects(self):
        return jsonpickle.decode(Database.DATA_FILE.read())

    def store_project(self, project):
        self.projects[project.identifier] = project
        self._store()

    def load_project(self, project_identifier):
        if self.projects.len == 0:
            self._load_projects()
        return self.projects[project_identifier]

    def list_projects(self):
        return self.projects

    def delete_project(self, p):
        del self.projects[p.identifier]
