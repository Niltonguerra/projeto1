### Serviços / Recursos

#### Sistema Agendador de Coleta de Dados

**Responsabilidade:** agendar as coletas de dados.

**Justificativa da stack:** Rust foi escolhido por interesse pessoal de estudo, não por exigência técnica do problema. Para um agendador, qualquer linguagem atenderia igualmente bem — não há requisito funcional que torne Rust superior às alternativas aqui. A comunicação com os demais serviços será feita via RabbitMQ, padrão de mensageria adotado no restante do sistema.

---

#### Sistema Coletor de Dados

**Responsabilidade:** coletar dados externos (Banco Central, Brapi, CVM, IBGE) e encaminhar para o sistema de enriquecimento.

**Justificativa da stack:** NestJS foi escolhido por permitir uso de TypeScript, o que possibilita validação de propriedades e chaves dos diversos formatos de dados recebidos das diferentes fontes — um facilitador de segurança e consistência a longo prazo. Java também seria uma opção viável. A decisão final por NestJS considerou também o uso planejado de Kafka como mensageria neste serviço específico (motivado por interesse em estudar a ferramenta), além de maior vivência prática com o ecossistema Node/NestJS. **O Coletor publica os dados coletados em Kafka**, consumido pelo sistema de Enriquecimento.

---

#### Sistema de Enriquecimento de Dados

**Responsabilidade:** enriquecer os dados conforme regras de negócio definidas (ex.: lógica de avaliação de empresas, lógica de previsão macroeconômica) e encaminhar para o sistema de tagueamento.

**Justificativa da stack:** Java foi escolhido pela quantidade prevista de regras de negócio e manipulação/refinamento de dados. Python seria uma alternativa igualmente adequada para esse tipo de processamento, mas a tipagem forte e a orientação a objetos do Java foram consideradas mais úteis para lidar com um volume grande de regras e cálculos complexos. **Este serviço consome de Kafka** (dados vindos do Coletor) **e publica em RabbitMQ** para o sistema de Tagueamento.

---

#### Sistema de Tagueamento das Informações

**Responsabilidade:** analisar os dados enriquecidos e, com base em regras de negócio, atualizar registros existentes ou criar novos.

**Justificativa da stack:** Python foi escolhido pelo uso planejado de comunicação via MCP para o tagueamento. Já houve experiência anterior usando Node.js para comunicação MCP, com resultado satisfatório, mas Python foi priorizado por ser hoje o padrão de mercado predominante para integração com IA. **Este serviço recebe os dados do Enriquecimento via RabbitMQ.**

---

#### Sistema Sincronizador de Dados

**Responsabilidade:** sincronizar bancos de dados com base em eventos.

**Justificativa da stack:** Go foi escolhido pela sua performance. Como a arquitetura separa banco de leitura (Elasticsearch) e banco de escrita (Postgres), a velocidade de sincronização entre eles foi considerada um fator relevante. Os eventos que disparam essa sincronização são recebidos via RabbitMQ, mesmo padrão de mensageria adotado no restante do sistema.

---

#### SGBD 1 (Escrita)

**Responsabilidade:** armazenar dados de investimentos, com foco em escrita.

**Justificativa da stack:** Postgres foi escolhido porque o volume de dados tem crescimento estimado e limitado — não há expectativa de escala excessiva. Dado esse cenário, o conjunto de ferramentas do Postgres foi considerado mais adequado do que outras opções relacionais, não relacionais ou colunares.

---

#### SGBD 2 (Leitura)

**Responsabilidade:** otimizar consultas de leitura sobre os dados de investimentos.

**Justificativa da stack:** Elasticsearch foi escolhido por facilitar busca, seleção e filtragem de campos de forma simples e eficiente, otimizando o padrão de acesso de leitura.