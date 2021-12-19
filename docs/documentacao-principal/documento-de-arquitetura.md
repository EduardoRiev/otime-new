# OTime

## Documento de arquitetura do Sistema 
#### Histórico de Revisão
| Data | Versão | Descrição | Autor |
| ------ | ------ | ------ | ------ |
|10-03-2020|1.0|Descrição da primeira arquitetura usada no OTime| Fernanda G.|
#### Visão do ambiente computacional e físico
Para inicialização do projeto será necessário a instalação do pacote Django que pode ser instalado através do Pip, um gerenciador de pacotes usado para instalar e gerenciar pacotes de software escritos na linguagem de programação Python. Também será necessária a instalação do Django Rest que servirá como ferramenta para criação da api do O’Time, para seu correto funcionamento é necessário que o ambiente django já esteja na máquina do desenvolvedor. Não há restrições quanto a máquina física utilizada.

### 2.Estilo Arquitetural
#### 2.1 Descrição do estilo arquitetural
`Não definido`
### 3.Pacotes ou Sub-Sistemas
#### 3.1Pacote de interface com o usuário
No Django utiliza-se o modelo MVT(Model View Template), nesse cenário, o pacote de templates é responsável por armazenar as páginas de interação direto com o usuário, os arquivos de extensão html.
#### 3.2 Pacote de negócio (serviços do sistema)
O pacote de views é responsável pela camada de negócio do sistema, ela implementa as restrições antes que os dados sejam gravados no banco de dados, além de fornecer todas as funções que alimentam os templates do sistema.  
#### 3.3 Pacote de persistência
O arquivo responsável pela persistência de dados no sistema é models.py, ele é responsável pela criação das classes de modelo que estruturam o banco de dados. 
#### 3.4 Subsistema de mensagens assíncronas 
`Não definido` 
#### Anexos
##### Diagrama de contexto
![Diagrama De Contexto](doc/img/diagrama-de-contexto.jpg)
