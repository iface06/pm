from enum import Enum
import uuid
from datetime import datetime

class PersistentObject(object):
    def __init__(self, identifier):
        self.created_date=datetime.now()
        self.modified_date=datetime.now()
        self.identifier = identifier
        self.created_by =

class Application(object):
    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name

class Project(PersistentObject):
    def __init__(self, identifier, target_date):
        super().__init__(identifier)
        self.target_date = target_date
        self.requirements = {}


class Requirement(object):
    def __init__(self, identifier, complexity, author):
        self.identifier = identifier
        self.tasks = {}
        self.description = ''
        self.complexity = complexity
        self.author = author

class WorkingState(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    DONE = 3


class Task(object):
    def __init__(self, identifier, estimation):
        self.identifier = identifier
        self.estimation = estimation
        self.description = ''
        self.time_records = []
        self.working_state = WorkingState.OPEN


class TimeRecord(object):
    def __init__(self, user, start, end):
        self.user = user
        self.start = start
        self.end = end

class User(PersistentObject):
    def __init__(self, identifier, nickname):
        super().__init(self, identifier)
        self.nickname = nickname
        self.active = true
