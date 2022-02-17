import pytest

def testINTplus():
    assert 5+5 == 10

def testDICTlen():
    assert len({'A':1, 'B':2,'C':3}) == 3

def testINTparity():
    assert 3%2 == 1

def testDICTin():
    assert ('A' in {'A':1, 'B':2,'C':3}) == True


def testDICTdel():
    try:
        assert  {'A':1, 'B':2,'C':3}.pop('F')
    except KeyError:
        pass

@pytest.mark.parametrize('int',[30,40,50,60])
def testINTover100(int):
    assert (int*4) > 100


if __name__ == '__main__':
    pytest.main()