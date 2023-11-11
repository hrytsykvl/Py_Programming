import csv

id_count = 0


class Worker:
    def __init__(self, name, surname, department, salary):
        global id_count
        self.__id = id_count
        id_count += 1
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = float(salary)

    def get_id(self):
        return self.__id

    def __str__(self):
        return (f"Worker's id: {self.__id}\n"
                f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"Department: {self.department}\n"
                f"Salary: {self.salary}\n")


class WorkerDB:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def delete_worker(self, worker):
        self.workers.remove(worker)

    def read_workers(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name, surname, department, salary = row
                worker = Worker(name, surname, department, salary)
                self.add_worker(worker)

    def edit_workers(self, local_id, local_label, edited_label):
        for worker in self.workers:
            if worker.get_id() == local_id:
                worker_to_edit = worker
                setattr(worker_to_edit, local_label, edited_label)

    def sort_workers(self, field, ascending=True):
        self.workers.sort(key=lambda worker: getattr(worker, field), reverse=not ascending)

    def display_workers(self):
        for worker in self.workers:
            print(worker)
