from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        courses = self.models['Course'].get_course()
        return self.load_view('index.html', courses = courses)

    def add(self):
        data = {
            'title': request.form['title'],
            'description': request.form['description']
        }
        self.models['Course'].add_course(data)
        return redirect('/')

    def remove(self, id):
        course_id = self.models['Course'].remove(id)
        return self.load_view('remove.html', course_id=id)
