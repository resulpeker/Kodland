import unittest
from database import Database

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def tearDown(self):
        self.db.close()

    def test_complete_task(self):
        task_id = self.db.add_task("Tamamlanacak görev")
        self.db.complete_task(task_id)
        tasks = self.db.get_tasks()
        self.assertTrue(tasks[0][2])  # Görev tamamlandı olarak işaretlenmeli

if __name__ == "__main__":
    unittest.main()
