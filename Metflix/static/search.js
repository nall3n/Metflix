

// Make link of element
function clickLink(item) {
    window.location = item.getAttribute('data-href');
}


// Drop down search
$(document).ready(function () {
    $('.selectSearch').select2();
});

//Pagination
$(document).ready(function () {
    $('#data').after('<div id="nav"></div>');
    var rowsShown = 5;
    var rowsTotal = $('#data tbody tr').length;
    var numPages = rowsTotal / rowsShown;
    for (i = 0; i < numPages; i++) {
        var pageNum = i + 1;
        $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
    }
    $('#data tbody tr').hide();
    $('#data tbody tr').slice(0, rowsShown).show();
    $('#nav a:first').addClass('active');
    $('#nav a').bind('click', function () {

        $('#nav a').removeClass('active');
        $(this).addClass('active');
        var currPage = $(this).attr('rel');
        var startItem = currPage * rowsShown;
        var endItem = startItem + rowsShown;
        $('#data tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
            css('display', 'table-row').animate({ opacity: 1 }, 300);
    });
});








function showActive() {

    var active = document.getElementsByClassName("False");
    var closed = document.getElementsByClassName("True");
    console.log(active);
    for (i = 0; i < closed.length; i++) {
        closed[i].classList.add("hide");
        console.log("TEST2");
    }
    for (i = 0; i < active.length; i++) {
        active[i].classList.remove('hide');
    }
}

function showClosed() {

    var active = document.getElementsByClassName("False");
    var closed = document.getElementsByClassName("True");
    console.log(closed);
    for (i = 0; i < closed.length; i++) {
        closed[i].classList.remove("hide");
        console.log("TEST3");
    }
    for (i = 0; i < active.length; i++) {
        active[i].classList.add('hide');
    }
}

function showAll() {

    var active = document.getElementsByClassName("False");
    var closed = document.getElementsByClassName("True");

    for (i = 0; i < closed.length; i++) {
        closed[i].classList.remove("hide");
    }
    for (i = 0; i < active.length; i++) {
        active[i].classList.remove('hide');
    }
}

