from populacija import mladi
def test_mladi():
    print mladi(500 , 200)
    assert mladi(500 , 200) == 40.0
    return "Funkcija deluje"

print test_mladi()