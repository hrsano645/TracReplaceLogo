// Trac ReplaceLogo Plugin main

// run after page load
$(window).load(function() {

    var trac_title;
    trac_title = $("meta[name=TracProjectTitle]").attr("content");

    console.log(trac_title);
    $("#logo img").replaceWith("<h1>" + trac_title + "</h1>");
});


