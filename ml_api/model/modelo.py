import numpy as np
import joblib


class Model:

    def carrega_modelo(self, path):
        """Carrega o modelo .joblib
        """

        model = joblib.load(path)

        return model

    def preditor(self, model, form):
        """Realiza a predição se o empregado deixará o emprego com base no modelo treinado
        """
        X_input = np.array([form.preg,
                            form.plas,
                            form.pres,
                            form.skin,
                            form.test,
                            form.mass,
                            form.pedi,
                            form.age
                            ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        resultado = model.predict(X_input.reshape(1, -1))
        return int(resultado[0])
