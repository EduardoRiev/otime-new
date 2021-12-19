# O&#39;Time
## Plano de Desenvolvimento de Software
### Histórico da Revisão
| Data | Versão | Descrição | Autor |
| ---- | ------ | --------- | ----- |
| 16/03/2020 | 1.0 | Elaboração da 1ª do Plano de Desenvolvimento de Software baseada no modelo descrito no PAAD | Eduardo Riev |

# 1. Introdução

## 1.1. Objetivo

O objetivo principal deste Plano de Desenvolvimento de Software é definir quais as atividades de desenvolvimento em termos de fases e iterações são requeridas para implementar um serviço de gerenciamento de horários para o Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte (IFRN), envolvendo os alunos do curso de Tecnologia em Análise e Desenvolvimento de Sistemas (TADS) da disciplina de Seminário de Orientação ao Desenvolvimento de Sistemas Distribuídos.

## 1.2. Escopo

Este Plano de Desenvolvimento de Software descreve o planejamento que venha a ser usado no desenvolvimento do sistema proposto, bem como o reconhecimento, a validação e possíveis soluções do problema que o O&#39;Time deseja resolver, as atribuições funcionais de cada componente do grupo e suas devidas responsabilidades. Os detalhes do gerenciamento das iterações serão individualmente descritos nos Planos de Iteração.

##  1.3. Definições , Acrônimos e Abreviações

Ainda não temos.

## 1.4. Referências

- Documento de Visão
- Documento de Risco
- Documento de Arquitetura

# 2. **Processo de Gerência**

## 2.1. Estimativas de Projeto
A finalidade principal do projeto é desenvolver e gerenciar um sistema complexo de formato distribuído, sendo o foco o uso e consumo de uma API externa, e também evoluir o sistema de uma forma que se torne um negócio validado e, possivelmente, lançado como um produto de real valor no mercado de sistemas.

## 2.2. Plano de Fases

O desenvolvimento do será conduzido usando uma abordagem em fases em que várias iterações ocorrem dentro de uma fase. As fases e a linha do tempo relativa são mostradas na tabela abaixo:

| Fase | Nº de Iterações | Início | Fim |
| ---- | --------------- | ------ | --- |
| Concepção | 2 | 5 de Fevereiro | 4 de Março |
| Elaboração | 2 | 11 de Março | 8 de Abril |
| Construção | 2 | 15 de Abril | 13 de Maio |
| Validação | 2 | 20 de Maio | 17 de Junho |

Os marcos que marcam o final de cada fase podem ser vistos na tabela abaixo.

| Marco | Descrição |
| --------- | ----- |
| Concepção | A fase de concepção busca uma visão inicial para se trabalhar o sistema, deixando como resultado, a clara visualização do sistema a ser desenvolvido (seu escopo, seus principais requisitos e desejos do cliente). Todas as atividades desenvolvidas nesta fase têm este fim, e para tanto necessitam da participação ativa do cliente. Trata-se de uma fase marcada por reuniões e discussões onde inicialmente o cliente apresenta sua visão do sistema, e num segundo momento os projetistas apresentam a visão que puderam capturar do mesmo. |
| Elaboração | O propósito da Fase de Elaboração é analisar o domínio do problema, validar uma arquitetura consistente, onde o sistema será desenvolvido, e desenvolver o plano de projeto. Embora o processo sempre tenha que acomodar mudanças, as atividades desta fase asseguram que a arquitetura, requisitos e planos são bastante estáveis, podendo-se então, determinar o custo de maneira previsível e programar a conclusão do desenvolvimento. |
| Construção | Durante a fase de construção, todos os componentes e características restantes da aplicação são desenvolvidos, testados e integrados ao produto.A fase de construção é, de certo modo,um processo industrial, no qual é enfocado o gerenciamento de recursos, prazos e qualidade. |
| Validação | O foco da Fase de Validação é assegurar que o software esteja disponível para seus usuários finais.Ela pode atravessar várias iterações e inclui testes do produto em preparação para release e ajustes pequenos com base no feedback do usuário. |

## 2.3. Plano da fase de concepção

A fase de concepção do projeto pode ser vista da seguinte forma:

