import unittest
from database import Database

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def tearDown(self):
        self.db.close()

    def test_delete_task(self):
        task_id = self.db.add_task("Silinecek görev")
        self.db.delete_task(task_id)
        tasks = self.db.get_tasks()
        self.assertEqual(len(tasks), 0)  # Görev silindiği için liste boş olmalı

if __name__ == "__main__":
    unittest.main()
