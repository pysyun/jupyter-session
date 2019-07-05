import os
import dill

class Session:
    
    def __init__(self, fileName = 'session.db'):
        self.fileName = fileName
        if os.path.isfile(self.fileName):
            dill.load_session(self.fileName)
            
    def process(self):
        dill.dump_session(self.fileName)
