create database todo_db;
use todo_db;

create table tasks (
	id int auto_increment primary key,
    title varchar(255) not null,
    completed boolean default false
);

show tables;

describe tasks;

insert into tasks(title, completed) values ("Learn Python TO-DO App", false);

select * from tasks;