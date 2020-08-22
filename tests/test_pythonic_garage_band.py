from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band,Musician,Guitarist,Bassist,Drummer
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def prep_data():
    Alan_Waker = Guitarist('Alan Waker')
    sia = Bassist('sia')
    Dan_Reynolds=Drummer('Dan Reynolds')
    Imagine_Dragons_test= (Band("Imagine Dragons", [Alan_Waker,sia,Dan_Reynolds]))
    return {'Alan_Waker':Alan_Waker,'sia':sia,'Dan_Reynolds':Dan_Reynolds,'Imagine_Dragons_test':Imagine_Dragons_test}

def test_name(prep_data):
    expected = 'Alan Waker'
    actual = prep_data['Alan_Waker'].name
    assert actual == expected

def test_str(prep_data):
    expected = 'The name:sia'
    actual = prep_data['sia'].__str__()
    assert actual == expected


def test_repr(prep_data):
    expected = 'Guitarist : Alan Waker'
    actual = prep_data['Alan_Waker'].__repr__()
    assert actual == expected

def test_get_instrument(prep_data):
    acutal = prep_data['Dan_Reynolds'].get_instrument()
    expected = 'instrument : drums'
    assert expected==acutal

def test_play_solo(prep_data):
    actual = prep_data['Dan_Reynolds'].play_solo()
    expected = 'play_solo from Drummer class'
    assert expected ==actual

    
def test_band(prep_data):
    actual = len(Band.to_list)
    expected =6#coz I called the prep_data 6 times 
    assert expected ==actual