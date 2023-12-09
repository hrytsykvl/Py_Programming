import unittest
from WorkerDB import WorkerDB, Worker


class TestWorkerDatabase(unittest.TestCase):
    def setUp(self):
        self.worker_db = WorkerDB()
        self.worker1 = Worker("Joel", "Miller", "Grocery", 10000)
        self.worker2 = Worker("Peter", "Parker", "Construction", 8000)
        self.worker3 = Worker("Bob", "Hoe", "Nike", 20000)
        self.worker4 = Worker("John", "Milwall", "School", 10800)
        self.worker_db.add_worker(self.worker1)
        self.worker_db.add_worker(self.worker2)
        self.worker_db.add_worker(self.worker3)
        self.worker_db.add_worker(self.worker4)
        filepath = "workers.csv"

    def test_read_workers(self):
        self.worker_db.read_workers("workers.csv")
        self.assertEqual(len(self.worker_db.workers), 8)

    def test_add_workers(self):
        worker1 = Worker("Arthur", "Morgan", "Clinic", 40950)
        worker2 = Worker("Dutch", "Vanderlinde", "University", 80290)
        cur_length = len(self.worker_db.workers)
        self.worker_db.add_worker(worker1)
        self.worker_db.add_worker(worker2)
        afterwards_length = len(self.worker_db.workers)
        self.assertEqual(cur_length + 2, afterwards_length)

    def test_delete_workers(self):
        cur_length = len(self.worker_db.workers)
        self.worker_db.delete_worker(7)
        self.worker_db.delete_worker(8)
        afterwards_length = len(self.worker_db.workers)
        self.assertEqual(afterwards_length, cur_length - 2)

    def test_edit_workers(self):
        self.worker_db.edit_workers(11, "name", "Micah")
        edited_worker = next((w for w in self.worker_db.workers if w.get_id() == 11), None)
        self.assertEqual(edited_worker.name, "Micah")

    def test_sort_workers(self):
        self.worker_db.sort_workers('salary', ascending=True)
        sorted_salaries = [worker.salary for worker in self.worker_db.workers]
        self.assertEqual(sorted_salaries, [8000, 10000, 10800, 20000])

        self.worker_db.sort_workers('name', ascending=False)
        sorted_names = [worker.name for worker in self.worker_db.workers]
        self.assertEqual(sorted_names, ['Peter', 'John', 'Joel', 'Bob'])

    def test_search_workers(self):
        search_results = self.worker_db.search_workers('name', 'Peter')
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0].name, 'Peter')

        search_results_none = self.worker_db.search_workers('department', 'fpsopfosp')
        self.assertEqual(len(search_results_none), 0)


if __name__ == "__main__":
    unittest.main()
