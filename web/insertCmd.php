<?php

if(empty($_GET["numb"]) || empty($_GET["opt"]))
{
    http_response_code(400);
    die();
}

$numb = $_GET["numb"];
$opt = json_encode($_GET["opt"]);

var_dump($opt);

include("conexao.php");

mysqli_query($con, "INSERT INTO cmd (numb, opt) VALUES ($numb, '$opt')");

?>