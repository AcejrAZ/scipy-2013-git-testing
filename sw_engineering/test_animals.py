import animals


def test_read_animals():
    ref_dates = ['2011-04-22', '2011-04-23', '2011-04-23', '2011-04-23', '2011-04-23']

    dates, time, species, counts = animals.read_animals('animals.txt')

    assert dates == ref_dates


    

