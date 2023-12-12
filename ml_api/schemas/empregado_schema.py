from pydantic import BaseModel


class EmpregadoSchema(BaseModel):
    """ Define como o Empregado a ser consultado deve ser representado
    """
    education: int = 1
    joiningYear: int = 2015
    paymentTier: int = 2
    age: int = 30
    gender: int = 2
    everBenched: int = 0
    experienceInCurrentDomain: int = 5


class ResultadoSchema(BaseModel):
    """Define como o resultado da previsão deve ser representado
    """
    resultado: str = "0"
