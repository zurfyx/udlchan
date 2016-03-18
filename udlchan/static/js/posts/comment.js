(function($) {

    var comment = {
        ajax: function(href, callback) {
            $.get(href, function(data, err) {
                return callback(data.votes);
            }).fail(function() {
                return callback('Error!');
            });
        },
        listener: function() {
            var self = this;
            $('p').click(function(e) {
                var voteObj = $(this);
                var href = 'topic/1/comment';
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