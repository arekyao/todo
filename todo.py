""" Basic todo list using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/view', 'View',
    '/del/(\d+)', 'Delete',
    '/add', 'NewEntry'
)


### Templates
render = web.template.render('templates', base='base')
#render = web.template.render('templates')



class View:

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, 
            description="I need to:"),
        web.form.Button('Add todo'),
    )

    def GET(self):
        """ Show page """
        todos = model.get_todos()
        form = self.form()
        return render.view(todos, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        form.validates()
        model.new_todo(form.d.title)
        raise web.seeother('/view')


class Index:

    def GET(self):
        """ Show page """
        
        return render.index()

class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/view')


class NewEntry:

    def POST(self):
        """ Add based str """
        i=web.input()
        str = i.todo_name
        model.new_todo(str)
        raise web.seeother('/view')

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
