import core.utils as utils


def test_should_get_domain(db):
    assert utils.get_domain() == 'http://example.com'


def test_should_get_domain_raise_error(db, mocker):
    mock = mocker.patch.object(utils, 'Site')
    mock.objects.get_current.side_effect = Exception
    assert utils.get_domain() == ''
