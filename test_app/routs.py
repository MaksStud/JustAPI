from routs.routs import Routs
from request_response.response import HTMLResponse, JsonResponse

router = Routs()


router.set("/", HTMLResponse("<p><b>MAIN<b/><p/>"))
router.set("/contact", HTMLResponse("<p><b>contact<b/><p/>"))
router.set("/j_test", JsonResponse({"page": "JSON TEST"}))
router.set("/j_test2", JsonResponse({"page": "JSON TEST2"}))
