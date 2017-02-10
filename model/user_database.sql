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
	`Group_ID`	INTEGER,
	`Card` TEXT
);
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
INSERT INTO `Mentor` (ID,Name,Surname,Email,Date_of_birth,City,Phone,Login,Password) VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
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
INSERT INTO `Manager` (ID,Name,Surname,Email,Date_of_birth,City,Phone,login,password) VALUES (1,'Tomasz','Kowalski',NULL,NULL,NULL,NULL,'tok','1234');
CREATE TABLE "Groups" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Student_list`	TEXT,
	`Assignment_ID` INTEGER
);
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
INSERT INTO `Employee` (ID,Name,Surname,Email,Date_of_birth,City,Phone,login,password) VALUES (1,'Jan','Kowalik',NULL,NULL,NULL,NULL,'jak',NULL);
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
	`Answer_text`	TEXT,
	`grade` INTEGER

);
INSERT INTO `Answers` (ID,Student_ID,Answer_text) VALUES (1,4,'Square has four sides');
INSERT INTO `Answers` (ID,Student_ID,Answer_text) VALUES (2,2,'Circle is round');
COMMIT;
