from router.router import route


def test_create_order():

    result = route(
        "закажи кофе"
    )

    assert result["intent"] == "create_order"