| Tarefa | Início | Fim |
| --- | --- | --- |
| Revisar a definição do projeto | Sábado 29/02/2020 | Quinta-feira 05/03/2020 |
| Revisar escopo do projeto | Sábado 29/02/2020 | Quarta-feira 04/03/2020 |
| Revisar funcionalidades e restrições do sistema | Sábado 29/02/2020 | Quinta-feira 05/03/2020 |
| Revisar a divisão do problema em casos de uso | Sábado 29/02/2020 | Sábado 07/03/2020 |
| Classificar casos de uso por módulo do sistema | Sábado 29/02/2020 | Domingo 08/03/2020 |
| Descrever brevemente os casos de uso | Sábado 29/02/2020 | Quarta-feira 11/03/2020 |
| Analisar o modelo de casos de uso | Sábado 29/02/2020 |   |
| Reunir equipe e clientes para avaliação da arquitetura candidata | Sábado 29/02/2020 |   |
| Elaborar documento de arquitetura do sistema | Sábado 29/02/2020 | Quarta-feira 11/03/2020 |
| Confeccionar protótipos das telas iniciais do sistema | Sábado 29/02/2020 |   |
| Especificar sistema operacional | Sábado 29/02/2020 |   |
| Elaborar documento de arquitetura do sistema | Sábado 29/02/2020 | Quarta-feira 11/03/2020 |
| Especificar ferramentas de escritório | Sábado 29/02/2020 | Quarta-feira 11/03/2020 |
| Especificar a ferramenta da gerência | Sábado 29/02/2020 | Quarta-feira 11/03/2020 |
| Configurar as ferramentas | Sábado 29/02/2020 | Domingo 08/03/2020 |
| Elaborar documentação de ambiente | Sábado 29/02/2020 | Quarta-feira 11/03/2020 |
| Planejar reuniões com a equipe | Sábado 29/02/2020 | Terça-feira 03/03/2020 |

## 2.3. Plano da fase de elaboração

A fase de elaboração do projeto pode ser vista da seguinte forma:

| Tarefa | Início | Fim |
| ------ | ------ | --- |
| Observar as funcionalidades do TimeTables | Domingo 08/03/2020 |   |
| Revisar o documento de visão | Segunda-feira 09/03/2020 | Quarta-feira 11/03/2020 |
| Revisar o Diagrama Geral de Casos de Uso | Terça-feira 10/03/2020 | Terça-feira 10/03/2020 |
| Registrar reunião da equipe do dia 10/03/2020 | Terça-feira 10/03/2020 | Quarta-feira 11/03/2020 |
| Escolher Casos de Uso para validação de arquitetura | Quarta-feira 11/03/2020 |   |
| Iniciar implementação dos CDUs escolhidos | Quarta-feira 11/03/2020 |   |
| Identificar mudanças nos requisitos | Quarta-feira 11/03/2020 |   |
| Revisar documento de Visão, Arquitetura e Especificação de CDUs | Quarta-feira 11/03/2020 |   |
| Elaborar Diagramas de Sequência do Sistema | Quarta-feira 11/03/2020 |   |
| Realizar a disciplina de Implementação e Testes para os CDUs implementados | Quarta-feira 11/03/2020 |   |
| Registrar reunião da equipe do dia 15/03/2020 | Quarta-feira 11/03/2020 | Segunda-feira 16/03/2020 |

## 2.5. Objetivos da Iteração

| Fase | Iteração | Descrição | Marcos Associados | Riscos Associados |
| --- | --- | --- | --- | --- |
| Concepção | Início do projeto |   | Gerência de Processo [concepção]Implementação e Testes [concepção]Análise e Projeto [concepção]Requisitos [concepção] |    |
| Elaboração |   |   | Gerência de Processo [elaboração]Implementação e Testes [elaboração]Análise e Projeto [elaboração]Requisitos [elaboração] |   |
| Construção |   |   | Gerência de Processo [construção]Implementação e Testes [construção]Análise e Projeto [construção]Requisitos [construção] |   |
| Validação |   |   | Gerência de Processo [validação]Implementação e Testes [validação]Análise e Projeto [validação]Requisitos [validação] |   |