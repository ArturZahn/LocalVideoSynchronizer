<?php

if(isset($_GET["data"]))
{
    include("./conexao.php");

    // first of all, remove old commands from database
    mysqli_query($con, "CALL deleteOldCmds;");

    $q = mysqli_query($con, "SELECT numb, opt, dt_created FROM cmd");


    while($e = mysqli_fetch_array($q))
    {
        echo "<tr><td>$e[numb]</td><td>$e[opt]</td><td>$e[dt_created]</td></tr>";
    }

    die();
}

?>

<script src="./assets/js/jquery-3.6.0.min.js"></script>
<script>

    setInterval(() => {
        $.ajax({
            url: "./actions.php?data",
            success: (data)=>{
                $("#tab").html(data);
            }
        })
    }, 200);

</script>
<a href="./">voltar</a>
<table id="tab" border="1">
</table>