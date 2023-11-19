def generator_id():
    count = 1
    while True:
        yield count
        count += 1


class Worker:
    id_count = generator_id()

    def __init__(self, name, surname, department, salary):
        self.__id = next(self.id_count)
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
