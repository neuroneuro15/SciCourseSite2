from run import app, freezer


freezer.init_app(app)
freezer.freeze()
# print(list(freezer.all_urls()))