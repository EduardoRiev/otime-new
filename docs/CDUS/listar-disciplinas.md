### Caso de Uso: Listar disciplinas
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja visualizar as disciplinas cadastradas no sistema.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
- As disciplinas cadastradas são exibidas numa lista.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "Disciplinas" na página inicial.
2. O sistema redireciona o usuário para uma página contendo uma lista de disciplinas cadastradas.
3. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. Não existem disciplinas cadastradas**

3. O sistema retorna uma mensagem de erro, informando "Não há disciplinas a serem listadas, tente cadastrar uma!".
4. CDU finalizado.

**3b. A conexão com a internet cai**

3. O sistema exibe um alerta informando que não há conexão com a internet.
4. O gestor volta ao passo 2 do fluxo principal.