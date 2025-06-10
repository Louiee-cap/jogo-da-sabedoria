CREATE DATABASE jogo_educacional;
USE jogo_educacional;


CREATE TABLE Série (
    idSérie INT PRIMARY KEY,
    nome_série VARCHAR(45)
);

CREATE TABLE Aluno (
    id_jogador INT PRIMARY KEY,
    nome_jogador VARCHAR(75),
    email_jogador VARCHAR(45),
    senha_jogador VARCHAR(15),
    Série_idSérie INT,
    FOREIGN KEY (Série_idSérie) REFERENCES Série(idSérie)
);

CREATE TABLE Professor (
    id_professor INT PRIMARY KEY,
    nome_professor VARCHAR(75),
    email_professor VARCHAR(45),
    senha_professor VARCHAR(15)
);

CREATE TABLE Matérias (
    id_matérias INT PRIMARY KEY,
    nome_materia VARCHAR(50)
);

CREATE TABLE Perguntas (
    id_perguntas INT PRIMARY KEY,
    txt_perguntas VARCHAR(255),
    nivel_perguntas VARCHAR(45),
    Matérias_id_matérias INT,
    FOREIGN KEY (Matérias_id_matérias) REFERENCES Matérias(id_matérias)
);

CREATE TABLE Respostas (
    id_respostas INT PRIMARY KEY,
    txt_respostas VARCHAR(255),
    Perguntas_id_perguntas INT,
    FOREIGN KEY (Perguntas_id_perguntas) REFERENCES Perguntas(id_perguntas)
);

CREATE TABLE Respostas_aluno (
    idRespostas_aluno INT PRIMARY KEY,
    Aluno_id_jogador INT,
    Perguntas_id_perguntas INT,
    Respostas_id_respostas INT,
    FOREIGN KEY (Aluno_id_jogador) REFERENCES Aluno(id_jogador),
    FOREIGN KEY (Perguntas_id_perguntas) REFERENCES Perguntas(id_perguntas),
    FOREIGN KEY (Respostas_id_respostas) REFERENCES Respostas(id_respostas)
);

CREATE TABLE Ranking (
    id_ranking INT PRIMARY KEY,
    pontuacao INT,
    posicao INT,
    Aluno_id_jogador INT,
    FOREIGN KEY (Aluno_id_jogador) REFERENCES Aluno(id_jogador)
);

CREATE TABLE Aluno_has_Matérias (
    Aluno_id_jogador INT,
    Matérias_idMatérias INT,
    PRIMARY KEY (Aluno_id_jogador, Matérias_idMatérias),
    FOREIGN KEY (Aluno_id_jogador) REFERENCES Aluno(id_jogador),
    FOREIGN KEY (Matérias_idMatérias) REFERENCES Matérias(id_matérias)
);

