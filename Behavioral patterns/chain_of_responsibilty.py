from abc import ABC, abstractmethod
from typing import Optional


class IHandler(ABC):
    """Handler interface"""
    @abstractmethod
    def set_next(self, handler):
        ...

    @abstractmethod
    def handle(self, request, handler_func) -> Optional[str]:
        ...


class WebRequestHandler(IHandler):
    """Implementation for handler interface"""

    _error_massage = ''

    def __init__(self):
        self.next = None

    def set_next(self, handler: IHandler) -> IHandler:
        self.next = handler

    def handle(self, request) -> Optional[str]:
        if self._check_request(request):
            if self.next is None:
                return f'Access granted for url: {request.url}'
            return self.next.handle(request)

        return self._error_massage

    def _check_request(self, request):
        return True


class HTTPGetWebRequestHandler(WebRequestHandler):
    _error_massage = 'Bad HTTP method.'

    def _check_request(self, request):
        return request.method == 'get'


class LoggedWebRequestHandler(WebRequestHandler):
    _error_massage = 'User is not logged.'

    def _check_request(self, request):
        return request.is_user_logged


class AdminStatusWebRequestHandler(WebRequestHandler):
    _error_massage = 'User is not an admin.'

    def _check_request(self, request):
        return request.is_user_admin


class HandlerChain:
    """Let's you build and get response from handler chain"""
    def __init__(self, handlers, request):
        self.handlers = handlers
        self.request = request
        self.chain_starter = None

    def build(self):
        head = self.handlers.pop(0)
        temp = head
        for h in self.handlers:
            temp.set_next(h)
            temp = h

        self.chain_starter = head

    def get_response(self):
        return self.chain_starter.handle(self.request)


class Request:
    def __init__(self, method, is_logged, is_admin, url):
        self.method = method
        self.is_user_logged = is_logged
        self.is_user_admin = is_admin
        self.url = url


get_admin_panel_requested_by_admin = Request(method='get', is_logged=True, is_admin=True, url='https://admin.com')
handler_chain = HandlerChain([HTTPGetWebRequestHandler(), LoggedWebRequestHandler(), AdminStatusWebRequestHandler()],
                             get_admin_panel_requested_by_admin)
handler_chain.build()
print(handler_chain.get_response())
# Access granted for url: https://admin.com

bad_method_request = Request(method='post', is_logged=True, is_admin=False, url='https://google.com')
handler_chain = HandlerChain([HTTPGetWebRequestHandler(), LoggedWebRequestHandler()], bad_method_request)
handler_chain.build()
print(handler_chain.get_response())
# Bad HTTP method.

get_profile_settings_requested_by_guest = Request(method='get', is_logged=False, is_admin=False, url='https://people.com/profile-settings')
handler_chain = HandlerChain([HTTPGetWebRequestHandler(), LoggedWebRequestHandler()], get_profile_settings_requested_by_guest)
handler_chain.build()
print(handler_chain.get_response())
# User is not logged.
