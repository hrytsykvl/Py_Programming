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
        self.salary = salary

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

    def display_workers(self):
        for worker in self.workers:
            print(worker)
