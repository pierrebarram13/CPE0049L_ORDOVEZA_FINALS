from src.services.strategy import EncryptionStrategy

def test_encryption():

    strategy = EncryptionStrategy()

    data = [78,82,91]

    result = strategy.process(data)

    assert result != data