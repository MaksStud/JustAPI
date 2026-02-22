from routs.routs import Routes
from request_response.response import HTMLResponse

router = Routes()


router.register("/two", HTMLResponse("<p><b>TWo<b/><p/>"))
