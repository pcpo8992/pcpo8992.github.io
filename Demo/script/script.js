$(function () {
    $("[id^=ans]").hide();
    $("#and-btn").click(function () {
        $("[id^=ans]").slideDown(3000);
    })
});
