# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime


class Note:
     HIGH: str = "HIGH"
     MEDIUM: str = "MEDIUM"
     LOW: str = "LOW"

     def __innit__(self, code: str, title: str, text: str, importance: str, creation_date: datetime):
        self.code: str = code
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






