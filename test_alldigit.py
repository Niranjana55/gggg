import alldigit

def test_CanAssertTrue():
    assert True

def test_36returnTrue():
    #arrange
    n = 35
    excepted = True
    #act
    actual = alldigit.numdivN(n)
    #assert
    assert excepted == actual
