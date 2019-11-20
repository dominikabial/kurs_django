from django_redis import get_redis_connection


class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        con = get_redis_connection("default")
        response = self.get_response(request)

        print("\nTO DZIALŁA")
        n_request = con.incr("xxx")
        keys = con.keys(n_request)

        for k in keys:
            print(k, con.get(k), sep=":")

        # Code to be executed for each request/response after
        # the view is called.
        #if not request.user.is_superuser:
        #    print("TO nie jest superuser")
        #else:
        #    print("TO jest super")

        return response
