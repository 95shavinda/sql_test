create database user;
 
create table tbluser(username varchar(32) primary key, password varchar(32));
 
insert into tbluser (username,password) values ('john','secret');
insert into tbluser (username,password) values ('mike','pass10');
