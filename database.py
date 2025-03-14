import sqlite3

class Database:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
        """)
        self.conn.commit()

    def add_task(self, description):
        self.cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        self.conn.commit()
        return self.cursor.lastrowid

    def complete_task(self, task_id):
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def get_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
