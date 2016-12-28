import database
import entities

db = database.Database()


def load_projects():
    return db.list_projects()

def load_project(identifier):
    return db.load_project(identifier)

def create(identifier, target_date):
    return entities.Project(identifier, target_date)

def delete_project(p):
    db.delete_project(p)

def new_requirement_to_project(project, identifier, complexity):
    r = entities.Requirement(identifier, complexity)
    project.requirements[identifier] = r
    return r;

def load_requirment(project, identifier):
    return project.requirements[identifier]

def delete_requirment(p, r):
    del p.requirements[r.identifier]


def new_task_to_requirement(r, identifier, estimation):
    t = entities.Task(identifier, estimation)
    r.tasks[task] = t
    return t

def delete_task(r, t):
    del r.tasks[t.identifier]

def load_task(r, identifier):
    return r.tasks[identifier]

def store_project(p):
    db.store_project(p)

def new_time_record(t, user, start_date, end_date):
    tr = entities.TimeRecord(user, start_date, end_date)
    t.time_records.append(tr)
    return tr

def calculate_project_end(p, start_date):
    estimation = 0
    for r in p.requirements:
        for t in r.tasks:
            estimation += t.estimation
