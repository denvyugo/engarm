import sqlite3


class ProjectData:
    __slots__ = ('number', 'name', 'current')

    def __init__(self, number=0, name='NewProject', current=True):
        self.number = number
        self.name = name
        self.current = current


class EngarmDB:
    # database connection
    _cnn = sqlite3.connect('data\\engarm.sqlite')
    # cursor
    _cur = _cnn.cursor()

    def close_db(self):
        print('close db')
        self._cnn.close()

    def add_project(self, project):
        # get last number
        sql = 'select ID from Projects order by ID desc limit 1'
        try:
            self._cur.execute(sql)
            numb = self._cur.fetchone()
        except Exception as e:
            print(e)
        else:
            if numb is not None:
                project.number = numb[0] + 1
            else:
                project.number = 1
        # insert new record for project
        sql = 'insert into Projects (ID, ProjectName, ProjectCurrent) values (?, ?, ?)'
        try:
            self._cur.execute(sql, (project.number, project.name, project.current))
        except Exception as e:
            print(e)
        else:
            self._cnn.commit()

    def get_project(self, number=0):
        if number == 0:
            sql = 'select ID, ProjectName, ProjectCurrent from Projects order by ID desc limit 1'
            prms = ()
        else:
            sql = 'select ID, ProjectName, ProjectCurrent from Projects where ID = ?'
            prms = (number,)
        try:
            self._cur.execute(sql, prms)
            row = self._cur.fetchone()
            prj = ProjectData()
            prj.number, prj.name, prj.current = row
            return prj
        except Exception as e:
            print(e)

    def upd_project(self, project):
        sql = 'update Projects set ProjectName = ?, ProjectCurrent = ? where ID = ?'
        params = (project.name, project.current, project.number)
        try:
            self._cur.execute(sql, params)
            self._cnn.commit()
        except Exception as e:
            print('Error in ''sql'':', e)

