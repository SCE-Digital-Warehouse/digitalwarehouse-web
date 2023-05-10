function toggleZoomScreen() {
    document.body.style.zoom = (1 / window.devicePixelRatio);
}


$(document).ready(function () {
    $('.sub-btn').click(function () {
        $(this).next('.sub-menu').slideToggle();
    });
});