BEGIN TRANSACTION;
CREATE TABLE "Student" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` INTEGER,
	`Attendance_level` INTEGER,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT,
	`Group_ID`	INTEGER
	`Card` TEXT
);
INSERT INTO `Student` (ID,Name,Surname,Age,Login,Password,Group_ID) VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL);
CREATE TABLE "Mentor" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` INTEGER,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT
);
INSERT INTO `Mentor` (ID,Name,Surname,Login,Password) VALUES (1,NULL,NULL,NULL,NULL);
CREATE TABLE `Manager` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` INTEGER,
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
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` INTEGER,
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
	`Answer_text`	TEXT,
	`Grade`	INTEGER,
	`Student_ID`	INTEGER,
	`Assignment_id`	INTEGER
);
INSERT INTO `Answers` (ID,Answer_text,Grade,Student_ID,Assignment_id) VALUES (1,'Square has four sides',6,1,1);
INSERT INTO `Answers` (ID,Answer_text,Grade,Student_ID,Assignment_id) VALUES (2,'Circle is round',5,1,2);
COMMIT;
