### Caso de Uso: Verificar pré-requisitos
---
**Ator principal:** 
- Sistema

**Interessados e Interesses:**
- Sistema: verificar se os requisitos para o cadastro de um horário.
- Gestor: deseja saber se os requisitos para cadastrar um horário já foram antendidos.

**Pré-Condições:**
- O gestor deve ter cadastro completo, estar logado no sistema.

**Pós-condições**
-  O sistema informa se os requisitos foram atendidos ou não.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. Segue os passos de 1 e 2 do Caso de Uso Definir Horários.
2. O sistema então verifica se já estão cadastrados: um professor, uma disciplina, uma turma e uma sala,<br> ao menos 1 de cada e caso cumpra os requisitos solicitados, redireciona o usuário para a tela de cadastro de horários.
3. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**2a. A conexão com a internet cai**

3. O sistema exibe um alerta informando que não há conexão com a internet.
4. O sistema redireciona o usuário para a página inicial.
5.  CDU finalizado.

**2b. Os requisitos não foram cumpridos**

3. O sistema exibe a mensagem "O sistema não conta com os requisitos para que um horário seja reservado. <br>Adicione uma sala de aula, uma disciplina e um professor antes." e então redireciona o usuário para a página inicial.
4. CDU finalizado.