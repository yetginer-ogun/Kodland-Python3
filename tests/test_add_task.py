import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Session, Task


class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        session = Session()
        new_task = Task(description="Test görevi")
        session.add(new_task)
        session.commit()
        
        task = session.query(Task).filter_by(description="Test görevi").first()
        assert task is not None
        assert task.description == "Test görevi"
        
        session.close()


if __name__ == '__main__':
    unittest.main()