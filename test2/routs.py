from routs.routs import Routs
from request_response.response import HTMLResponse

router = Routs()


router.register("/two", HTMLResponse("<p><b>TWo<b/><p/>"))
