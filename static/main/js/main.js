$('.counter').each(function () {
    $(this).prop('Counter', 0).animate({
        Counter: $(this).text()
    }, {
        duration: 4000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
});

$(document).on('click', '.pg', () => {
    $.ajax({
        type: "GET",
        headers: {
            "X-CSRFToken": csrftoken,
        },
        url: $(".get_page").val(),
        data: {
            "get_page": "get_page"
        },
        success: function (response) {
            $(".news_cards").empty();
            $(".news_cards").html(response);
            window.history.pushState("object or string", "Title", `?page=${$(".pg").attr("data-pagenumper")}`);
            var elem = document.getElementById("topNew");
            elem.scrollIntoView();
        }
    });
})