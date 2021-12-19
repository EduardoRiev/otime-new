### Caso de Uso: Listar Professores
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja visualizar os professores cadastrados no sistema.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
- Os professores cadastrados são exibidos numa lista.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "professores" na página inicial.
2. O sistema redireciona o usuário para uma página contendo uma lista de professores cadastrados.
3. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. Não existem professores cadastrados**

3. O sistema retorna uma mensagem de erro, informando "Não há professores a serem listados, tente cadastrar um!".
4. CDU finalizado.

**3b. A conexão com a internet cai**

3. O sistema exibe um alerta informando que não há conexão com a internet.
4. O gestor volta ao passo 2 do fluxo principal.