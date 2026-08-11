create database if not exists biblioteca;
use biblioteca;

create table if not exists usuarios(
id int auto_increment primary key,
nome varchar(255),
email varchar(255) unique,
senha varchar(255)
);

create table if not exists categorias(
id int auto_increment primary key,
nome varchar(255) unique
);

create table if not exists livros(
id int auto_increment primary key,
titulo varchar(255) not null,
autor varchar(255) not null,
categoria_id int not null,
quantidade int not null,

foreign key (categoria_id) references categorias(id) 
);

create table if not exists emprestimos(
id int auto_increment primary key,
estado enum("emprestado","devolvido"),
data_emprestimo date not null,
data_devolucao date,
usuario_id int not null,
livro_id int not null,

foreign key (usuario_id) references usuarios(id),
foreign key (livro_id) references livros(id)
);

insert into categorias (nome) values ("Terror"),("Drama"),("Comédia");
insert into livros (titulo, autor, categoria_id, quantidade) values
('O Iluminado', 'Stephen King', 1, 5),
('Extraordinário', 'R. J. Palacio', 2, 4),
('O Auto da Compadecida', 'Ariano Suassuna', 3, 3);

select * from livros