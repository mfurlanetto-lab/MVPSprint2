from sklearn.metrics import accuracy_score


class Avaliador:

    def avaliar(self, modelo, X_test, Y_test):
        """ Faz uma predição e avalia o modelo pela acurácia e especificidade.
        """
        predicoes = modelo.predict(X_test)

        return (accuracy_score(Y_test, predicoes))
