USE [master]
GO

/****** Object:  Database [CLINICA_DB]    Script Date: 26/11/2023 21:21:04 ******/
CREATE DATABASE [CLINICA_DB]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'CLINICA_DB', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\CLINICA_DB.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'CLINICA_DB_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\CLINICA_DB_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [CLINICA_DB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [CLINICA_DB] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [CLINICA_DB] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [CLINICA_DB] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [CLINICA_DB] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [CLINICA_DB] SET ARITHABORT OFF 
GO

ALTER DATABASE [CLINICA_DB] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [CLINICA_DB] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [CLINICA_DB] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [CLINICA_DB] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [CLINICA_DB] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [CLINICA_DB] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [CLINICA_DB] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [CLINICA_DB] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [CLINICA_DB] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [CLINICA_DB] SET  DISABLE_BROKER 
GO

ALTER DATABASE [CLINICA_DB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [CLINICA_DB] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [CLINICA_DB] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [CLINICA_DB] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [CLINICA_DB] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [CLINICA_DB] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [CLINICA_DB] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [CLINICA_DB] SET RECOVERY FULL 
GO

ALTER DATABASE [CLINICA_DB] SET  MULTI_USER 
GO

ALTER DATABASE [CLINICA_DB] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [CLINICA_DB] SET DB_CHAINING OFF 
GO

ALTER DATABASE [CLINICA_DB] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [CLINICA_DB] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [CLINICA_DB] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [CLINICA_DB] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO

ALTER DATABASE [CLINICA_DB] SET QUERY_STORE = OFF
GO

ALTER DATABASE [CLINICA_DB] SET  READ_WRITE 
GO

--------------------------------- Tables creation  ---------------------------------

CREATE TABLE Persons (
    id INTEGER IDENTITY(1,1) NOT NULL PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    email VARCHAR(40) NOT NULL,
    cep CHAR(8) NOT NULL,
    state CHAR(2) NOT NULL,
    city VARCHAR(45) NOT NULL,
    neighborhood VARCHAR(20) NOT NULL,
    street VARCHAR(45) NOT NULL,
);

CREATE TABLE Phones (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    persons_id INT NOT NULL,
    phone VARCHAR(11) NOT NULL,
    FOREIGN KEY (persons_id) REFERENCES Persons(id)
);

CREATE TABLE Users (
    id INT IDENTITY(1,1) NOT NULL,
    persons_id INT NOT NULL,
	username VARCHAR(40) NOT NULL,
    password CHAR(8) NOT NULL,
    PRIMARY KEY(id, Persons_id),
    FOREIGN KEY (persons_id) REFERENCES Persons(id)
);

CREATE TABLE Clients (
    id INT IDENTITY(1,1) NOT NULL,
    persons_id INT NOT NULL,
    PRIMARY KEY(id, Persons_id),
    FOREIGN KEY (persons_id) REFERENCES Persons(id)
);

CREATE TABLE Allergies_types (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    name VARCHAR(25) NOT NULL
);

CREATE TABLE Allergies (
    id INT IDENTITY(1,1) NOT NULL,
    allergies_types_id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    nivel INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (allergies_types_id) REFERENCES Allergies_types(id)
);

CREATE TABLE Allergies_Clients (
    clients_id INT NOT NULL,
    clients_persons_id INT NOT NULL,
    allergies_id INT NOT NULL,
    PRIMARY KEY(clients_id, clients_persons_id, allergies_id),
    FOREIGN KEY (allergies_id) REFERENCES Allergies(id),
    FOREIGN KEY (clients_id, clients_Persons_id) REFERENCES Clients(id, persons_id)
);

CREATE TABLE Props (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    name VARCHAR(40) NOT NULL
);

CREATE TABLE Clients_Props (
    clients_id INT NOT NULL,
    clients_Persons_id INT NOT NULL,
    props_id INT NOT NULL,
    dose INT NOT NULL,
    PRIMARY KEY(clients_id, clients_persons_id, props_id),
    FOREIGN KEY (clients_id, clients_persons_id) REFERENCES Clients(id, persons_id),
    FOREIGN KEY (props_id) REFERENCES Props(id)
);

CREATE TABLE Diseases_types (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    name VARCHAR(25) NULL
);

CREATE TABLE Diseases (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    diseases_types_id INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    FOREIGN KEY (diseases_types_id) REFERENCES diseases_types(id)
);

CREATE TABLE Diseases_Clients (
    diseases_id INT NOT NULL,
    clients_id INT NOT NULL,
    clients_persons_id INT NOT NULL,
    PRIMARY KEY(diseases_id, clients_id, clients_persons_id),
    FOREIGN KEY (diseases_id) REFERENCES diseases(id),
    FOREIGN KEY (clients_id, clients_persons_id) REFERENCES Clients(id, persons_id)
);

CREATE TABLE Medicines_types (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    name VARCHAR(20) NULL
);

CREATE TABLE Medicines (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    medicines_types_id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    FOREIGN KEY (medicines_types_id) REFERENCES Medicines_types(id)
);

CREATE TABLE Medicines_Clients (
    clients_id INT NOT NULL,
    clients_Persons_id INT NOT NULL,
    medicines_id INT NOT NULL,
    PRIMARY KEY(clients_id, clients_persons_id, medicines_id),
    FOREIGN KEY (medicines_id) REFERENCES Medicines(id),
    FOREIGN KEY (clients_id, clients_Persons_id) REFERENCES Clients(id, persons_id)
);

--------------------------------- Initial load  ---------------------------------

INSERT INTO Persons (first_name, last_name, email, cep, state, city, neighborhood, street)
VALUES ('Marco', 'Almeida', 'marco.almeida@sou.unaerp.edu.br', '14025060', 'SP', 'Ribeirão Preto', 'Sumaré', 'Rua Júlio Prestes 870');

INSERT INTO Users (persons_id, username, password)
VALUES (1, 'marco.almeida@sou.unaerp.edu.br', 'senha123');

--------------------------------- Tables drops  ---------------------------------

-- DROP TABLE Allergies_Clients;

-- DROP TABLE Clients_Props;

-- DROP TABLE Diseases_Clients;

-- DROP TABLE Medicines_Clients;

-- DROP TABLE Users;

-- DROP TABLE Allergies;

-- DROP TABLE Diseases;

-- DROP TABLE Medicines;

-- DROP TABLE Phones;

-- DROP TABLE Props;

-- DROP TABLE Clients;

-- DROP TABLE Persons;

-- DROP TABLE Medicines_types;

-- DROP TABLE Diseases_types;

-- DROP TABLE Allergies_types;
