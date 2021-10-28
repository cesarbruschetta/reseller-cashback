from core.serializers import ResellerSerializer


def test_should_serializer_user_raise_email(reseller_user, admin_user):
    val_dict = {'email': reseller_user.email}
    serializer = ResellerSerializer(data=val_dict, instance=admin_user)

    assert serializer.is_valid() is False
    assert str(serializer.errors['email'][0]) == 'The e-mail must be unique.'


def test_should_serializer_user_update(reseller_user, admin_user):
    val_dict = reseller_user.__dict__
    val_dict['full_name'] = 'New Reseller'
    serializer = ResellerSerializer(data=val_dict, instance=reseller_user)

    assert serializer.is_valid() is True
    assert serializer.save()
