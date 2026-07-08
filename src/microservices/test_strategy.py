from src.microservices.strategy import EncryptionStrategy
from src.microservices.strategy import CompressionStrategy

data_stream = [78,82,91,65,40,99,88]

encrypt = EncryptionStrategy()
compress = CompressionStrategy()

print(encrypt.process(data_stream))
print(compress.process(data_stream))