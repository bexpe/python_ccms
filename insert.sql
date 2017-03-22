-- PRAGMA writable_schema = 1;
-- delete from sqlite_master where type in ('table', 'index', 'trigger');
-- PRAGMA writable_schema = 0;
-- PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS Answers;
DROP TABLE IF EXISTS Attendance;
DROP TABLE If EXISTS Assignments;
DROP TABLE If EXISTS Employee;
DROP TABLE If EXISTS Manager;
DROP TABLE If EXISTS Mentor;
DROP TABLE If EXISTS Student;
DROP TABLE If EXISTS Teams;

CREATE TABLE "Mentor" (
	`User_ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` TEXT,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT
);
INSERT INTO "Mentor" VALUES(1,'Marcin','Izworski',NULL,NULL,NULL,NULL,'marcin@m','dupa');
INSERT INTO "Mentor" VALUES(2,'Przemysław','Ciąćka',NULL,NULL,NULL,NULL,'przemek@m','dupa');
INSERT INTO "Mentor" VALUES(3,'Mentor','Mentorowski',NULL,NULL,NULL,NULL,'mentor@m','dupa');
CREATE TABLE `Manager` (
	`User_ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` TEXT,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT
);
INSERT INTO "Manager" VALUES(1,'Jurek','Jurkowski',NULL,NULL,NULL,NULL,'jurek@j','dupa');
CREATE TABLE `Employee` (
	`User_ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email` TEXT,
	`Date_of_birth` TEXT,
	`City` TEXT,
	`Phone` TEXT,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT
);
INSERT INTO "Employee" VALUES(1,'Miriam','Niewiem',NULL,NULL,NULL,NULL,'miriam@e','dupa');
INSERT INTO "Employee" VALUES(2,'Kati','Niewiem',NULL,NULL,NULL,NULL,'kati@e','dupa');
INSERT INTO "Employee" VALUES(3,'Sprzataczka','Sprzataczkowska',NULL,NULL,NULL,NULL,'lol@e','dupa');
CREATE TABLE `Attendance` (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Student_ID`	INTEGER,
	 Date	INTEGER,
	`Attendance_value` TEXT
);
CREATE TABLE `Assignments` (	
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Task_type`	TEXT,
);
INSERT INTO "Assignments" VALUES(1,'Square','Find the area of a square with a given side',1);
CREATE TABLE "Teams" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT
);
INSERT INTO "Teams" VALUES(1,NULL);
CREATE TABLE "Student" (
	`User_ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Surname`	TEXT,
	`Email`	TEXT,
	`Date_of_birth`	TEXT,
	`City`	TEXT,
	`Phone`	TEXT,
	`Login`	TEXT UNIQUE,
	`Password`	TEXT,
	`Team_ID`	INTEGER,
	`Card`	TEXT
);
INSERT INTO "Student" VALUES(1,'Marek','Dupa',NULL,NULL,NULL,NULL,'m@s','dupa',NULL,NULL);
INSERT INTO "Student" VALUES(2,'Jadzia','Worek',NULL,NULL,NULL,NULL,'j@s','dupa',NULL,NULL);
INSERT INTO "Student" VALUES(3,'Kili','walis',NULL,NULL,NULL,NULL,'k@s','dupa',NULL,NULL);
INSERT INTO "Student" VALUES(4,'typ 1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
CREATE TABLE "Answers" (
	`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Answer_text`	TEXT,
	`Grade`	TEXT,
	`Student_ID`	INTEGER,
	`Team_ID`	INTEGER,
	`Assignment_ID`	INTEGER,
	`Grade_date`	TEXT
);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('Mentor',3);
INSERT INTO "sqlite_sequence" VALUES('Manager',1);
INSERT INTO "sqlite_sequence" VALUES('Employee',3);
INSERT INTO "sqlite_sequence" VALUES('Assignments',1);
INSERT INTO "sqlite_sequence" VALUES('Teams',1);
INSERT INTO "sqlite_sequence" VALUES('Student',4);
INSERT INTO "sqlite_sequence" VALUES('Answers',2);
COMMIT;
