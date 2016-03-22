from django.http import JsonResponse
from .decorators import ajax_required


class CommentAddAJAXMixin(object):
    """
    AJAX response to create topic.
    """
    @ajax_required
    def get(self, request, *args, **kwargs):
        pass

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'status': 'success'
        })

    def form_invalid(self, form):
        return JsonResponse({
            'status': 'error',
            'data': form.errors,
            'message': 'Form validated with errors.'
        })

