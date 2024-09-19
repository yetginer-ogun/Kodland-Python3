import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Session, Task


class TestAddTask(unittest.TestCase):
    def test_complete_task(self):
        session = Session()
        task = session.query(Task).filter_by(description="Test görevi").first()
        
        if task:
            task.completed = True
            session.commit()
        
        assert task.completed is True
    
        session.close()

if __name__ == '__main__':
    unittest.main()
