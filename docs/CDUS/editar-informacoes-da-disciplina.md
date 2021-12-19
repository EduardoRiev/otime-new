### Caso de Uso: Editar informações de uma disciplina
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja editar as informações de uma disciplina.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
-  O sistema exibe os detalhes da disciplina já contendo as alterações feitas.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "disciplinas" do menu e em seguida vai até a disciplina desejada seleciona o botão **Detalhes**. 
2. O sistema redireciona o usuário para a página de detalhes da disciplina, exibindo as informações da mesma.
3. O gestor seleciona a opção **alterar**.
4. O sistema abre um formulário modal contendo as informações já cadastradas anteriormente.
5. O gestor então realiza as alterações desejadas e clica no botão **salvar**.
6. O sistema redireciona o usuário para a página de detalhes da disciplina, exibindo as informações modificadas, mostrando que foram salvas.
7. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**5a. A conexão com a internet cai**

6. O sistema exibe um alerta informando que não há conexão com a internet.
7. O gestor volta ao passo 2 do fluxo principal.