from wsgiref.simple_server import make_server

import falcon

APP_VERSION = '1.0.0'


# class AppInfoResource:
#
#     def on_get(self, req, resp):
#         resp.status = falcon.HTTP_200
#         resp.content_type = falcon.MEDIA_TEXT
#         resp.text = (f'\nName: UI Testrunner'
#                      f'\nApp version: {APP_VERSION}'
#                      f'\nDeveloped with Falcon Framework.'
#                      f'\n')
#
#
# app = falcon.App()
#
# app_info = AppInfoResource()
#
# app.add_route('/app_info', app_info)
#
# if __name__ == '__main__':
#     with make_server('', 7000, app) as httpd:
#         print('Serving on port 7000...')
#
#         httpd.serve_forever()
