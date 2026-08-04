<?php

$host="localhost";
$dbname="biblioteca";
$user="root";
$senha="";
$port=3306;

try{
    $pdo= new PDO("mysql:host=$host;dbname=$dbname;charset=utf8;port=$port", $user, $senha);

    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}catch (PDOException $e){
    die("Erro na conexão:" . $e->getMessage());
}
