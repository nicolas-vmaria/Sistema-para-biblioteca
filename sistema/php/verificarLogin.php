<?php

require_once "../../config/conexao.php";

if($_SERVER["REQUEST_METHOD"] == "POST"){
    try{
        $email = $_POST['email'];
        $senha = $_POST['senha'];

        
    
        header("Location: ../html/index.html");
        exit;
    }catch(Exception $e){
        echo $e->getMessage();
    }
}else{
    echo "Erro ao enviar formulário";
}