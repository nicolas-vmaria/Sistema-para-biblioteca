<?php

require_once "../../config/conexao.php";

if($_SERVER["REQUEST_METHOD"] == "POST"){
    try{
        $nome = $_POST['nome'];
        $email = $_POST['email'];
        $senha = $_POST['senha'];

        $stmtCheck = $pdo->prepare("select 1 from usuarios where email = :email");
        $stmtCheck->execute([':email' => $email]);

        if($stmtCheck->fetch()){
            echo "Este email jé foi cadastrado.";
            exit;
        }

        $hashSenha = password_hash($senha,PASSWORD_DEFAULT);

        $stmt= $pdo->prepare("insert into usuarios (nome,email,senha) values (:nome,:email,:senha)");
        $stmt->execute([
            ':nome' => $_POST['nome'],
            ':email' => $_POST['email'],
            ':senha' => $hashSenha
        ]);
    
        header("Location: ../html/index.html");
        exit;
    }catch(Exception $e){
    echo $e->getMessage();
    }
}else{
    echo "Erro ao enviar formulário";
}