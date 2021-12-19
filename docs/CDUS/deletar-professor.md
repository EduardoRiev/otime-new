### Caso de Uso: Deletar professor
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja deletar um professor.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
-  O sistema retorna para a página de professores já sem o professor deletado.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "professores" do menu e em seguida vai até o professor desejado seleciona o botão **Detalhes**. 
2. O sistema redireciona o usuário para a página de detalhes da professor, exibindo as informações da mesmo.
3. O gestor seleciona a opção **deletar**.
4. O sistema abre um formulário modal com a mensagem: "Tem certeza que deseja remover (nome do professor)?" e aguarda pela confirmação.
5. O gestor então seleciona a opção **confirmar**.
6. O sistema redireciona o usuário para a página de professores, já não mais exibindo o professor excluído, indicando que foi apagado.
7. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**5a. A conexão com a internet cai**

6. O sistema exibe um alerta informando que não há conexão com a internet.
7. O gestor volta ao passo 2 do fluxo principal.