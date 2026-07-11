## regras gerais
- 

## serviços/recursos

### sistema agendador de coleta de dados
responsável por agendar as coletas de dados


### sistema coletor de dados
responsável por coletar dados externos, nele vai estar as classes responsaveis por coletar os dados do banco central, brapi,cvm e ibge
resposavel por encaminhar para o enriquecimento de dados


### sistema de enriquecimento de dados
responsável por enriquecer os dados com base da regra de negócio de enriquecimento desejada.ex: enriquecimento dados sobre uma lógica de avaliação de emrpresa,enriquecimento de dados sobre lógica de avaliação para prever macro economia e etc.
resposavel por encaminhar para o sistema ded tagiamento


### sistema de tagiamento das informações
responsável por tagiar as informações geradas, ele basicamente vai ver as informações enriquecidas e vai atualizar dados ou criar um novo registro tudo segundo regras de negócio


### SGBD 1