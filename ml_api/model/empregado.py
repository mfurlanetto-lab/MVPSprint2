from datetime import datetime


class Empregado():

    def __init__(self, education: int, joiningYear: int, paymentTier: int, age: int,
                 gender: int, everBenched: int, experienceInCurrentDomain: int):
        """
        Dados do empregado a ser consultado

            education: Grau acadêmico - (1) Bacharelado; (2) Mestrado; (3) PhD
            joiningYear: Ano de admissão - Formato AAAA
            paymentTier: Nível salarial - 1,  2 ou 3
            age: Idade
            gender: Gênero - (1) Masculino; (2) Feminino
            everBenched: Já esteve sem alocação no trabalho - (1) Sim; (0) Não
            experienceInCurrentDomain: Experiência na função atual - 0, 1, 2, 3, 4, 5, 6 ou 7

        """
        self.education = education
        self.joiningYear = joiningYear
        self.paymentTier = paymentTier
        self.age = age
        self.gender = gender
        self.everBenched = everBenched
        self.experienceInCurrentDomain = experienceInCurrentDomain

    def validar_dados(self):

        # Valida dados do formulário
        if (self.education == '' or self.joiningYear == '' or self.paymentTier == '' or self.age == '' or self.gender == '' or self.everBenched == '' or self.experienceInCurrentDomain == ''):
            raise ValueError('Informações não preenchidas. Verifique!')

        if not (isinstance(self.education, int) and isinstance(self.joiningYear, int) and isinstance(self.paymentTier, int) and isinstance(self.age, int) and isinstance(self.gender, int) and isinstance(self.everBenched, int) and isinstance(self.experienceInCurrentDomain, int)):
            raise ValueError('Informações inválidas. Verifique!')

        # Domínios validados
        # Educação
        if (self.education < 1 or self.education > 3):
            raise ValueError('Selecione um grau de educação válido.')

        # Ano de admissão
        if (self.joiningYear <= 1950 or self.joiningYear > datetime.now().year):
            raise ValueError('Informe um ano de admissão válido.')

        # Nível de salário
        if (self.paymentTier < 1 or self.paymentTier > 3):
            raise ValueError('Selecione um nível de salário válido.')

        # Idade
        if (self.age < 18 or self.age > 90):
            raise ValueError('Informe uma idade válida para o empregado.')

        # Gênero
        if (self.gender not in {1, 2}):
            raise ValueError('Selecione um gênero válido.')

        # Esteve sem alocação no trabalho
        if (self.everBenched not in {1, 0}):
            raise ValueError("Selecione uma opção válida para 'Esteve sem alocação no trabalho'.")

        # Experiência na função atual
        if (self.experienceInCurrentDomain < 1 or self.experienceInCurrentDomain > 7):
            raise ValueError("Selecione uma opção válida para 'Experiência na função atual'.")


