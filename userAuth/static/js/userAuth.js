$(document).ready(function() {
    $('#id_intern').on('change', function() {
        var selected_id = $(this).val();
        $.ajax({
            url: '/get-name/',
            data: {
                'uuid': selected_id
            },
            dataType: 'json',
            success: function(data) {
                $('#id_intern_name').val(data.name);
            }
        });
    });
});
