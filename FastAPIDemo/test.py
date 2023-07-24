from enum import Enum
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

class Color(Enum):
    Black = 1
    White = 2
    Gray = 3

class MyClass:
    def __init__(self, x: int = 0):
        self.x = x

object_local = MyClass(1)

async def read_item(function_parameter: str):
    print(function_parameter)
    return templates.TemplateResponse("test.html",
                                      {
                                        "function_parameter": function_parameter,
                                        "function_parameter_diffname": function_parameter,
                                        "literal_bool": False,
                                        "literal_int": 42,
                                        "literal_string": "string",
                                        "literal_enum": Color.Black,
                                        "object_local": object_local,
                                        "object_local_diffname": object_local,
                                        "object_inline": MyClass(2),
                                        "bar": object_local
                                      }
                                     )