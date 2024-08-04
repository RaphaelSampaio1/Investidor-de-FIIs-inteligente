# Sistema de Gerenciamento de Investimentos em FIIs

Desenvolvi um sistema para organizar e gerenciar meus investimentos em FIIs utilizando Python, Flask e AWS!

Este projeto foi criado para facilitar e otimizar a administração da minha carteira de Fundos de Investimento Imobiliário (FIIs). O sistema combina tecnologias modernas para fornecer uma solução eficiente e intuitiva. Confira os detalhes abaixo:

## Tecnologias Utilizadas:
- **Python e Flask**: Para o desenvolvimento do backend e lógica de aplicação.
- **PostgreSQL**: Banco de dados utilizado para armazenar informações dos investimentos, hospedado na AWS.
- **SQLAlchemy**: Biblioteca ORM para integrar o Flask com o PostgreSQL.
- **AWS**: Para o deploy do banco de dados PostgreSQL, garantindo alta disponibilidade e escalabilidade.

## Funcionalidades Principais:
- **Tela Inicial**: Visualize o valor total investido em FIIs e acompanhe a performance da carteira de maneira clara e objetiva.
- **Simulação de Investimento**: Simule novos investimentos inserindo o valor desejado. O sistema calcula e sugere a melhor distribuição com base nas porcentagens definidas para cada tipo de fundo.
- **Aplicação de Investimento**: Após a simulação, aplique os investimentos diretamente no sistema. Os dados são armazenados no banco de dados PostgreSQL para um gerenciamento seguro e eficiente.
- **Atualização em Tempo Real**: A página inicial é atualizada automaticamente com os novos valores investidos, refletindo as aplicações recentes.

## Fundos de Investimento Imobiliário (FIIs) Incluídos:
Os fundos disponíveis no sistema são:
- **HGLG11**
- **HFOF11**
- **MXRF11**
- **VILG11**
- **RZTR11**

O valor simulado é distribuído entre esses fundos de acordo com as porcentagens detalhadas no código. Cada fundo possui uma alocação específica, ajustada para otimizar a distribuição do investimento com base nas características de cada fundo.

Este sistema não apenas melhora a organização dos meus investimentos, mas também proporciona uma maneira prática e automatizada de gerenciar minha carteira de FIIs. A combinação de Python, Flask e AWS garante um desempenho robusto e escalável.

