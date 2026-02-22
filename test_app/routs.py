from routs.routs import Routes
from request_response.response import HTMLResponse, JsonResponse

router = Routes()


router.register("/", HTMLResponse("<p><b>MAIN<b/><p/>"))
router.register("/contact", HTMLResponse("<p><b>contact<b/><p/>"))
router.register("/j_test", JsonResponse({"page": "JSON TEST"}))
router.register("/j_test/two", JsonResponse({"page": "JSON TEST2"}))
