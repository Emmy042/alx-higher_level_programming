#!/usr/bin/env node
$("#add_item").click(function(e) {
    e.preventDefault();
    $(".my_list").append("<li>New item</li>");
});