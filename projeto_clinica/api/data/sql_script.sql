-- Database: CLINICA_DB

-- DROP DATABASE IF EXISTS "CLINICA_DB";

CREATE DATABASE "CLINICA_DB"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

--------------------------------- Tables creation  ---------------------------------

CREATE TABLE Persons (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    email VARCHAR(40) NOT NULL,
    cep CHAR(8) NOT NULL,
    state CHAR(2) NOT NULL,
    city VARCHAR(45) NOT NULL,
    neighborhood VARCHAR(20) NOT NULL,
    street VARCHAR(45) NOT NULL
);

CREATE TABLE Phones (
    id SERIAL PRIMARY KEY,
    persons_id INT NOT NULL,
    phone VARCHAR(11) NOT NULL,
    FOREIGN KEY (persons_id) REFERENCES Persons(id)
);

CREATE TABLE Users (
    persons_id INT PRIMARY KEY,
    username VARCHAR(40) NOT NULL,
    password CHAR(8) NOT NULL,
    FOREIGN KEY (persons_id) REFERENCES Persons(id)
);

CREATE TABLE Clients (
    persons_id INT PRIMARY KEY,
    FOREIGN KEY (persons_id) REFERENCES Persons(id)
);

CREATE TABLE Allergies_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL
);

CREATE TABLE Allergies (
    id SERIAL PRIMARY KEY,
    allergies_types_id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    nivel INT NOT NULL,
    FOREIGN KEY (allergies_types_id) REFERENCES Allergies_types(id)
);

CREATE TABLE Allergies_Clients (
    persons_id INT NOT NULL,
    allergies_id INT NOT NULL,
    PRIMARY KEY(persons_id, allergies_id),
    FOREIGN KEY (allergies_id) REFERENCES Allergies(id),
    FOREIGN KEY (persons_id) REFERENCES Clients(persons_id)
);

CREATE TABLE Props (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL
);

CREATE TABLE Clients_Props (
    persons_id INT NOT NULL,
    props_id INT NOT NULL,
    dose INT NOT NULL,
    PRIMARY KEY(persons_id, props_id),
    FOREIGN KEY (persons_id) REFERENCES Clients(persons_id),
    FOREIGN KEY (props_id) REFERENCES Props(id)
);

CREATE TABLE Diseases_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25)
);

CREATE TABLE Diseases (
    id SERIAL PRIMARY KEY,
    diseases_types_id INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    FOREIGN KEY (diseases_types_id) REFERENCES diseases_types(id)
);

CREATE TABLE Diseases_Clients (
    diseases_id INT NOT NULL,
    persons_id INT NOT NULL,
    PRIMARY KEY(diseases_id, persons_id),
    FOREIGN KEY (diseases_id) REFERENCES diseases(id),
    FOREIGN KEY (persons_id) REFERENCES Clients(persons_id)
);

CREATE TABLE Medicines_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE Medicines (
    id SERIAL PRIMARY KEY,
    medicines_types_id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    FOREIGN KEY (medicines_types_id) REFERENCES Medicines_types(id)
);

CREATE TABLE Medicines_Clients (
    persons_id INT NOT NULL,
    medicines_id INT NOT NULL,
    PRIMARY KEY(persons_id, medicines_id),
    FOREIGN KEY (medicines_id) REFERENCES Medicines(id),
    FOREIGN KEY (persons_id) REFERENCES Clients(persons_id)
);

CREATE TABLE Appointments (
    id SERIAL PRIMARY KEY,
    persons_id INT NOT NULL,
    schedule TIMESTAMP NOT NULL,
    note VARCHAR(255) NOT NULL,
    FOREIGN KEY (persons_id) REFERENCES Clients(persons_id)
);

--------------------------------- Initial load ---------------------------------

INSERT INTO Persons (first_name, last_name, email, cep, state, city, neighborhood, street)
VALUES ('Marco', 'Almeida', 'marco.almeida@sou.unaerp.edu.br', '14025060', 'SP', 'Ribeirão Preto', 'Sumaré', 'Rua Júlio Prestes 870');

INSERT INTO Users (persons_id, username, password)
VALUES (1, 'marco.almeida@sou.unaerp.edu.br', 'senha123');


--------------------------------- Tables drops  ---------------------------------

-- DROP TABLE IF EXISTS Appointments;
-- DROP TABLE IF EXISTS Medicines_Clients;
-- DROP TABLE IF EXISTS Diseases_Clients;
-- DROP TABLE IF EXISTS Clients_Props;
-- DROP TABLE IF EXISTS Allergies_Clients;
-- DROP TABLE IF EXISTS Users;
-- DROP TABLE IF EXISTS Medicines;
-- DROP TABLE IF EXISTS Diseases;
-- DROP TABLE IF EXISTS Props;
-- DROP TABLE IF EXISTS Allergies;
-- DROP TABLE IF EXISTS Phones;
-- DROP TABLE IF EXISTS Clients;
-- DROP TABLE IF EXISTS Persons;
-- DROP TABLE IF EXISTS Allergies_types;
-- DROP TABLE IF EXISTS Diseases_types;
-- DROP TABLE IF EXISTS Medicines_types;
