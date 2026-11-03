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
data_emprestimo date not null,
data_devolucao date,
usuario_id int not null,
livro_id int not null,

foreign key (usuario_id) references usuarios(id),
foreign key (livro_id) references livros(id)
);

insert ignore into categorias (nome) values ("Terror"),("Drama"),("Comédia");

insert into livros (titulo, autor, categoria_id, quantidade)
select 'O Iluminado', 'Stephen King', c.id, 5
from categorias c
left join livros l on l.titulo = 'O Iluminado'
where c.nome = 'Terror' and l.id is null;

insert into livros (titulo, autor, categoria_id, quantidade)
select 'Extraordinário', 'R. J. Palacio', c.id, 4
from categorias c
left join livros l on l.titulo = 'Extraordinário'
where c.nome = 'Drama' and l.id is null;

insert into livros (titulo, autor, categoria_id, quantidade)
select 'O Auto da Compadecida', 'Ariano Suassuna', c.id, 3
from categorias c
left join livros l on l.titulo = 'O Auto da Compadecida'
where c.nome = 'Comédia' and l.id is null;

select * from livros