from datamodel.datamodel import TestDataModel


def test_test_datamodel() -> None:
    dm = TestDataModel()
    fighters = dm.get_fighters()
    assert len(fighters) == 3
    assert fighters[0].name == "Ronaldo Souza"
    assert fighters[1].name == "Roger Gracie"
    assert fighters[2].name == "Rafael Lovato Jr."
