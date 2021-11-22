<?php

include("./conexao.php");
include("./mysqlDate.php");

if(empty($_GET["ip"]))
{
    // if ip was not provided, return error
    http_response_code(400);
    echo "Ip not informed";
    die();
}
$ip = $_GET["ip"];

if(empty($_GET["lastConnDate"]))
{
    // if last connection date is not provided, we cannot trust the id
    $_GET["id"] = "";
}
else
{
    // if last connection date is older than the last database reset, discard old id
    $lastConnDate = $_GET["lastConnDate"];
    $q = mysqli_query($con, "SELECT `time`, `time` >= '$lastConnDate' AS newIdIsneeded FROM `lastreset`");

    if(mysqli_fetch_array($q)["newIdIsneeded"] == "1") $_GET["id"] = "";
}


if(empty($_GET["id"]))
{
    // if id was not provided, creates a new id and return it along with current date
    insertAndReturnIdDate();
    die();
}
$id = $_GET["id"];

// if id was provided, verify if it exists...
$q = mysqli_query($con, "SELECT `id` FROM `connection` WHERE `id` = $id");

if(mysqli_num_rows($q) == 0)
{
    // if not, creates a new id and return it along with current date...
    insertAndReturnIdDate();
    die();
}

// and if so, update ip and return id along with current date...
$q = mysqli_query($con, "UPDATE `connection` SET `ip` = '$ip' WHERE `id` = $id");
returnIdDate($id);




function insertAndReturnIdDate()
{
    $q = mysqli_query($GLOBALS['con'], "INSERT INTO `connection` (`ip`) VALUES ('$GLOBALS[ip]')");
    returnIdDate(mysqli_insert_id($GLOBALS['con']));
}

function returnIdDate($rId)
{
    echo json_encode(array(
        'id' => $rId,
        'date' => mysqlDate($GLOBALS['con'])
    ));
}

?>