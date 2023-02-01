#!/usr/bin/node
// a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag
$('div#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
