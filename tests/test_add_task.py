import unittest
from database import Database

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def tearDown(self):
        self.db.close()

    def test_add_task(self):
        task_id = self.db.add_task("Yeni görev")
        tasks = self.db.get_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][0], task_id)
        self.assertEqual(tasks[0][1], "Yeni görev")
        self.assertFalse(tasks[0][2])  # Default olarak tamamlanmamış olmalı

if __name__ == "__main__":
    unittest.main()
