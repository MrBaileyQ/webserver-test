def internal_print(msg):
    # TODO: ADD LOGGING HERE
    pass

class Url():
    view_function = None
    path = ""
    
    def __init__(self, view_function, path):
        self.view_function = view_function
        self.path = path

class render_view():
    file = ""
    context = []
    def __init__(self, f, c):
        self.file = f
        self.context = c