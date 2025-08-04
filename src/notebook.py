# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime


class Note:
     HIGH: str = "HIGH"
     MEDIUM: str = "MEDIUM"
     LOW: str = "LOW"

     def __innit__(self, code: str, title: str, text: str, importance: str, creation_date: datetime):
        self.code: int = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: str = datetime
        self.tags: list[str] = []

     def add_tag(self, tags: str):
         if tags not in self.tags:
             self.tags.append(tags)

     def __str__(self) -> str:
         Date: {creation_date}
         {title}: {text}

class Notebook:
    def __innit__(self, notes: list[Note]):
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, importance: str)-> int:
       pass
    def delete_note(self, code: int):
        pass
    def important_notes()-> list[Note]
        pass
    def notes_by_tags(self, tags: str) -> list[Note]:
        pass
    def tag_with_most_notes(self) -> str:
        pass
