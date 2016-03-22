from django.http import Http404


def ajax_required(func):
    def func_wrapper(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404("Not an AJAX request")
        return func(self, request, *args, **kwargs)

    return func_wrapper
