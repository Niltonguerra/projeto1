## serviços/recursos

### sistema agendador de coleta de dados
responsável por agendar as coletas de dados

#### explicação da steak adotada:
- usarei rust para fazer esse serviço porque eu simplesmente estou com muita vontade de estudar ele, não tem nenhuma outra definição tecnica além dessa, para um agendador qualquer linguagem serviria então decidi usar o rust





### sistema coletor de dados
responsável por coletar dados externos, nele vai estar as classes responsaveis por coletar os dados do banco central, brapi,cvm e ibge
resposavel por encaminhar para o enriquecimento de dados

#### explicação da steak adotada:
nessa irei usar o nestJS porque ele permite usar o typescript e como vou trabalhar com varios fontes de dados quero poder validar suas propriedades e chaves para ter maior segurança, acredito que isso vai ser um facilitador a longo prazo,poderia usar também java, mas como também pretendo usar um serviço de kafka como mensageria porque quero estudar kafka então então preferi usar o nestJS porque tenho mais vivencia com o mesmo



### sistema de enriquecimento de dados
responsável por enriquecer os dados com base da regra de negócio de enriquecimento desejada.ex: enriquecimento dados sobre uma lógica de avaliação de emrpresa,enriquecimento de dados sobre lógica de avaliação para prever macro economia e etc.
resposavel por encaminhar para o sistema ded tagiamento

#### explicação da steak adotada:
aqui estou usando java porque pretendo implementar bastantes regras de negócio para fazer tratamento de dados além de também fazer manipulação desses mesmo dados para deixalos mais refinados, é claro, daria para usar python, ele também é muito bom para isso, mas preferi usar o java por conta da tipagem forte e orientação a objeto que acredito que vão ser ferramentar uteis no desenvolvimento em um mar de regras de negocio e calculos complexos



### sistema de tagiamento das informações
responsável por tagiar as informações geradas, ele basicamente vai ver as informações enriquecidas e vai atualizar dados ou criar um novo registro tudo segundo regras de negócio

#### explicação da steak adotada:
aqui irei usar o python porque pretendo usar uma comunicação MCP para fazer o tagiamento, pretendo usar o python porque hoje em dia ele é a melhor linguagem para se comunicar com AI, já usei já node para fazer uma comunicação com MCP e ficou legal, mas como o python parece ser o padrão de mercado para esse tipo de coisa irei usar o mesmo



### sistema sincronizador de dados
sistema destinado a sincronização de bancos de dados com base em eventos

#### explicação da steak adotada:
aqui irei usar o golang porque ele é uma linguagem rapida e considerando que estou usando uma abordagem de um banco de dados para leitura(elasticsearch) e outro para escrita(postgres), acredito que velocidade seja algo importante


### SGBD 1
banco de dados com informações de investimentos, destinado principalmente para a escrita de dados
#### explicação da steak adotada:
irei usar o postgres aqui porque como os dados não iram crescer indefinitivamente com uma escala escessivament grande, tendo uma ideia já de qual vai ser o tamanho e que não vai crescer muito mais que aqui, acredito que o postgres com as ferramentas que ele já dispoe vai ser mais util que qualquer outro banco relacional ou não relacional ou até mesmo colunares






### SGBD 2
sistema de banco de dados com foco em leitura de dados  de investimentos  com o objetivo de otimizar consultas de leitura de dados.

#### explicação da steak adotada:
pretendo usar um sgbd elasticsearch por que  ele permite a pesquisa de campos no banco de dados de forma simples e facil através fa seleção e filtragem de dados do banco de dados 