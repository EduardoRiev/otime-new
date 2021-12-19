### Caso de Uso: Filtrar por professor
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja visualizar os horários cadastrados para um professor específico.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.
- Ter pelo menos 1 horário cadastrado.

**Pós-condições**
- O sistema retorna uma página contendo os horários cadastrados de um professor específico.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor loga no sistema e seleciona a opção 'Buscar'. 
2. O sistema retorna uma tela com filtros disponíveis.
3. O gestor seleciona a opção 'Filtrar por Professor'. 
4. O sistema retorna uma página contendo os professores cadastrados.
5. O gestor então seleciona um professor específico para visualizar os horários cadastrados dele.
6. O sistema retorna uma página contendo os horários cadastrados para aquele professor.
7. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**5a. A conexão com a internet cai**

6. O sistema exibe um alerta informando que não há conexão com a internet.
7. O gestor volta ao passo 1 do fluxo principal.
