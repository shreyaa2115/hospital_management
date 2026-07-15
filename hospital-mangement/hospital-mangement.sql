CREATE DATABASE HospitalManagement;
USE HospitalManagement;
CREATE TABLE Doctors (
    IDNumber INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Department VARCHAR(50),
    LoginTime DATETIME
);

CREATE TABLE Nurses (
    NurseID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    IDNumber VARCHAR(50) UNIQUE NOT NULL,
    Age INT NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Department VARCHAR(100) NOT NULL,
    LoginTime TIME NOT NULL
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    IDNumber VARCHAR(50) UNIQUE NOT NULL,
    Age INT NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Department VARCHAR(100) NOT NULL,
    LoginTime TIME NOT NULL
);

