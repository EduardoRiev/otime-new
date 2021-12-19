### Caso de Uso: Listar Turmas
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja visualizar as turmas cadastradas no sistema.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
- As turmas cadastradas são exibidas numa lista.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "turmas" na página inicial.
2. O sistema redireciona o usuário para uma página contendo uma lista de turmas cadastradas.
3. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. Não existem turmas cadastradas**

3. O sistema retorna uma mensagem de erro, informando "Não há turmas a serem listadas, tente cadastrar uma!".
4. CDU finalizado.

**3b. A conexão com a internet cai**

3. O sistema exibe um alerta informando que não há conexão com a internet.
4. O gestor volta ao passo 2 do fluxo principal.