# Documento de visão
# O'Time
## 1. Introdução
### 1.1. Resumo

`O O'Time é uma aplicação web que permite a gestão e montagem de horários de forma eficiente e simples.`

### 1.3. Escopo

Principais responsabilidades e não responsabilidades do sistema.

### Responsabilidades

- Permitir que os usuários se cadastrem no sistema e tenham níveis de acesso diferentes de acordo com as preferências de um usuário principal.
- Garantir que não haja inconsistência nos dados.

### Não-responsabilidades

- Garantir acesso total no caso de perda de conexão com a internet.
- Permitir que os funcionários da escola conversem entre si.
- Segurança em caso de vazamento de senhas oriundo de descuido dos usuários.
- Criação automática de horários.

## 2. Requisitos

### 2.1. Requisitos Funcionais

| Cod | Nome | Descrição | Categoria |
| ------ | ------ | ------ | ------ |
| F01 | Cadastro de usuários | O sistema deve permitir que os usuários se cadastrem no mesmo. | Evidente |
| F02 | Login |  O sistema deve permitir que os usuários entrem no sistema usando suas credenciais. | Evidente |
| F03 | Recuperação de senha | O sistema deve permitir que os usuários recuperem suas senhas, se necessário. | Evidente |
| F04 | Definição nos slots de horários | O sistema deve permitir que gestores definam slots de horários para as turmas cadastradas. | Evidente |
| F05 | Alteração nos slots de horários | O sistema deve permitir que gestores alterem slots de horários já definidos, podendo excluí-los se necessário. | Evidente |
| F06 | Notificação de mudanças de horário | O sistema deve notificar aos usuários de mudanças nos horários. | Evidente |
| F07 | Cadastro de horários de disponibilidade | O sistema deve permitir o cadastro de horários de disponibilidade dos professores. | Evidente |
| F08 | Alteração horários de disponibilidade | O sistema deve permitir a alteração de horários de disponibilidade dos professores, podendo excluí-los se necessário. | Evidente |
| F09 | Visualização horários cadastrados | O sistema deve permitir aos gestores que visualizem os horários cadastrados por eles. | Evidente |
| F10 | Adicão de diretorias | O sistema deve permitir ao diretor Cadastrarr diretorias. | Evidente |
| F11 | Solicitação mudança de horários | O sistema deve permitir aos professores solicitarem aos gestores mudanças de horários. | Evidente |
| F12 | Alteração de diretorias | O sistema deve permitir que o diretor altere as diretorias cadatradas, podendo excluí-las se necessário. | Evidente |
| F13 | Lista de diretorias | O sistema deve permitir a listagem de diretorias cadastradas. | Evidente |
| F14 | Adição de gestores | O sistema deve permitir ao diretor Cadastrarr gestores. | Evidente |
| F15 | Alteração de gestores | O sistema deve permitir ao diretor alterar gestores cadastrados, podendo excluí-los se necessário. | Evidente |
| F16 | Lista de gestores | O sistema deve permitir a listagem de gestores cadastrados. | Evidente |
| F17 | Adição de salas | O sistema deve permitir ao diretor Cadastrarr salas. | Evidente |
| F18 | Alteração de salas | O sistema deve permitir ao diretor alterar as salas cadastradas, podendo excluí-las se necessário. | Evidente | Evidente |
| F19 | Lista de salas | O sistema deve permitir a listagem de salas cadastradas.| Evidente |
| F20 | Verificação de disponibilidade de salas | O sistema deve permitir a verificação a disponibilidade de salas. | Evidente |
| F21 | Adição disciplinas | O sistema deve permitir ao gestor Cadastrarr disciplinas.| Evidente |
| F22 | Alteração de disciplinas | O sistema deve permitir ao gestor alterar disciplinas cadastradas, podendo excluí-las se necessário. | Evidente |
| F23 | Lista de disciplinas | O sistema deve permitir ao gestor a listagem de disciplinas cadastradas. | Evidente |
| F24 | Adição curso | O sistema deve permitir ao gestor Cadastrarr cursos.| Evidente |
| F25 | Alteração de curso | O sistema deve permitir ao gestor alterar cursos cadastrados, podendo excluí-los se necessário. | Evidente |
| F26 | Lista de cursos | O sistema deve permitir a listagem de cursos cadastrados. | Evidente |
| F27 | Adição de turma | O sistema deve permitir ao gestor Cadastrarr turmas. | Evidente |
| F28 | Editar turma | O sistema deve permitir ao gestor alterar turmas cadastradas, podendo excluí-las se necessário. | Evidente |
| F29 | Lista de turmas | O sistema deve permitir a listagem de turmas cadastradas. | Evidente |
| F30 | Definição de slots de horário | O sistema deve permitir ao gestor definir os slots de horário de uma turma já cadastrada. | Evidente |
| F31 | Alteração nos slots de horário | O sistema deve permitir ao gestor alterar os slots de horário de uma turma já cadastrada, podendo excluí-los se necessário. | Evidente |
| F32 | Visualização dos slots de horário | O sistema deve permitir o professor visualizar slots de horário nos quais ele tem aula. | Evidente |
| F33 | Filtro para visualização de horários | O sistema deve permitir a filtragem da visualização dos slots de horários por sala, disciplina e turma. | Evidente |

