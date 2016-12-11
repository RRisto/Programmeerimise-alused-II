var Courses = {
    init: function () {
        Courses.init_user_actions();
    },

    init_user_actions: function () {
        var userHud = $('#user-hud');
        var actionsButton = userHud.find('.user-actions-button');
        var actions = userHud.find('.user-actions');

        var discard = function () {
            actionsButton.removeClass('active');
            actions.removeClass('open');
        };

        actionsButton.click(function () {
            if (!actionsButton.hasClass('active')) {
                actionsButton.addClass('active');
                actions.addClass('open');
                setTimeout(function() { $(document).one('click', discard); }, 0); // defer
            }
            else
                discard();
            return false;
        });
    }
};

$(Courses.init);