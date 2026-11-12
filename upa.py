
from abc import ABC, abstractmethod 
from dataclasses import dataclasses

@dataclasses(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

class Atendimento(ABC)
    def __init__(self, paciente: Paciente) -> None:
        self._paciente: Paciente = paciente

    @property
    def paciente(self) -> Paciente:
        return self._paciente
    
    @abstractmethod
    def duracao_minutos(self) -> int:
        pass

    def __str__(self) -> str:
        return (
            f"{self.__clss__.__nome__}"
            f"Paciente: {self.paciente.nome} -"
            f"Duração: {self.duracao_minutos()} min"
        )


class Comsulta(Atendimento):
    def __init__(
        self, paciente: Paciente,
        especialidade: str, 
        retorno: bool = False) -> None:
        super().__init__(paciente)
        self.especialidade: str = especialidade
        self.retorno: bool = retorno
    
    def duracao_minutos(self) -> int:
        if self.retorno:
            return 15

        return 30

class Exame(Atendimento):
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool = False) -> None
        super().__init__(paciente)
        self.tipo: str = tipo
        self.jejum: bool = jejum

    def duracao_minutos(self) -> int:
        if self.jejum:
            return 30

        return 20 

class Vacinacao(Atendimento):
    def __init__(self, paciente: Paciente, vacina: str, doses: int = 1) -> 
        super().__init__(paciente)
        self.vacina: str = vacina
        self.doses: int = doses

    def duracao_minutos(self) -> int:
        return 10 * self.doses
