from routs.routs import Routs
from request_response.response import HTMLResponse, JsonResponse

router = Routs()


router.register("/", HTMLResponse("<p><b>MAIN<b/><p/>"))
router.register("/contact", HTMLResponse("<p><b>contact<b/><p/>"))
router.register("/j_test", JsonResponse({"page": "JSON TEST"}))
router.register("/j_test2", JsonResponse({"page": "JSON TEST2"}))
