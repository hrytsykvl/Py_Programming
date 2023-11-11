import csv
from Worker import Worker


class WorkerDB:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def delete_worker(self, local_id):
        for i in range(len(self.workers)):
            if self.workers[i].get_id() == local_id:
                self.workers.pop(i)
                return

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

    def search_workers(self, search_query):
        search_results = []
        for worker in self.workers:
            if search_query.lower() in str(worker).lower():
                search_results.append(worker)
        print("Search Results:\n")
        for ad in search_results:
            print(ad, end="\n\n")

    def display_workers(self):
        for worker in self.workers:
            print(worker)