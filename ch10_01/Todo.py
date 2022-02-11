from dataclasses import dataclass

@dataclass
class Todo:
    id:int
    title:str
    userId:int
    completed:bool


