class EncryptionStrategy:

    def process(self, data):
        return [value ^ 0x4F for value in data]


class CompressionStrategy:

    def process(self, data):
        return [round(value * 0.85, 2) for value in data]