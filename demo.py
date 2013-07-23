#!/usr/bin/python
# coding=utf-8
from os import path

from tornado import web, ioloop, gen

from handlers import *


def load_app(port, root):
    settings = {
        "static_path": path.join(root, "static"),
        "template_path": path.join(root, "template"),
        "globals": {
            "project_name": u"震歪歪",
        }
    }

    routers = [
        (r"/", MainHandler),
        (r"/detail", DetailHandler),
        (r"/ajax-detail", AjaxDetailHandler),
    ]

    application = web.Application(
        routers,
        **settings
    )
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":

    root = path.dirname(__file__)
    port = 2080
    load_app(port, root)
