$(function () {
    $("[id^=ans]").hide();
    $("#and-btn").click(function () {
        $("[id^=ans]").show();
        $("[id^=ans]").slideDown(5000);
    })
});
