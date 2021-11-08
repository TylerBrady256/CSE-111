from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city(",,")==""
    assert extract_city("8865 Tenbury Ct,Bristow, VA 20136")=="Bristow"
    assert extract_city("8000 YODOG St,Gainesville,VA 20136")=="Gainesville"
    assert extract_city("13 Elm St, Milwaukee,WY 22200")=="Milwaukee"
    assert extract_city("500 JJ Ct,St.Louis,MO 21300")=="St.Louis"
    assert extract_city("400 Pizz-a St,Rexburg,ID 14820")=="Rexburg"

def test_extract_state():
    assert extract_state(",,")==" "
    assert extract_state("8865 Tenbury Ct,Bristow, VA 20136")==" "
    assert extract_state("8000 YODOG St,Gainesville,VA 20136")==" "
    assert extract_state("13 Elm St, Milwaukee,WY 22200")==" "
    assert extract_state()==" "
    assert extract_state()==" "

def test_extract_zipcode():
    assert extract_zipcode("8865 Tenbury Ct,Bristow, VA 20136")==" "
    assert extract_zipcode("8000 YODOG St,Gainesville,VA 20136")==" "
    assert extract_zipcode("13 Elm St, Milwaukee,WY 22200")==" "
    assert extract_zipcode()==" "
    assert extract_zipcode()==" "
    assert extract_zipcode()==" "



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN","test_address.py"])