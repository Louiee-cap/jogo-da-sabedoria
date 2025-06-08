+-----------------------------------------------------------+
|                           JOGO DA SABEDORIA                            |
+------------------------------------------------------+

Um sistema de quiz educacional desenvolvido em Python, utilizando a 
biblioteca Tkinter para a interface gráfica.

SOBRE O PROJETO
---------------------------

Este projeto consiste em um jogo de perguntas e respostas com funcionalidades 
distintas para alunos e administradores. A aplicação permite que os usuários 
joguem em diferentes categorias de matérias, enquanto os administradores 
podem gerenciar o banco de questões e visualizar o ranking de pontuações.

A interface foi desenvolvida com Tkinter, e o sistema utiliza um banco de dados local 
(SQLite) ou um servidor (MySQL) para persistência de dados.


TECNOLOGIAS UTILIZADAS
---------------------------
O projeto foi construído com as seguintes tecnologias principais:

* Python 3: Linguagem base da aplicação.
* Tkinter: Biblioteca padrão do Python para a criação da interface gráfica (GUI).
* SQLite: Utilizado para o banco de dados local de perguntas e ranking.
* MySQL: Integração para um banco de dados mais robusto, com o uso da 
  biblioteca mysql-connector-python.


  
Funcionalidades para Alunos
---------------------------
* Autenticação de Usuário: Sistema de login para jogadores.
* Seleção de Desafio: Permite ao aluno escolher a matéria e a série antes de iniciar.
* Mecânica de Jogo: Resolução de perguntas de múltipla escolha com pontuação.
* Sistema de Dicas: Disponibiliza uma opção para eliminar duas alternativas incorretas.

Funcionalidades para Administradores
------------------------------------
* Painel de Controle: Acesso a uma tela de gerenciamento restrita.
* Gerenciamento de Conteúdo: Funcionalidade para adicionar novas perguntas ao banco de dados.
* Visualização de Ranking: Permite ao administrador visualizar a classificação dos jogadores com base na pontuação.

PRÉ-REQUISITOS
--------------
* Python 3.x

COMO UTILIZAR
---------------------------

A aplicação possui fluxos de login separados para alunos e administradores.

* Acesso de Aluno: 
  Selecione a opção de login para aluno e insira um nome de usuário e 
  senha para registrar e jogar.

* Acesso de Administrador: 
  Selecione a opção de login para administrador e insira um nome de usuário e 
  senha para registrar e modificar questões ou visualizar o ranking.
* DEBUG(Remover depois)
  - Usuário: admin
  - Senha:   1234 ou admin

AUTORES
---------------------------

* Coloquem seus nomes completos aqui
