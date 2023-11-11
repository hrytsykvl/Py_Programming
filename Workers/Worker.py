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
