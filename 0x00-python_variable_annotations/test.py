0-add.py

def add(a: float, b: float)-> float:
    return a + b


print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)



1-concat.py



def concat(str1: str, str2: str ) ->str:
    return str1+str2

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)


2-floor.py


import math

def floor(n:float) ->int:
     return math.floor(n)

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))



3-to_str.py


def to_str(p: float) -> str:
    return str(p)
    
pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))



4-define_variables.py



a:int = 1
pi:float = 3.14
i_understand_annotations:bool = True
school:str= 'Holberton'




print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))


5-sum_list.py



from typing import List
def sum_list(input_list : List[float]) -> float:
    sum : float = 0
    for i in input_list:
        sum+=i
    return sum
    

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))




6-sum_mixed_list.py
from typing import List , Union
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum : float = 0
    for i in mxd_lst:
        sum+=i
    return sum


print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))


7-to_kv.py


from typing import Tuple ,Union
def to_kv(k: str, v:Union[int, float]) -> Tuple[str, float]:
    return (k,v*v)
print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))

8-make_multiplier.py
from typing import Callable
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier

print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))


9-element_length.py
from typing import Iterable, List, Sequence, Tuple
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]

print(element_length.__annotations__)

