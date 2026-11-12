from abc import ABC, abstractmethod 
from dataclasses import dataclass

from excecoes import HorarioIndisponivelError, PacienteJaAgendadoError

@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

class Atendimento(ABC):
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
            f"{self.__class__.__name__}"
            f"Paciente: {self.paciente.nome} -"
            f"Duração: {self.duracao_minutos()} min"
        )


class Consulta(Atendimento):
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
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool = False) -> None:
        super().__init__(paciente)
        self.tipo: str = tipo
        self.jejum: bool = jejum

    def duracao_minutos(self) -> int:
        if self.jejum:
            return 30

        return 20 

class Vacinacao(Atendimento):
    def __init__(self, paciente: Paciente, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente)
        self.vacina: str = vacina
        self.doses: int = doses

    def duracao_minutos(self) -> int:
        return 10 * self.doses

class Agenda:
    def __init__(self, limite_minutos: int = 240) -> None:
        self.limite_minutos: int = limite_minutos
        self._atendimentos: list[Atendimento] = []

    @property
    def atendimentos(self) -> tuple[Atendimento, ...]:
        return tuple(self._atendimentos)
    
    @property
    def minutos_ocupados(self) -> int:
        return sum(atendimento.duracao_minutos() for atendimento in self._atendimentos)

    def agendar(self, atendimento: Atendimento) -> None:
        for existe in self._atendimentos:
            if existe.paciente == atendimento.paciente: raise PacienteJaAgendadoError(
                f"Paciente {atendimento.paciente.nome}")

            minutos_necessarios: int = atendimento.duracao_minutos()
            minutos_restantes: int = (self.limite_minutos - self.minutos_ocupados)

            if minutos_necessarios > minutos_restantes: raise HorarioIndisponivelError(
                f"Horario Indisponível!" 
                f"{minutos_necessarios} min" 
                f"Restantes {minutos_restantes} min"
                )

            self._atendimentos.append(atendimento)
