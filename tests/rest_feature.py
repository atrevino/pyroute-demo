
def test_get_gender_female(I):
    resp = I.send_get_request('?gender=female').json()
    result = resp['results'][0]
    gender = result['gender']

    assert gender in 'female'


def test_get_gender_male(I):
    resp = I.send_get_request('?gender=male').json()
    result = resp['results'][0]
    gender = result['gender']

    assert gender in 'male'


def test_with_us_nationality(I):
    resp = I.send_get_request('?nat=us').json()
    result = resp['results'][0]
    nationality = result['nat']

    assert nationality in 'US'


def test_with_unknown_nationality(I):
    resp = I.send_get_request('?nat=klj').json()
    result = resp['results'][0]
    nationality = result['nat']

    assert nationality in 'klj'
