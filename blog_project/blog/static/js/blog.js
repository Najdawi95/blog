$(document).ready(function () {
    $(".convert-to-grid-view").click(function () {
        $(this).hide();
        $(".convert-to-list-view").removeClass("d-none");
        $(".product-row").addClass("col-6");
        $(".product-row").removeClass("col-12");
        $(".product-row").removeClass("m-md-1");


        $(".logo-cell").removeClass("col-md-2");
        $(".logo-cell").addClass("col-md-3");

        $(".price-cell").removeClass("col-md-4");
        $(".price-cell").addClass("col-md-3");

    });
});

$(document).ready(function () {
    $(".convert-to-list-view").click(function () {
        $(this).addClass("d-none");
        $(".convert-to-grid-view").show();
        $(".product-row").addClass("col-12");
        $(".product-row").addClass("m-md-1");


        $(".logo-cell").removeClass("col-md-3");
        $(".logo-cell").addClass("col-md-2");

        $(".price-cell").removeClass("col-md-3");
        $(".price-cell").addClass("col-md-4");
    });
});