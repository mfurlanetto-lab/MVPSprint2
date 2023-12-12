from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros
url_dados = "datasets\Employee_golden.csv"
colunas = ['Education', 'JoiningYear', 'PaymentTier', 'Age',
           'Gender', 'EverBenched', 'ExperienceInCurrentDomain', 'LeaveOrNot']


# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)


# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]


# Método para testar modelo SVM a partir do arquivo correspondente
def test_modelo_svm():
    # Importando modelo de SVM
    svm_path = 'ml_modelo\modelo_treinadoSVM.joblib'
    modelo_svm = modelo.carrega_modelo(svm_path)

    # Obtendo as métricas do SVM
    acuracia_svm = avaliador.avaliar(
        modelo_svm, X, Y)

# Testando as métricas do SVM
# Modifique as métricas de acordo com seus requisitos
    assert acuracia_svm >= 0.7
