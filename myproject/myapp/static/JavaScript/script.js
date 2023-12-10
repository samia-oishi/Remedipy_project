$(function () {
    $('.alternate').click(function () {
        console.log('Toggle clicked!');
        $('form').animate({ height: "toggle", opacity: "toggle" }, "slow", function() {
            console.log('Animation complete!');
        });
    });
});
