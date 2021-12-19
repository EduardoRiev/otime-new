### Caso de Uso: Definir horário(s)
---
**Ator principal:** Gestor.

**Interessados e Interesses:**
- Gestor: deseja definir horário(s) para uma turma.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.
- Haver, no minimo, um professor, uma disciplina e uma sala de aula cadastrada no sistema.
 
**Pós-condições**
- Horário(s) foi(foram) definido(s) no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "Definir Horários" na página inicial.
2. O sistema solicita ao usuário que selecione uma turma para o qual deseja definir horários.
3. O sistema abre o formulário para definição dos horários desejados, contendo listas de **professores**, de **salas de aula** e de **disciplinas**.
4. O gestor seleciona um de cada opção.
5. O gestor vai até os slots na tabela, seleciona os horários que estão disponíveis para definir o slot e por fim, clica na opção "Cadastrar".
6. O gestor clica no(s) horário(s) que deseja definir.
9. O sistema cadastra a definição e CDU finaliza.

**Fluxos alternativos ou excepcionais**

**2a. Os pré-requisistos não foram atendidos**

3. O sistema exibe uma mensagem informando que "O sistema não conta com os requisitos para que um horário seja reservado. Adicione uma sala de aula, uma disciplina e um professor antes." e redireciona o usuário para a página inicial.
4. CDU finalizado.

**5a. O gestor esquece de selecionar um dos campos ao tentar cadastrar um horário**

6. O sistema solicita, sem cadastrar, que o usuário selecione uma opção no campo restante.
7. O gestor seleciona a opção desejada e o sistema então define os horários.
8. CDU finalizado.