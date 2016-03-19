(function($) {
    /** Generates new form for the comment HTML element **/
    var ORIGINAL_FORM = $('.new_comment')[0];
    var COMMENT_ELEMENT = '.element';
    var REPLY_FORM = '.reply-form';
    var REPLY_CANCEL = '.reply-cancel';
    var REPLY_CANCEL_CLASS = 'reply-cancel';

    var write_form = {
        update_parent: function() {
            // TODO
        },
        append_cancel_button: function() {
            var cancel_button = '' +
                '<button class="'+REPLY_CANCEL_CLASS+'">' +
                'Cancel' +
                '</button>';
            this.form.find('button').parent().prepend(cancel_button);
        },
        init: function(element) {
            this.form = $(ORIGINAL_FORM).clone();
            this.append_cancel_button();
            element.html(this.form);
        }
    }

    function listener_reply() {
        $('a.do-reply').click(function(e) {
            e.preventDefault();
            var replyForm = $(this).closest(COMMENT_ELEMENT).find(REPLY_FORM);
            write_form.init(replyForm);
        });
    }

    function listener_cancel() {
        $(document).on('click', REPLY_CANCEL, function(e) {
            e.preventDefault();
            $(this).closest(REPLY_FORM).html('');
        });
    }

    ///

    listener_reply();
    listener_cancel();

})(jQuery);