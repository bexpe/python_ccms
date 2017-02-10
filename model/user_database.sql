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
<<<<<<< HEAD
=======
INSERT INTO `Student` (Name,Surname,Login,Password) VALUES ('Marek','Dupa','m@s','dupa');
INSERT INTO `Student` (Name,Surname,Login,Password) VALUES ('Jadzia','Worek','j@s','dupa');
INSERT INTO `Student` (Name,Surname,Login,Password) VALUES ('Kili','walis','k@s','dupa');
>>>>>>> 4161abf7d15ddc1474963d6566d4467a6d016447
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
<<<<<<< HEAD
INSERT INTO `Mentor` (ID,Name,Surname,Email,Date_of_birth,City,Phone,Login,Password) VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
=======
INSERT INTO `Mentor` (Name,Surname,Login,Password) VALUES ('Marcin','Izworski','marcin@m','dupa');
INSERT INTO `Mentor` (Name,Surname,Login,Password) VALUES ('Przemysław','Ciąćka','przemek@m','dupa');
INSERT INTO `Mentor` (Name,Surname,Login,Password) VALUES ('Mentor','Mentorowski','mentor@m','dupa');
>>>>>>> 4161abf7d15ddc1474963d6566d4467a6d016447
CREATE TABLE `Manager` (
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
<<<<<<< HEAD
INSERT INTO `Manager` (ID,Name,Surname,Email,Date_of_birth,City,Phone,login,password) VALUES (1,'Tomasz','Kowalski',NULL,NULL,NULL,NULL,'tok','1234');
CREATE TABLE "Groups" (
=======
INSERT INTO `Manager` (Name,Surname,Login,Password) VALUES ('Jurek','Jurkowski','jurek@j','dupa');
CREATE TABLE `Groups` (
>>>>>>> 4161abf7d15ddc1474963d6566d4467a6d016447
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
	`Login`	TEXT UNIQUE,
	`Password`	TEXT
);
<<<<<<< HEAD
INSERT INTO `Employee` (ID,Name,Surname,Email,Date_of_birth,City,Phone,login,password) VALUES (1,'Jan','Kowalik',NULL,NULL,NULL,NULL,'jak',NULL);
=======
INSERT INTO `Employee` (Name,Surname,Login,Password) VALUES ('Miriam','Niewiem','miriam@e','dupa');
INSERT INTO `Employee` (Name,Surname,Login,Password) VALUES ('Kati','Niewiem','kati@e','dupa');
INSERT INTO `Employee` (Name,Surname,Login,Password) VALUES ('Sprzataczka','Sprzataczkowska','lol@e','dupa');
>>>>>>> 4161abf7d15ddc1474963d6566d4467a6d016447
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
<<<<<<< HEAD
	`Answer_text`	TEXT,
	`grade` INTEGER
=======
	`Answer_text`	TEXT
	`Grade` INTEGER
>>>>>>> 4161abf7d15ddc1474963d6566d4467a6d016447

);
INSERT INTO `Answers` (ID,Student_ID,Answer_text) VALUES (1,4,'Square has four sides');
INSERT INTO `Answers` (ID,Student_ID,Answer_text) VALUES (2,2,'Circle is round');
COMMIT;
