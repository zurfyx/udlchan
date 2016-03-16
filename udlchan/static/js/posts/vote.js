(function($) {

    var vote = {
        ajax: function(href, callback) {
            $.get(href, function(data, err) {
                return callback(data.votes);
            }).fail(function() {
                return callback('Error!');
            });
        },
        listener: function() {
            var self = this;
            $('.vote').click(function(e) {
                var voteObj = $(this);
                var href = voteObj.attr('href');
                e.preventDefault();

                self.ajax(href, function(data) {
                    voteObj.next('.vote_label').text(data);
                });

            });
        },
        init: function() {
            this.listener();
        }
    };

    ///

    vote.init();

})(jQuery);