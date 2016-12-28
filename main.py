import datetime
import project


def main():
    target_date = datetime.date.today()
    p = project.create('P22', target_date)
    r = project.new_requirement_to_project(p, 'P22-1', 100)
    r.description = 'Die Anwendung soll mit Hilfe der AWS betrieben werden.'
    t1 = project.new_task_to_requirement(r, "P22-1-1", 60*8*4)
    t1.description = 'Einarbeitung in die AWS Dienst für den Betrieb von Java-Webanwendungen.'
    t2 = project.new_task_to_requirement(r, "P22-1-2", 60*8)
    t2.description = 'Aufsetzen der Umgebung.'
    project.store_project(p)
    project.calculate_project_end(p)


if __name__ == '__main__':
    main()