$(document).ready(()=>{
    $("#vid_open").click(openLink);
    $("#vid_pred").change(predChanged)
    $("#vid_link").change(linkChanged)

    $("#vid_play").click(()=>{
        sendCmd(2, {act: "k"});
    });
    // $("#vid_play").click(()=>{
    //     sendCmd(2, {act: "p"});
    // });
    $("#vid_esc").click(()=>{
        sendCmd(2, {act: "e"});
    });
    $("#vid_begining").click(()=>{
        sendCmd(2, {act: "b"});
    });
    $("#vid_fullscreen").click(()=>{
        sendCmd(2, {act: "f"});
    });
    $("#vid_ekbf").click(()=>{
        sendCmd(2, {act: "ekbf"});
    });


    $("#vol_globalvalbtn").click(setGlobalVolVal);

    $("#vol_globalMax").click(()=>{
        sendCmd(3, {mode: 2});
    });
    $("#vol_globalMin").click(()=>{
        sendCmd(3, {mode: 3});
    });

    $("#vol_globalMaxF").click(()=>{
        sendCmd(3, {mode: 4});
    });
    $("#vol_globalMinF").click(()=>{
        sendCmd(3, {mode: 5});
    });

    $("#vol_indvvalbtn").click(setIndvVolVal);

    $("#vol_indvMax").click(()=>{
        sendCmd(3, {mode: 7});
    });
    $("#vol_indvMin").click(()=>{
        sendCmd(3, {mode: 8});
    });

    $("#vid_forward").click(forwardclicked);
    $("#vid_temp").change(tempchanged);
    $("#vid_back").click(backclicked);

    $("#vid_newchrome").click(()=>{
        sendCmd(4, {act: "n"})
    });
    $("#vid_altf4").click(()=>{
        sendCmd(4, {act: "f"})
    });
    $("#vid_newtab").click(()=>{
        sendCmd(4, {act: "t"})
    });
    $("#vid_closetab").click(()=>{
        sendCmd(4, {act: "c"})
    });
    $("#vid_prevtab").click(()=>{
        sendCmd(4, {act: "<"})
    });
    $("#vid_nexttab").click(()=>{
        sendCmd(4, {act: ">"})
    });
});


function sendCmd(numb, opt)
{
    $.get({
        url: "./insertCmd.php",
        data: {numb: numb, opt: opt},
        complete: (request)=>{
            console.log("status:" + request.statusText)
            console.log(request.responseText)
        }
    })
}

function openLink()
{
    var url = $.trim($("#vid_link").val());

    if(url.length == 0) return;

    sendCmd(1, {url: url});
}

function predChanged()
{
    vid = $("#vid_pred").val();
    if(vid != "")
    {
        $("#vid_link").val(vid);
    }
}
function linkChanged()
{
    $("#vid_pred option:first-child").prop("selected", true)
}



function setGlobalVolVal()
{
    var val = $("#vol_globalvalval").val();
    sendCmd(3, {mode: 1, val: val});
}

function setIndvVolVal()
{
    var val = $("#vol_indvvalval").val();
    sendCmd(3, {mode: 6, val: val});
}

function get_vidtemp()
{
    var val = parseInt($("#vid_temp").val());
    val = Math.round(val/5)*5;
    $("#vid_temp").val(val);
    return val;
}
function tempchanged()
{
    var val = get_vidtemp();
    $("#vid_forward").val(`+${val}s`)
    $("#vid_back").val(`-${val}s`)
}
function forwardclicked()
{
    vid_move(">");
}
function backclicked()
{
    vid_move("<");
}
function vid_move(letter)
{
    var val = get_vidtemp()/5;
    var str = letter.repeat(Math.abs(val));
    sendCmd(2, {act: str});
}