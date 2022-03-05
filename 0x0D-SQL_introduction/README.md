# SQL INTRODUCTION

This project covers the basics of MYSQL to some inntermediate.

## General

What’s a database
What’s a relational database
What does SQL stand for
What’s MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions

## HOW TO INSTALL MY SQL 8.0 ON UBUNTU 20.04

$ sudo apt update

$ sudo apt install mysql-server

...

$ mysql --version

mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

$

## Conect to your MySQL server:

$ sudo mysql

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 11

Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)


Copyright (c) 2000, 2021, Oracle and/or its affiliates.


Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.


Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.


mysql>

mysql> quit

Bye

$

## Use “container-on-demand” to run MySQL

In the container, credentials are root/root

<ul>
<li>Ask for container Ubuntu 20.04</li>

<li>Connect via SSH</li>

<li>OR connect via the Web terminal</li>

<li>In the container, you should start MySQL before playing with it:</li>


$ service mysql start

 * Starting MySQL database server mysqld

$

$ cat 0-list_databases.sql | mysql -uroot -p

Database

information_schema

mysql

performance_schema

sys

$
