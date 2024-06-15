
$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});

$(document).on("click", ".js-toggle-modal", function (e) {
    e.preventDefault()
    $(".js-modal").toggleClass("hidden")
})
    .on("click", ".js-submit", function (e) {
        e.preventDefault()
        const text = $(".js-post-text").val().trim()
        const $btn = $(this)

        if (!text.length) {
            return false
        }

        $btn.prop("disabled", true).text("Posting!")
        $.ajax({
            type: 'POST',
            url: $(".js-post-text").data("post-url"),
            data: {
                text: text
            },
            success: (dataHtml) => {
                $(".js-modal").addClass("hidden");
                $("#posts-container").prepend(dataHtml);
                $btn.prop("disabled", false).text("New Post");
                $(".js-post-text").val('')
            },
            error: (error) => {
                console.warn(error)
                $btn.prop("disabled", false).text("Error");
            }
        });
    })
    .on("click", ".js-follow", function (e) {
        e.preventDefault();
        const action = $(this).attr("data-action")

        $.ajax({
            type: 'POST',
            url: $(this).data("url"),
            data: {
                action: action,
                username: $(this).data("username"),
            },
            success: (data) => {
                $(".js-follow-text").text(data.wording)
                if (action == "follow") {
                    // Change wording to unfollow
                    console.log("DEBUG", "unfollow")
                    $(this).attr("data-action", "unfollow")
                } else {
                    // The opposite
                    console.log("DEBUG", "follow")
                    $(this).attr("data-action", "follow")
                }
            },
            error: (error) => {
                console.warn(error)
            }
        });
    })

    .on("click", ".js-submit-feed", function (e) {
        e.preventDefault()
        const text = $(".js-post-text").val().trim()
        const btn = $(this)
        console.log(text)


        if (!text.length) {
            console.log("Sunmit Me")
            return false
        }

        // $btn.prop("disabled", true).text("Posting")
        document.getElementById("post-feed-button").innerHTML = "Posting";
        $.ajax({
            type: 'POST',
            url: $(".js-post-text").data("post_url"),
            data: {
                text: text
            },
            success: (datahtml) => {
                $(".js-modal").addClass("hidden");
                $("#posts-container").prepend(dataHtml);
                $btn.prop("disabled", false).text("New Post")
                $(".js-post-text").val('')

            },
            error: (error) => {

            }
        })
    }
    )