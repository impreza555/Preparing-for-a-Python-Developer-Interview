$(function () {
    let loadForm = function () {
        let btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                console.log("Форма загружается");
                $('.modal').modal();
            },
            success: function (data) {
                console.log(data);
                $("#modal1 .modal-content").html(data.html_form);
                console.log("Форма загружена");
            },

        });
    };

    let saveForm = function () {
        let form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $(".product-table").html(data.html_good_list);
                    $("#modal1").modal("close");
                } else {
                    $("#modal1 .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    $(".modal-trigger").click(loadForm);
    $("#modal1").on("submit", ".js-good-create-form", saveForm);

});
