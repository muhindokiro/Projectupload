$(document).ready(function() {

    var active1 = false;
    var active2 = false;
    var active3 = false;
    var active4 = false;

    $('.parent2').on('mousedown touchstart', function() {

        if (!active1) $(this).find('.test1').css({ 'background-color': 'gray', 'transform': 'translate(0px,125px)' });
        if (!active2) $(this).find('.test2').css({ 'background-color': 'gray', 'transform': 'translate(60px,105px)' });
        if (!active3) $(this).find('.test3').css({ 'background-color': 'gray', 'transform': 'translate(105px,60px)' });
        if (!active4) $(this).find('.test4').css({ 'background-color': 'gray', 'transform': 'translate(125px,0px)' });
        active1 = !active1;
        active2 = !active2;
        active3 = !active3;
        active4 = !active4;

    });
});