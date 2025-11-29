from main import Item


def test_item_model():
    it = Item(name="TestItem", price=12.5)
    assert it.name == "TestItem"
    assert it.price == 12.5
    assert it.description is None
    assert it.tax is None
