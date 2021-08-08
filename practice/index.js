$(function() {
    var today = new Date();
    var y = today.getFullYear();
    $('#calendar').multiDatesPicker({
        numberOfMonths: [4,3],
        defaultDate: '1/1/'+y
    });
});