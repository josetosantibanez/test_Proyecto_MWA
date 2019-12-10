$(document).ready(function() {
    var qty = 0;
    $("#plus").click(function() {
      qty++;
      $("#id_cantidad_reservar").val(qty);
    });
    $("#minus").click(function() {
      if (qty > 0) {
        qty--;
        $("#id_cantidad_reservar").val(qty);
      }
    });
  
    $("#info").click(function() {
      $("#pop").show("fast");
      $("#main").hide("fast");
    });
  
    $("#close").click(function() {
      $("#pop").hide("fast");
      $("#main").show("fast");
    });
  });