""" Basic todo list using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/view', 'View',
    '/del/(\d+)', 'Delete',
    '/add', 'NewEntry',
    '/ajax', 'ViewSuggest',
    '/account', 'Account'

)


### Templates
render = web.template.render('templates', base='base')
#render = web.template.render('templates')


class ViewSuggest:
    def GET(self):
        type_ajax = int(web.input()['type'])
        print type_ajax
        query = web.input()['q'].strip()
        print query

        if type_ajax == 0:
            return "no suggestion in this type"
        elif type_ajax == 1:
            if query[0]>='a' and query[0]<='z':
                return "OK"
            else:
                return "invalid"

        """ Show page """


        return "no suggestion,pls"



class Account:

    def GET(self):
        """ Show page """
        return render.account()



class View:

    def GET(self):
        """ Show page """
        todos = model.get_todos()
        return render.view(todos)


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
        if str == "":
            raise web.seeother('/view')
        model.new_todo(str)
        raise web.seeother('/view')

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
