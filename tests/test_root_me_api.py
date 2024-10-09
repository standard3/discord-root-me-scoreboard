from root_me_scoreboard_bot.utils.api import API, Endpoints

api = API()


async def test_get():
    response = await api.get(Endpoints.challenges)
    assert response


async def test_get_user_by_id():
    user = await api.get_user_by_id(2600)

    assert user
    assert user.name == "drakenshot"
    assert user.id == 2600
    assert user.status == "6forum"
    assert type(user.score) == int()
    assert type(user.position) == int()
