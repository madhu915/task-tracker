$(document).ready(function () {
  $("#id_intern").on("change", function () {
    var selected_id = $(this).val();
    $.ajax({
      url: "/get-name/",
      data: {
        uuid: selected_id,
      },
      dataType: "json",
      success: function (data) {
        $("#id_intern_name").val(data.name);
      },
    });
  });
});

jQuery(document).ready(function($) {
  $('*[data-href]').on('click', function() {
      window.location = $(this).data("href");
  });
});

var check = function () {
  if (
    document.getElementById("password").value ==
    document.getElementById("password-verify").value
  ) {
    if (document.getElementById("password").value == "") {
      document.getElementById("ico").style.display = "none";
      document.getElementById("cross").style.display = "none";
      document.getElementById("message").style.display = "none";
      document.getElementById("reset").disabled=true;
    } else {
      document.getElementById("ico").style.display = "block";
      document.getElementById("cross").style.display = "none";
      document.getElementById("message").style.display = "block";
      document.getElementById("message").innerHTML = "Passwords Match!";
      document.getElementById("message").style.color = "rgb(21, 226, 21)";
      document.getElementById("reset").disabled=false;
    }
  } else {
    document.getElementById("ico").style.display = "none";
    document.getElementById("cross").style.display = "block";
    document.getElementById("message").style.display = "block";
    document.getElementById("message").innerHTML = "Passwords do not match!";
    document.getElementById("message").style.color = "#ff2c39";
    document.getElementById("reset").disabled=true;
  }
};
