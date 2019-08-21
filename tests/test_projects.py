import datas
import projects
import unittest


class TestProject(unittest.TestCase):

    def test_project(self):
        project = projects.Project()
        project.new_project('new_project_one')
        db = datas.EngarmDB()
        prj = db.get_project()
        self.assertEqual('new_project_one', prj.name)
