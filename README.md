# Coffee-Machine
Coffee Machine, Python Code

Descrição:
Este código Python implementa um simulador básico de uma máquina de café. A máquina oferece três tipos de bebidas: espresso, café com leite e cappuccino. Cada bebida tem sua própria receita de ingredientes e custo associado.

O código mantém um registro dos recursos disponíveis na máquina, como água, leite e café, além de acompanhar o custo total das vendas realizadas.

Os principais componentes do código são:

MENU: Um dicionário que define as opções de bebidas disponíveis, juntamente com os ingredientes necessários e os custos associados a cada uma.

recursos: Um dicionário que rastreia a quantidade disponível de cada recurso na máquina.

funções:

recursos_suficientes: Verifica se há recursos suficientes na máquina para fazer a bebida solicitada.
processar_pagamento: Solicita ao usuário que insira o valor do pagamento e calcula o total recebido.
sucesso_transacao: Verifica se o pagamento é suficiente e fornece troco, se necessário.
fazer_cafe: Deduz os ingredientes utilizados para fazer a bebida do total de recursos disponíveis.
loop principal: Executa o programa principal, onde o usuário pode escolher uma bebida, verificar o relatório de recursos ou desligar a máquina.

Este código pode ser útil para entender os princípios básicos de processamento de transações, controle de recursos e estruturas de dados em Python, além de servir como base para o desenvolvimento de sistemas mais complexos de gerenciamento de vendas de bebidas.

