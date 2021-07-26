from main import world_cup_logger


def test_world_cup_logger():
    country = "Alemanha"
    year_list = [2014, 1990, 1974, 1954]

    result = world_cup_logger(country, *year_list)
    expected = "Alemanha - 1954, 1974, 1990 e 2014"

    assert (
        result == expected
    ), "Verifique se a montagem da string foi feita corretamente"
