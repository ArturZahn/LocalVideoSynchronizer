<?php

function mysqlDate($conx)
{
    $qdate = mysqli_query($conx, "SELECT NOW() AS now");
    return mysqli_fetch_array($qdate)["now"];
}

?>