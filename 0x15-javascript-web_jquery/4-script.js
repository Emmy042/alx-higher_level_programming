#!/usr/bin/env node
$(".green").click(function() {
    if ($(this).hasClass("red")) {
        $(this).removeClass("red").addClass("green")
    } else {
        $(this).removeClass("green").addClass("red")
    }
});