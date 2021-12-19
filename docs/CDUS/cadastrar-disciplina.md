### Caso de Uso: Cadastrar disciplina
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja cadastrar disciplinas.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
- Uma disciplina é cadastrado no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "Disciplinas" do menu e em seguida seleciona o botão **Novo**. 
2. O sistema abre um formulário modal para cadastro de uma disciplina, contendo os campos para **nome**, **código** e **carga horária**.
3. O gestor então preenche todos os campos e clica no botão **Salvar**.
4. O sistema redireciona o usuário para a página de disciplinas, mostrando que o cadastro foi feito com sucesso.
5. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. A conexão com a internet cai**

3. O sistema exibe um alerta informando que não há conexão com a internet.
4. O gestor volta ao passo 2 do fluxo principal.

**3b. O gestor não preenche algum dos campos**

4. O sistema exibe uma mensagem na tela solicitando que o usuário preencha os campos requeridos.
5. O gestor volta ao passo 3 do fluxo principal.