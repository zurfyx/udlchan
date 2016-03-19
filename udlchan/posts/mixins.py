from django.http import JsonResponse
from django.core import serializers

class CommentAddAJAXMixin(object):
    """
    AJAX response to create topic.
    """
    #@ajax_required
    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'status': 'success'
        })

    #@ajax_required
    def form_invalid(self, form):
        return JsonResponse({
            'status': 'error',
            'data': form.errors,
            'message': 'Form validated with errors.'
        })

