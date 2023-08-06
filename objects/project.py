"""
Project Class
"""
from .par import Par

class Project:
    def __init__(self, par=Par()):
        self.par = par

    def save(self):
        pass

def create_new_project():
    print("I created a new project")
    proj = Project()
    return proj