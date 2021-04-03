const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// FadeOut the error message for 3 seconds
setTimeout(function () {
    $('#message').fadeOut('slow')
}, 3000);
