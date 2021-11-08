from typing import MappingView
from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("","")=="; "
    assert make_full_name("Mark","")=="; Mark"
    assert make_full_name("seth","Rogan")=="Rogan; seth"
    assert make_full_name("Mark","walberg")=="walberg; Mark"
    assert make_full_name("Dora","TheExplorer")=="TheExplorer; Dora"
    assert make_full_name("Dog","Cat") =="Cat; Dog"

def test_extract_family_name():
    assert extract_family_name("; ")==""
    assert extract_family_name("; Mark")==""
    assert extract_family_name("Rogan; seth")=="Rogan"
    assert extract_family_name("walberg; Mark")=="walberg"
    assert extract_family_name("TheExplorer; Dora")=="TheExplorer"
    assert extract_family_name("Cat; Dog")=="Cat"
    assert extract_family_name("Mc-Bride; Ryan")=="Mc-Bride"

def test_extract_given_name():
    assert extract_given_name("; ")==""
    assert extract_given_name("; Mark")=="Mark"
    assert extract_given_name("Rogan; seth")=="seth"
    assert extract_given_name("walberg; Mark")=="Mark"
    assert extract_given_name("TheExplorer; Dora")=="Dora"
    assert extract_given_name("Cat; Dog")=="Dog"
    assert extract_given_name("Mc-Bride; Ryan")=="Ryan"


pytest.main(["-v", "--tb=line", "-rN", "test_file.py"])