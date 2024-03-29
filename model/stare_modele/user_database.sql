BEGIN TRANSACTION;
CREATE TABLE "Student" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` TEXT,
	`Attendance_level` TEXT,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT,
	`Group_ID`	INTEGER,
	`Card` TEXT
);
INSERT INTO `Student` (Name,Surname,Login,Password) VALUES ('Marek','Dupa','m@s','dupa');
INSERT INTO `Student` (Name,Surname,Login,Password) VALUES ('Jadzia','Worek','j@s','dupa');
INSERT INTO `Student` (Name,Surname,Login,Password) VALUES ('Kili','walis','k@s','dupa');
CREATE TABLE "Mentor" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` TEXT,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT
);
INSERT INTO `Mentor` (Name,Surname,Login,Password) VALUES ('Marcin','Izworski','marcin@m','dupa');
INSERT INTO `Mentor` (Name,Surname,Login,Password) VALUES ('Przemysław','Ciąćka','przemek@m','dupa');
INSERT INTO `Mentor` (Name,Surname,Login,Password) VALUES ('Mentor','Mentorowski','mentor@m','dupa');
CREATE TABLE `Manager` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` TEXT,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT
);
INSERT INTO `Manager` (Name,Surname,Login,Password) VALUES ('Jurek','Jurkowski','jurek@j','dupa');
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
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` TEXT,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT
);
INSERT INTO `Employee` (Name,Surname,Login,Password) VALUES ('Miriam','Niewiem','miriam@e','dupa');
INSERT INTO `Employee` (Name,Surname,Login,Password) VALUES ('Kati','Niewiem','kati@e','dupa');
INSERT INTO `Employee` (Name,Surname,Login,Password) VALUES ('Sprzataczka','Sprzataczkowska','lol@e','dupa');


CREATE TABLE `Attendance` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Student_ID`	INTEGER,
	 Date	INTEGER,
	`Attendance_value` TEXT
);
CREATE TABLE `Assignments` (	
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Description`	TEXT,
	`Student_ID`	INTEGER
);
INSERT INTO `Assignments` (ID,Name,Description,Student_ID) VALUES (1,'Square','Find the area of a square with a given side',1);
CREATE TABLE `Answers` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Answer_text`	TEXT,
	`Grade`	TEXT,
	`Student_ID`	INTEGER,
	`Assignment_id`	INTEGER
);
INSERT INTO `Answers` (ID,Answer_text,Grade,Student_ID,Assignment_id) VALUES (1,'Square has four sides',6,1,1);
INSERT INTO `Answers` (ID,Answer_text,Grade,Student_ID,Assignment_id) VALUES (2,'Circle is round',5,1,2);
COMMIT;
