(function($) {

    var ELEMENT = $('form.new_comment');

    function processAJAXData(data) {
        if (data.status === 'error') {
            alert(data.message);
            return;
        }
        console.log('Successfully posted! :-)');
    }

    function listener() {
        ELEMENT.submit(function(e) {
            var href = $(this).attr('action')
            var data = $(this).serialize();
            e.preventDefault();

            $.post(href, data, processAJAXData).fail(function() {
                alert('Failed to retrieve data');
            });
        });
    }

    ///

    listener();

})(jQuery);