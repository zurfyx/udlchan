(function($) {
    /** Submit comment form, then adds it into the HTML. **/

    var ELEMENT = 'form.new-comment';

    function processAJAXData(data) {
        if (data.status === 'error') {
            alert(data.message);
            return;
        }
        console.log('Successfully posted! :-)');
    }

    function listener() {
        $('body').on('submit', ELEMENT, function(e) {
            var href = $(this).attr('action');
            var data = $(this).serialize();
            e.preventDefault();

            $.post(href, data, processAJAXData).fail(function() {
                alert('Failed to retrieve data from the server.');
            });
        });
    }

    ///

    listener();

})(jQuery);