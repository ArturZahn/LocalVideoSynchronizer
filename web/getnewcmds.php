<?php

include("./conexao.php");

// first of all, remove old commands from database
mysqli_query($con, "CALL deleteOldCmds;");


if(empty($_GET["id"]))
{
    // if id was not provided, return error
    http_response_code(400);
    echo "Id not informed";
    die();
}
$id = $_GET["id"];

$qstr = "SELECT `cmd_cod`, `numb`, `opt` FROM `cmd` WHERE `cmd_cod` NOT IN ( SELECT `cmd_cod` FROM `cmd_executed` WHERE `id` = $id )";
$q = mysqli_query($con, $qstr);

$cmds = [];

if(mysqli_num_rows($q) > 0)
{
    $queryInsert = "INSERT INTO `cmd_executed` (`id`, `cmd_cod`) VALUES ";

    while($e = mysqli_fetch_object($q))
    {
        $cmds[] = $e;
        $queryInsert .= "($id, $e->cmd_cod),";
    }

    $queryInsert = substr($queryInsert, 0, strlen($queryInsert)-1);

    mysqli_query($con, $queryInsert);
}



echo json_encode($cmds);

// echo json_encode(Array(
//     "mensagem" => $queryInsert
// ));

?>