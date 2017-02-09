BEGIN TRANSACTION;
CREATE TABLE `Student` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Imie`	TEXT,
	`Nazwisko`	TEXT,
	`Wiek`	INTEGER,
	`Login`	TEXT UNIQUE,
	`Haslo`	TEXT,
	`Group_ID`	INTEGER
);
INSERT INTO `Student` (ID,Imie,Nazwisko,Wiek,Login,Haslo,Group_ID) VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL);
CREATE TABLE `Mentor` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Imię`	TEXT,
	`Nazwisko`	TEXT,
	`Login`	TEXT UNIQUE,
	`Hasło`	TEXT
);
INSERT INTO `Mentor` (ID,Imię,Nazwisko,Login,Hasło) VALUES (1,NULL,NULL,NULL,NULL);
CREATE TABLE `Manager` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`surname`	TEXT,
	`login`	TEXT UNIQUE,
	`password`	TEXT
);
INSERT INTO `Manager` (ID,name,surname,login,password) VALUES (1,'Tomasz','Kowalski','tok','1234');
CREATE TABLE `Groups` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Assignment_ID`	INTEGER
);
INSERT INTO `Groups` (ID,Name,Assignment_ID) VALUES (1,NULL,NULL);
CREATE TABLE `Employee` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`login`	TEXT UNIQUE,
	`password`	TEXT
);
INSERT INTO `Employee` (ID,Name,Surname,login,password) VALUES (1,'Jan','Kowalik','jak',NULL);
CREATE TABLE `Attendance` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Day`	INTEGER,
	`Month`	INTEGER,
	`Year`	INTEGER,
	`Status`	TEXT,
	`Student_ID`	INTEGER
);
INSERT INTO `Attendance` (ID,Day,Month,Year,Status,Student_ID) VALUES (1,25,11,2016,'present',NULL);
INSERT INTO `Attendance` (ID,Day,Month,Year,Status,Student_ID) VALUES (2,26,11,2016,'late',NULL);
INSERT INTO `Attendance` (ID,Day,Month,Year,Status,Student_ID) VALUES (3,27,11,2016,'present',NULL);
INSERT INTO `Attendance` (ID,Day,Month,Year,Status,Student_ID) VALUES (4,29,11,2016,'present',NULL);
CREATE TABLE `Assignments` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Description`	TEXT,
	`Student_ID`	INTEGER
);
INSERT INTO `Assignments` (ID,Name,Description,Student_ID) VALUES (1,'Square','Find the area of a square with a given side',1);
CREATE TABLE `Answers` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Student_ID`	INTEGER,
	`Answer_text`	TEXT
);
INSERT INTO `Answers` (ID,Student_ID,Answer_text) VALUES (1,4,'Square has four sides');
INSERT INTO `Answers` (ID,Student_ID,Answer_text) VALUES (2,2,'Circle is round');
COMMIT;
