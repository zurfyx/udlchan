(function($) {

    var vote = {
        ajax: function(href, callback) {

        },
        listener: function() {
            $('.vote').click(function(e) {
                e.preventDefault();
                var voteObj = $(this);
                var href = voteObj.attr('href');
                $.get(href, function(data, err) {
                    $(voteObj.parent()).find('.vote_label').text(data.votes);
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