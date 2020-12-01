function create_table (json) {
    var output = [];
    output.push("<table>");
    $.each(json, function(k, v) {
                output.push("<tr><td>");
                output.push(k);
                output.push("</td><td>");
                output.push(v);    
                output.push("</td></tr>");
    });
    output.push("</table>");

    $("#resume-table").append(output.join(""));

    $("#resume-table").find("table").dataTable();
}

$("#resume-form").submit(function (e) {
    e.preventDefault();
    var form = $(this);
    var data = new FormData(this);
    var url = form.attr('action');
    $.ajax({
        url: url,
        data: data,
        type: 'POST',
        success: function (data) {
            console.log(typeof(data));
            create_table(data);
        },
        error: function (err) {
            alert(err);
        },
        cache: false,
        contentType: false,
        processData: false
    });
});
