### Caso de Uso: Deletar disciplina
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja deletar uma disciplina.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
-  O sistema retorna para a página de disciplinas já sem a disciplina deletada.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "disciplinas" do menu e em seguida vai até a disciplina desejada seleciona o botão **Detalhes**. 
2. O sistema redireciona o usuário para a página de detalhes da disciplina, exibindo as informações da mesma.
3. O gestor seleciona a opção **deletar**.
4. O sistema abre um formulário modal com a mensagem: "Tem certeza que deseja remover (nome da disciplina)?" e aguarda pela confirmação.
5. O gestor então seleciona a opção **confirmar**.
6. O sistema redireciona o usuário para a página de disciplinas, já não mais exibindo a excluída, indicando que foi apagada.
7. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**5a. A conexão com a internet cai**

6. O sistema exibe um alerta informando que não há conexão com a internet.
7. O gestor volta ao passo 2 do fluxo principal.