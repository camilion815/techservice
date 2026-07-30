DROP DATABASE IF EXISTS techservice_db;

CREATE DATABASE techservice_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE techservice_db;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    codigo_postal VARCHAR(10),
    status TINYINT NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL
);

CREATE TABLE equipamento (
    id_equipamento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descricao TEXT,
    status TINYINT NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL
);


CREATE TABLE ordem_de_servico (
    id_ordem INT AUTO_INCREMENT PRIMARY KEY,
    id_equipamento INT NOT NULL,
    diagnostico TEXT NOT NULL,
    solucao TEXT,
    status TINYINT NOT NULL DEFAULT 1,
    prioridade TINYINT NOT NULL DEFAULT 1,
    custo_total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL,
    FOREIGN KEY (id_equipamento) REFERENCES equipamento(id_equipamento)
);

--cliente e equipamento de exemplo
INSERT INTO clientes (
    nome,
    email,
    telefone,
    codigo_postal
)
VALUES (
    'Mário Fortunato',
    'mario.fortunato@email.com',
    '912345678',
    '1000-001'
);


INSERT INTO equipamento (
    nome,
    tipo,
    descricao
)
VALUES (
    'Dell Inspiron 15',
    'Laptop',
    'Portátil simples.'
);

