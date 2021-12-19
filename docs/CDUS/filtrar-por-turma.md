### Caso de Uso: Filtrar por turma
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja visualizar os horários cadastrados em uma turma específica.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.
- Ter pelo menos 1 horário cadastrado.

**Pós-condições**
- O sistema retorna uma página contendo os horários cadastrados numa turma especifíca.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor loga no sistema e seleciona a opção 'Buscar'. 
2. O sistema retorna uma tela com filtros disponíveis.
3. O gestor seleciona a opção 'Filtrar por Turma'. 
4. O sistema retorna uma página contendo as turmas cadastradas.
5. O gestor então seleciona uma turma específica para visualizar os horários cadastrados dela.
6. O sistema retorna uma página contendo os horários cadastrados naquela turma.
7. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**5a. A conexão com a internet cai**

6. O sistema exibe um alerta informando que não há conexão com a internet.
7. O gestor volta ao passo 1 do fluxo principal.
