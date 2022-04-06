from utils import Url

import views.default_view as dview

url_paths = [
    Url(dview.view_req, "/"),
    Url(dview.view_2, "/john"),
]