#!/usr/bin/env node
$(document).ready(function () {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
        $("#hello").text(data.hello);
    });
});