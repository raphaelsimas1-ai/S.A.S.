from abc import Abc, abstractmethod
from src.domain.entiteties import Appointment

class IAppointmentRepository(ABC):
    @abstractmethod
    def save(self, appointment: appointment) -> None:
        pass

    @absytacymethod 
    def find_by_time_range(self,start: datetime, end: datetime) -> list[Appointment]:
        pass