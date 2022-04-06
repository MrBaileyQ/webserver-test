from utils import render_view

def view_req(request):
    context = {}
    return render_view("views/lbasic.html", context)

def view_2(request):
    context = {
        "name": "John",
        "age": "42",
        "title": "Mr.",
        "married": "True",
        "child_count": "3",
        "children": [
            "John",
            "Jane",
            "Jack",
        ],
    }
    return render_view("views/test.html", context)