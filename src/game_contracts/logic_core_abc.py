from pydantic import BaseModel, model_serializer
from abc import abstractmethod
from typing import ClassVar, Optional


class GameState(BaseModel):

    @abstractmethod
    def model_post_init(self, __context):
        pass

    @property
    def is_game_over(self):
        return False  # Placeholder for game over logic


class CommandResult(BaseModel):
    success: bool = True
    pending_commands: list[str] = []  # List of serialized command JSONs
    message: Optional[str] = None


class Command(BaseModel):
    controller_id: str
    category: ClassVar

    @abstractmethod
    def execute(self, game_state: GameState) -> CommandResult:
        pass

    @model_serializer
    def model_dump(self, *args, **kwargs):
        data = self.__dict__.copy()
        data["category"] = self.category
        return data
