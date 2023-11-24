import csv
from Worker import Worker


def sort_dec(func):
    def wrapper(self, field, ascending=True):
        try:
            func(self, field, ascending)
            print(f"Sorted by {field}:")
            self.display_workers()
        except AttributeError:
            print("Invalid field for sorting.")

    return wrapper


def search_dec(func):
    def wrapper(self, field, keyword):
        try:
            return func(self, field, keyword)
        except AttributeError:
            print("Invalid field for searching.")

    return wrapper


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
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    name, surname, department, salary = row
                    worker = Worker(name, surname, department, salary)
                    self.add_worker(worker)
        except FileNotFoundError:
            print("File not found")

    def edit_workers(self, local_id, local_label, edited_label):
        for worker in self.workers:
            if worker.get_id() == local_id:
                worker_to_edit = worker
                setattr(worker_to_edit, local_label, edited_label)

    @sort_dec
    def sort_workers(self, field, ascending=True):
        self.workers.sort(key=lambda worker: getattr(worker, field), reverse=not ascending)

    @search_dec
    def search_workers(self, field, keyword):
        search_results = []
        for worker in self.workers:
            if keyword.lower() in str(getattr(worker, field)).lower():
                search_results.append(worker)
        if len(search_results) == 0:
            print(f"There are no matches in '{field}' with keyword:'{keyword}'")
        else:
            print(f"Search Results for {field} containing '{keyword}':\n")
            for result in search_results:
                print(result, end="\n\n")
        return search_results

    def display_workers(self):
        for worker in self.workers:
            print(worker)
