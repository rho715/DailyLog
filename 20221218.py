#post__init__
#field 사용하여 목록 속성을 기본값 지정
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Person:
    first_name:str
    last_name:str
    full_name:str = field(init=False)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

user = Person(first_name='Steve', last_name='Jobs') 
print(user.full_name)