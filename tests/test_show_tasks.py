import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Session, Task


class TestAddTask(unittest.TestCase):
    def test_show_tasks(self):
        session = Session()
        tasks = session.query(Task).all()
        assert isinstance(tasks, list)
        session.close()



if __name__ == '__main__':
    unittest.main()