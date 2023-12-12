## Dataset Employee - Kaggle

Dados do dataset:
- Education - Grau de escolaridade:   (1) Bachelors  (2) Masters  (3) PhD;
- JoiningYear - Ano de admissão;
- PaymentTier - Nível salarial:  1; 2 ou3
- Gender - Gênero:     (1) Male   (2) Female
- EverBanched - Esteve sem alocação no trabalho: (0) No  (1) Yes
- ExperienceInCurrentDomain - Experiência na função atual:    0 à 7
Classe
- LeaveOrNot - Deixará ou não o emprego:   (0) No  (1) Yes



## Problema a resolver

Dentre várias possibilidades de se avaliar estes dados, escolhi verificar a resiliência quando ocorre ficar sem alocação no trabalho, e se o grau de escolaridade poderia influenciar na decisão de ficar no emprego.

## Preparação dos dados

O dataset original possui 4653 linhas.

Total: 4653
deixarão o emprego(leaveOrNot=1): 1600
não deixarão o emprego(leaveOrNot0):3053

O dataset original tinha dados do ano 2012 até 2018. Ocorre que a maioria dos dados de 2018 estavam indicando que os empregados deixaram o emprego. Como isso pareceu uma distorção, os dados de 2018 foram excluídos do dataset.

Foi separado manualmente 500 entradas do ano 2017 para ser o dataset golden, escolhidas de forma aleatória.
Os demais ficaram no dataset para treinar o modelo.

Preparação:

1) Retirada da informação Localidade;

2) Mapeamento das colunas para valores inteiros: 
    Escolaridade (Education)
        Bacharel (Bachelors) -> 1
        Mestre (Masters) -> 2
        Phd (PHD) -> 3 
    Gênero (Gender)
        Masculino (Male) -> 1
        Feminino (Female) -> 0
        
    

## Escolha do Modelo de Machine Learning

Foi utilizado o Colab para testar os modelos: KNN, CART, Naive-Bayes e SVM.

O melhor resultado foi para o SVM padronizado.

## Métrica
Foi escolhida a Acurácia (acertos de previsão), que deverá ser maior ou igual a 70%.

## Aplicação web
   1 - O modelo treinado será colocado no backend;
   2 - O usuário pode fornecer dados de um empregado e obter a previsão se deixará ou não o emprego;
   3 - O sistema permitirá realizar testes com um dataset gold, a fim de obter a acurácia, e verificar se o modelo treinado atende ao requisito mínimo de acurácia.
