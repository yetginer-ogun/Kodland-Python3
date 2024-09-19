import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Session, Task


class TestAddTask(unittest.TestCase):
    def test_delete_task(self):
        session = Session()
        task = session.query(Task).filter_by(description="Test görevi").first()
        
        if task:
            session.delete(task)
            session.commit()
        
        task = session.query(Task).filter_by(description="Test görevi").first()
        assert task is None
        
        session.close()


if __name__ == '__main__':
    unittest.main()