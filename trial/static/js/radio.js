function isChecked()
{
    var checkedYes = document.getElementById('type1').checked;
    var checkedNo = document.getElementById('type2').checked;
    var checkedreport = document.getElementById('report-0').checked;
    var checkedcomplain = document.getElementById('report-1').checked;

    if(checkedYes == false && checkedNo == false)
    {
        var msg = '<span style="color:#a94442;">Please an option</span><br>';
        document.getElementById('msg').innerHTML = msg;
        //alert('You need to select an option!');
        return false;
    }
    else if(checkedreport == false && checkedcomplain == false)
    {
        var message = '<span style="color:#a94442;">Please select an option</span><br>';
        document.getElementById('message').innerHTML = message;
        //alert('You need to select an option!');
        return false;
    }
    else
    {
        return true;
    }
}

function reset_msg() {
    document.getElementById('msg').innerHTML = '';
}

