from WorkerDB import WorkerDB
from Worker import Worker

MENU = """
1. Load data from csv file
2. Add worker
3. Delete worker
4. Sort workers
5. Search workers
6. Edit worker
7. Show workers
0. Quit
"""


def main():
    workers = WorkerDB()

    while True:
        print(MENU)
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                try:
                    filepath = input("Enter file you want to read from: ")
                    workers.read_workers(filepath)
                except Exception as ex:
                    print(ex)
            case '2':
                name = input("Enter name: ")
                surname = input("Enter surname: ")
                department = input("Enter department: ")
                salary = float(input("Enter salary: "))
                worker = Worker(name, surname, department, salary)
                workers.add_worker(worker)
            case '3':
                worker_id = int(input("Enter id: "))
                workers.delete_worker(worker_id)
            case '4':
                field_name = input("Enter field name to sort(name, surname, department, salary): ")
                ascending = input("Sort in ascending order? (y/n): ").lower().startswith('y')
                workers.sort_workers(field_name, ascending)
            case '5':
                field_name = input("Enter field name to search by(name, surname, department, salary): ")
                keyword = input("Enter keyword: ")
                workers.search_workers(field_name, keyword)
            case '6':
                worker_id = int(input("Enter id: "))
                field_to_edit = input("Enter field name to edit(name, surname, department, salary): ")
                edited_field = input(f"Enter the new value for {field_to_edit}:")
                workers.edit_workers(worker_id, field_to_edit, edited_field)
            case '7':
                workers.display_workers()
            case '0':
                return
            case _:
                print("Invalid choice. Please enter a valid option.")
                continue


if __name__ == "__main__":
    main()