### 2.2. Requisitos não funcionais

| Cód. | Nome | Descrição | Categoria | Obrigatoriedade | Permanência |
| ------ | ------ | ------ | ------ | ------ | ------ |
| NF01 | Interface Web | Deve funcionar em uma plataforma web | Interface | Obrigatório | Permanente |
| NF02 | Interface Mobile |  Deve funcionar em uma plataforma mobile | Interface | Desejável | Transitório |
| NF03 | Tecnologias de Desenvolvimento | Será desenvolvido usando o Django Framework na linguagem Python e HTML5 / JavaScript / CSS. | Implementação | Obrigatório | Transitório |
| NF04 | Restrição de horários | Permitir que apenas gestores modifiquem os horários | Implementação | Obrigatório | Transitório |
| NF05 | Exportação do arquivo de horários | O sistema deve permitir aos usuários exportar o arquivo de horários para outros formatos. | Especificação | Desejável | Transitório

### 2.3. Diagrama Geral de Casos de uso

![Diagrama Geral de Casos de Uso](doc/img/Diagrama-de-casos-de-uso.jpg)

### 2.4. Casos de Uso

| Cod. | Caso de Uso | Descrição | Classificação |
| ---- | ----------- | --------- | ------------- |
| UC01 | Listar salas | O gestor loga no sistema e seleciona a opção 'Salas' na página inicial. Abre-se então a Lista de salas. | Secundário |
| UC02 | Listar turmas | O gestor loga no sistema e seleciona a opção 'Turmas' na página inicial. Abre-se então a Lista de turmas. | Secundário |
| UC03 | Listar disciplinas | O gestor loga no sistema e seleciona a opção 'Listar Disciplinas'. Abre-se então a Lista de disciplinas. | Secundário |
| UC04 | Listar professores | O gestor loga no sistema e seleciona a opção 'Professores' na página inicial. Abre-se então a Lista de professores. | Secundário |
| UC05 | Cadastrar salas | O gestor loga no sistema e seleciona a opção 'Salas' na página inicial, e escolhe “Nova”. O sistema retorna um formulário modal de preenchimento de dados da sala. | Secundário |
| UC06 | Cadastrar turmas | O gestor loga no sistema e seleciona a opção 'Turmas' na página inicial e escolhe “Cadastrar turmas". O sistema retorna uma tela de preenchimento de dados do turmas.| Secundário |
| UC07 | Cadastrar disciplinas | O gestor loga no sistema e seleciona a opção 'Disciplinas' na página inicial e escolhe “Cadastrar Disciplina". O sistema retorna um formulário modal de preenchimento de dados da disciplina. | Secundário |
| UC08 | Cadastrar professores | O gestor loga no sistema e seleciona a opção 'Professores' na página inicial e escolhe “Cadastrar professor". O sistema retorna um formulário modal de preenchimento de dados do professor. | Secundário |
| UC09 | Definir horários | O gestor loga no sistema e seleciona a opção 'Definir horários'. O sistema então solicita que o gestor escolha a turma para qual deseja definir horários. O gestor seleciona a turma e o sistema retorna uma tabela no qual ele pode cadastrar os horários daquela turma. | Secundário |
| UC11 | Visualizar detalhes de uma sala | O gestor loga no sistema e seleciona a opção 'Salas' na página inicial, vai até a sala que deseja visualizar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da sala. | Secundário |
| UC12 | Visualizar detalhes de uma turma | O gestor loga no sistema e seleciona a opção 'Turmas' na página inicial, vai até a turma que deseja visualizar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da turma. | Secundário |
| UC13 | Visualizar detalhes de uma disciplina | O gestor loga no sistema e seleciona a opção 'Disciplinas' na página inicial, vai até a disciplina que deseja visualizar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da disciplina. | Secundário |
| UC14 | Visualizar detalhes de um professor | O gestor loga no sistema e seleciona a opção 'Professores' na página inicial, vai até o professor que deseja visualizar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da professor. | Secundário |
| UC15 | Verificar pré-requisitos | O gestor loga no sistema e seleciona a opção 'Definir horários'. O sistema então solicita que o gestor escolha a turma para qual deseja definir horários. O gestor seleciona a turma e o sistema então verifica se já estão cadastrados: um professor, uma disciplina, uma turma e uma sala, ao menos 1 de cada e caso cumpra os requisitos solicitados, redireciona o usuário para a tela de cadastro de horários. | Primário |
| UC16 | Editar  informações de uma sala | O gestor loga no sistema e seleciona a opção 'Salas' na página inicial, vai até a sala que deseja editar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da sala. O gestor clica em "Alterar" e então o sistema retorna um formulário modal de preenchimento de dados da sala. | Secundário |
| UC17 | Editar informações de uma turma | O gestor loga no sistema e seleciona a opção 'Turmas' na página inicial, vai até a turma que deseja editar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da turma. O gestor clica em "Alterar" e então o sistema retorna um formulário modal de preenchimento de dados da turma. | Secundário |
| UC18 | Editar informações de uma disciplina | O gestor loga no sistema e seleciona a opção 'Disciplinas' na página inicial, vai até a disciplina que deseja editar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da disciplina. O gestor clica em "Alterar" e então o sistema retorna um formulário modal de preenchimento de dados da disciplina. | Secundário |
| UC19 | Editar informações de um professor | O gestor loga no sistema e seleciona a opção 'Professores' na página inicial, vai até o professor que deseja editar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da professor. O gestor clica em "Alterar" e então o sistema retorna um formulário modal de preenchimento de dados da professor. | Secundário |
| UC20 | Filtrar por sala | O gestor loga no sistema e seleciona a opção 'Buscar'. O sistema retorna uma tela com filtros disponíveis e o gestor seleciona a opção 'Filtrar por Sala'. O sistema retorna uma página contendo as salas cadastradas. O gestor então seleciona uma sala específica para visualizar os horários cadastrados dela. | Secundário |
| UC21 | Filtrar por turma | O gestor loga no sistema e seleciona a opção 'Buscar'. O sistema retorna uma tela com filtros disponíveis e o gestor seleciona a opção 'Filtrar por Turma'. O sistema retorna uma página contendo as turmas cadastradas. O gestor então seleciona uma turma específica para visualizar os horários cadastrados dela. | Secundário |
| UC22 | Filtrar por disciplina | O gestor loga no sistema e seleciona a opção 'Buscar'. O sistema retorna uma tela com filtros disponíveis e o gestor seleciona a opção 'Filtrar por Disciplina'. O sistema retorna uma página contendo as disciplinas cadastradas. O gestor então seleciona uma disciplina específica para visualizar os horários cadastrados dela. | Secundário |
| UC23 | Filtrar por professor | O gestor loga no sistema e seleciona a opção 'Buscar'. O sistema retorna uma tela com filtros disponíveis e o gestor seleciona a opção 'Filtrar por Professor'. O sistema retorna uma página contendo os professores cadastrados. O gestor então seleciona um professor específico para visualizar os horários cadastrados dele. | Secundário |
| UC24 | Deletar sala | O gestor loga no sistema e seleciona a opção 'Salas' na página inicial, vai até a sala que deseja deletar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da sala.  O gestor clica em "Deletar" e então o sistema retorna um formulário modal com a mensagem: "Tem certeza que deseja remover (nome da sala)?" e aguarda pela confirmação. O gestor então seleciona a opção confirmar. O sistema redireciona o usuário para a página de salas, já não mais exibindo a excluída, indicando que foi apagada. | Secundário |
| UC25 | Deletar turma | O gestor loga no sistema e seleciona a opção 'Turmas' na página inicial, vai até a turma que deseja deletar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da turma. O gestor clica em "Deletar" e então o sistema retorna um formulário modal com a mensagem: "Tem certeza que deseja remover (nome da turma)?" e aguarda pela confirmação. O gestor então seleciona a opção confirmar. O sistema redireciona o usuário para a página de turmas, já não mais exibindo a excluída, indicando que foi apagada. | Secundário |
| UC26 | Deletar disciplina | O gestor loga no sistema e seleciona a opção 'Disciplinas' na página inicial, vai até a disciplina que deseja deletar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da disciplina.  O gestor clica em "Deletar" e então o sistema retorna um formulário modal com a mensagem: "Tem certeza que deseja remover (nome da disciplina)?" e aguarda pela confirmação. O gestor então seleciona a opção confirmar. O sistema redireciona o usuário para a página de disciplinas, já não mais exibindo a excluída, indicando que foi apagada. | Secundário |
| UC27 | Deletar professor | O gestor loga no sistema e seleciona a opção 'Professores' na página inicial, vai até o professor que deseja deletar e clica em "Detalhes". O sistema retorna uma tela contendo as informações da professor. O gestor clica em "Deletar" e então o sistema retorna um formulário modal com a mensagem: "Tem certeza que deseja remover (nome do professor)?" e aguarda pela confirmação. O gestor então seleciona a opção confirmar. O sistema redireciona o usuário para a página de professores, já não mais exibindo o excluído, indicando que foi apagado. | Secundário |

### 2.5. Casos de Uso por Módulo do Sistema

- Sala de Aula: *Listar salas, Cadastrar salas, Editar informações de uma sala e Deletar sala.*
- Disciplina: *Listar disciplinas, Cadastrar disciplinas, Editar informações de uma disciplina e Deletar disciplinas.*
- Turma: *Listar turmas, Cadastrar turma, Editar informações de uma turma e Deletar turma.*
- Professor: *Listar professor, Cadastrar professor, Editar informações de um professor e Deletar professor.*

### 2.6. Atores

| Ator | Descrição |
| ---- | --------- |
| Diretor | Responsável por cadastrar gestor e diretorias, se necessário. |
| Gestor | Responsável pela criação de tabelas de horários e mudanças nas mesmas, se necessário. | 
| Professor | Podem visualizar as tabelas de horários, solicitar mudanças aos gestores e selecionar horários de sua preferência. |

## 2.7. Clientes

```sh
O público-alvo do nosso sistema é formado principalmente por pessoas de instituições públicas,
que desejam adquirir um sistema que possibilite a gestão de horários de forma eficiente e simples.
```