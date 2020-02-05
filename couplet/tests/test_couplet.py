from couplet import __version__, babies


def test_version():
    assert __version__ == '0.1.0'

def test_babies():
    assert 'walcum' in babies()