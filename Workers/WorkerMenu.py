from Worker import Worker
from WorkerDB import WorkerDB
import tkinter as tk


class WorkerMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Workers Menu")
        self.workers = WorkerDB()

        self.file_label = tk.Label(root, text="Enter filename: ")
        self.file_label.place(x=10, y=10)

        self.file_entry = tk.Entry(root)
        self.file_entry.place(x=100, y=10)

        self.diagram_button = tk.Button(root, text="Show Diagram", command=self.show_diagram)
        self.read_workers_button = tk.Button(root, text="Read Workers", command=self.read_workers)
        self.display_workers_button = tk.Button(root, text="Display Workers", command=self.display_workers)
        self.add_worker_button = tk.Button(root, text="Add Worker", command=self.add_worker)
        self.delete_worker_button = tk.Button(root, text="Delete Worker", command=self.delete_worker_window)
        self.sort_workers_button = tk.Button(root, text="Sort Workers", command=self.sort_window)
        self.search_workers_button = tk.Button(root, text="Search Workers", command=self.search_window)
        self.edit_workers_button = tk.Button(root, text="Edit Workers", command=self.edit_window)

        self.read_workers_button.place(x=10, y=40)
        self.display_workers_button.place(x=100, y=40)
        self.diagram_button.place(x=203, y=40)
        self.add_worker_button.place(x=10, y=80)
        self.delete_worker_button.place(x=90, y=80)
        self.sort_workers_button.place(x=10, y=120)
        self.search_workers_button.place(x=95, y=120)
        self.edit_workers_button.place(x=195, y=120)

    def read_workers(self):
        filename = self.file_entry.get()
        if filename:
            self.workers.read_workers(filename)
            print("Workers read from file:", filename)
        else:
            print("Please enter a filename.")

    def show_diagram(self):
        self.workers.plot_pie_by_department()
        print("Pie chart generated and saved")

    def display_workers(self):
        workers_window = tk.Toplevel(self.root)
        workers_window.title("Workers List")

        workers_text = tk.Text(workers_window)
        workers_text.pack()

        for worker in self.workers.workers:
            workers_text.insert(tk.END, str(worker) + '\n\n')

    def add_worker(self):
        add_worker_window = tk.Toplevel(self.root)
        add_worker_window.title("Add Worker")

        labels = ['Name:', 'Surname:', 'Department:', 'Salary:']
        self.entries = []

        for label in labels:
            tk.Label(add_worker_window, text=label).pack()
            entry = tk.Entry(add_worker_window)
            entry.pack()
            self.entries.append(entry)

        add_button = tk.Button(add_worker_window, text="Add", command=self.process_worker)
        add_button.pack(pady=10)

    def process_worker(self):
        name, surname, department, salary = (entry.get() for entry in self.entries)
        try:
            salary = float(salary)
            if name and surname and department and salary:
                worker = Worker(name, surname, department, salary)
                self.workers.add_worker(worker)
                print("Worker added:", worker)
                self.display_workers()
            else:
                print("Please fill in all fields.")
        except ValueError:
            self.entries[3].delete(0, tk.END)
            self.entries[3].insert(tk.END, "Invalid Salary")
            self.entries[3].config(fg="red")

    def delete_worker_window(self):
        delete_worker_window = tk.Toplevel(self.root)
        delete_worker_window.title("Delete Worker")

        id_label = tk.Label(delete_worker_window, text="Enter Worker ID:")
        id_label.pack()

        self.id_entry = tk.Entry(delete_worker_window)
        self.id_entry.pack()

        delete_button = tk.Button(delete_worker_window, text="Delete worker", command=self.delete_worker)
        delete_button.pack(pady=10)

    def delete_worker(self):
        worker_id = self.id_entry.get()
        try:
            worker_id = int(worker_id)
            self.workers.delete_worker(worker_id)
            print(f"Worker with ID {worker_id} deleted.")
            self.display_workers()
        except ValueError:
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(tk.END, "Invalid ID")
            self.id_entry.config(fg="red")

    def sort_window(self):
        sort_worker_window = tk.Toplevel(self.root)
        sort_worker_window.title("Sort Workers")

        sort_field = tk.Label(sort_worker_window, text="Enter field name to sort(id, name, surname, department, salary):")
        sort_field.pack()
        self.sort_field_entry = tk.Entry(sort_worker_window)
        self.sort_field_entry.pack()
        sort_type = tk.Label(sort_worker_window, text="Enter sort type (asc/desc):")
        sort_type.pack()
        self.sort_type_entry = tk.Entry(sort_worker_window)
        self.sort_type_entry.pack()

        sort_button = tk.Button(sort_worker_window, text="Sort", command=self.sort_workers)
        sort_button.pack(pady=10)

    def sort_workers(self):
        field = self.sort_field_entry.get()
        sort_type = self.sort_type_entry.get()

        if field and sort_type in ('asc', 'desc'):
            ascending = True if sort_type == 'asd' else False
            self.workers.sort_workers(field, ascending)
            print(f"Sorted by {field} in {sort_type}ending order.")
            self.display_workers()
        else:
            print("Please enter a valid field and sort type (asc/desc).")

    def search_window(self):
        search_worker_window = tk.Toplevel(self.root)
        search_worker_window.title("Search Workers")

        search_field = tk.Label(search_worker_window,
                              text="Enter field name to search(name, surname, department, salary):")
        search_field.pack()
        self.search_field_entry = tk.Entry(search_worker_window)
        self.search_field_entry.pack()
        search_keyword = tk.Label(search_worker_window, text="Enter keyword to search by:")
        search_keyword.pack()
        self.keyword_entry = tk.Entry(search_worker_window)
        self.keyword_entry.pack()

        search_button = tk.Button(search_worker_window, text="Search", command=self.search_workers)
        search_button.pack(pady=10)

    def display_matching(self, field, keyword):
        workers_window = tk.Toplevel(self.root)
        workers_window.title("Workers List")

        workers_text = tk.Text(workers_window)
        workers_text.pack()

        for worker in self.workers.workers:
            if keyword.lower() in str(getattr(worker, field)).lower():
                workers_text.insert(tk.END, str(worker) + '\n\n')

    def search_workers(self):
        field = self.search_field_entry.get()
        keyword = self.keyword_entry.get()

        self.display_matching(field, keyword)

    def edit_window(self):
        edit_worker_window = tk.Toplevel(self.root)
        edit_worker_window.title("Edit Workers")

        id_label = tk.Label(edit_worker_window, text="Enter Worker ID:")
        id_label.pack()

        self.edit_id_entry = tk.Entry(edit_worker_window)
        self.edit_id_entry.pack()

        field_label = tk.Label(edit_worker_window, text="Enter field name to edit(name, surname, department, salary):")
        field_label.pack()

        self.edit_field_entry = tk.Entry(edit_worker_window)
        self.edit_field_entry.pack()

        new_value_label = tk.Label(edit_worker_window, text="Enter a new value:")
        new_value_label.pack()

        self.new_value_entry = tk.Entry(edit_worker_window)
        self.new_value_entry.pack()

        edit_button = tk.Button(edit_worker_window, text="Edit", command=self.edit_workers)
        edit_button.pack(pady=10)

    def edit_workers(self):
        wk_id = int(self.edit_id_entry.get())
        field_to_edit = self.edit_field_entry.get()
        new_value = self.new_value_entry.get()

        if field_to_edit == "salary":
            try:
                new_value = float(new_value)
                self.workers.edit_workers(wk_id, field_to_edit, new_value)
                self.display_workers()
            except ValueError:
                self.new_value_entry.delete(0, tk.END)
                self.new_value_entry.insert(tk.END, "Invalid value")
                self.new_value_entry.config(fg="red")
        else:
            self.workers.edit_workers(wk_id, field_to_edit, new_value)
            self.display_workers()