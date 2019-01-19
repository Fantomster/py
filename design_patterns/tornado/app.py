# import sys
import os
import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3


def _execute(query):
    connection = sqlite3.connect('db.sqlite3')
    cursorobj = connection.cursor()
    print(query)
    return cursorobj.execute(query)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = 'select * from task'
        todos = self._execute(query)
        # todos=[[1,2,3],[1,2,3],[1,2,3]]
        self.render('index.html', todos=todos)


class NewHandler(tornado.web.RequestHandler):
    def post(self):
        # print(self.get_arguments('name'))
        name = self.get_arguments('name')
        query = "CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, name TEXT, status NUMERIC)"
        _execute(query)
        query = "insert into task (name,status) values ('%s', '%d') " % (name.pop(), 1)
        _execute(query)
        self.redirect('/')

    def get(self):
        self.render('new.html')


class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = "update task set status=%d where id=%s" % (int(status), id)
        _execute(query)
        self.redirect('/')


class DeleteHandler(tornado.web.RequestHandler):
    def get(self, id):
        query = "delete from task where id=%s" % id
        _execute(query)
        self.redirect('/')


class RunApp(tornado.web.Application):
    def __init__(self):
        Handlers = [
            (r"/", IndexHandler),
            (r"/todo/new", NewHandler),
            (r"/todo/update/(\d+)/status/(\d+)", UpdateHandler),
            (r"/todo/delete/(\d+)", DeleteHandler)
        ]
        settings = dict(
            debug=True,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),

        )
        tornado.web.Application.__init__(self, Handlers, **settings)


if __name__ == '__main__':
    # sys.setrecursionlimit(1000)
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.current().start()
