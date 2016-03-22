(function($) {
    /** Submit comment form, then adds it into the HTML. **/

    var COMMENT_ELEMENT = '.element';
    var ELEMENT = 'form.new-comment';
    var REPLY_FORM = '.reply-form';
    var REPLY_LOG =  '.reply-log';

    function processAJAXData(ajaxData, form) {
        if (ajaxData.status === 'error') {
            alert(data.message);
            return;
        }

        // log
        var reply_log = '<span>Replied: ' + form.find('[name="content"]').val() + '</span>';
        form.closest(COMMENT_ELEMENT).find(REPLY_LOG).append(reply_log);

        // clear form
        console.log(form.find('[name="parent"]') )
        if (form.find('[name="parent"]').val() == '') {
            form.find('[name="content"]').val('');
        } else {
            form.closest(REPLY_FORM).html('');
        }
    }

    function listener() {
        $('body').on('submit', ELEMENT, function(e) {
            var form = $(this);
            var href = form.attr('action');
            var data = form.serialize();
            e.preventDefault();

            $.post(href, data, function(ajaxData) {
                processAJAXData(ajaxData, form);
            }).fail(function() {
                alert('Failed to retrieve data from the server.');
            });
        });
    }

    ///

    listener();

})(jQuery);