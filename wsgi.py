from sassutils.wsgi import SassMiddleware
from server import app

if __name__ == "__main__":
    app.wsgi_app = SassMiddleware(app.wsgi_app, {
        'web_server': ('static/assets/sass', 'static/assets/css', '/static/assets/css')
    })

    app.run()
