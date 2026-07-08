## Contas e Transações

Contas e Transações foram mantidos no mesmo bounded context porque exigem consistência forte (ACID) entre si: uma transação confirmada não pode existir sem que o saldo da conta reflita essa mudança imediatamente. Não há tolerância a inconsistência temporária entre as duas entidades.

Se Contas e Transações fossem separados em bounded contexts distintos (e, por consequência, em serviços distintos), a comunicação entre eles precisaria ser resolvida via consistência eventual — mensageria, orquestração com Saga, e tratamento de falha/compensação para os casos em que a transação e a atualização de saldo divergissem temporariamente. O Teorema CAP explica por que esse trade-off existe em sistemas distribuídos: um sistema particionado não consegue garantir simultaneamente consistência forte e disponibilidade máxima. Como o objetivo aqui é manter consistência forte entre saldo e transação sem lidar com a complexidade adicional de reconciliação distribuída, optou-se por manter os dois no mesmo bounded context, evitando as regras de comunicação assíncrona, a consistência eventual e o uso de Saga que a separação exigiria.

## Concessão de Crédito

Bounded context responsável pelas regras de concessão de crédito, cálculo de juros aplicados a cada usuário, e pelo cálculo do score de crédito do cliente. O score foi absorvido neste contexto (em vez de ser um contexto separado) porque, na modelagem atual, seu único consumidor é o processo de concessão de crédito — não havendo reuso por outro contexto, não há justificativa, pelo critério de Customer-Supplier de Vernon, para tratá-lo como um bounded context independente. Caso outro contexto (como Personalização de Sugestões de Investimento) passe a depender do score, essa decisão deve ser revisitada.

## Personalização de preferencias do usuário

Bounded context responsável pelas regras de personalização de notícias e investimentos exibidas a cada usuário, com base nos temas de interesse definidos por ele.

## Criptomoeda

Bounded context responsável pelas questões referentes à criptomoeda utilizada no sistema (protocolo, transação, validação). Por ser uma área de menor domínio de conhecimento no momento da modelagem, foi mantido como um único contexto, sem subdivisões internas.

## Captura de Notícias sobre Investimento

Bounded context dedicado à captura de dados sobre noticias, com regras de negócio próprias sobre o que pode ou não ser coletado das fontes de dados.

## Captura de Dados de investimento

Bounded context dedicado à captura de dados de informações de investimento, com regras de negócio próprias sobre o que pode ou não ser coletado das fontes de dados