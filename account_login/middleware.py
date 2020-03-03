from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import LoggedInUser


class OneSessionPerUserMiddleware:
    # Called only once when the web server starts
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            print("if loop started")
            #stored_session_key = request.user.logged_in_user.session_key
            #print(request.session.session_key)
            #print(stored_session_key)
            session_key = request.session.session_key
            try:
                logged_in_user = request.user.logged_in_user
                stored_session_key = logged_in_user.session_key
                if stored_session_key and stored_session_key != session_key:
                    print(stored_session_key)
                    Session.objects.filter(session_key=stored_session_key).delete()
                request.user.logged_in_user.session_key = request.session.session_key
                request.user.logged_in_user.save()
            except ObjectDoesNotExist:
                LoggedInUser.objects.create(user=request.user, session_key=session_key)
            stored_session_key = request.user.logged_in_user.session_key
            if stored_session_key and stored_session_key != request.session.session_key:
                Session.objects.get(session_key=stored_session_key).delete()
                print("second if loop started")

        response = self.get_response(request)
        return response



                #request.session.modified = True



