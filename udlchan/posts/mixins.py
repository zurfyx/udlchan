from django.http import JsonResponse

class CommentAddAJAXMixin(object):
    """
    AJAX response to create topic.
    """
    #@ajax_required
    def form_valid(self, form):
        print 'bye'

    def form_invalid(self, form):
        return JsonResponse({
            'error': 'Invalid form',
            'errors': form.errors
        })

