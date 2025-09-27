from ninja import Field, schema, ModelSchema
from django.db import models

from book_api.books.models import Author, Book

# Schema para o Autor (Simula GetIdName)
class AuthorOut(ModelSchema):
    """
     Schema para mostrar o autor
    """
    class Meta:
        model = Author
        model_fields = ['id', 'name']

# --- Schema Principal (O equivalente a EmployeeGetId) ---  
class BookGetId(ModelSchema):
    """
     schema responsável por mostrar os campos detalhados de um livro
    """
    author: AuthorOut = Field(..., description='Detalhes do Autor')
    is_active: bool = Field(..., description='Status de atividade')
    
    class Meta:
        model = Book
        model_fields = ['id', 'title', 'is_active']
        
    