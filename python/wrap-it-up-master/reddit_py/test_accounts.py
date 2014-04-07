import accounts as a

client = a.user_login(user_name='rb640', password='Florida7777', bot_desc='foo')


def test_user_login():
    assert client.user == 'rb640'


def test_current_account_overview():
    overview = a.current_account_overview(client)
    assert 'comment_karma' in overview.keys()
    assert overview['link_karma'] == 1



