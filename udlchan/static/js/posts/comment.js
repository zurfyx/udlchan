(function($) {

    var comment = {
        ajax: function(href, callback) {
            params = {'csrfmiddlewaretoken': 'TKERa2Ld2TZLLS4y7Tm8npCOTXeBCt0R'}
            $.post(href, params, function(data, err) {
                return callback(data);
            }).fail(function() {
                return callback('Error!');
            });
        },
        listener: function() {
            var self = this;
            $('p').click(function(e) {
                var voteObj = $(this);
                var href = '1/comment';
                e.preventDefault();

                self.ajax(href, function(data) {
                    console.log(data);
                });

            });
        },
        init: function() {
            this.listener();
        }
    };

    ///

    comment.init();

})(jQuery);