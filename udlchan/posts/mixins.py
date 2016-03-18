from django.http import JsonResponse

class CommentAddAJAXMixin(object):
    """
    AJAX response to create topic.
    """
    #@ajax_required
    def form_valid(self):
        pass

    def form_invalid(self):
        return JsonResponse({
            'msg': 'hello'
        })

