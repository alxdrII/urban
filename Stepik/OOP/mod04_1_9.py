class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, layer):
        self.next_layer = layer
        return layer


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.name = 'Input'
        for i in range(inputs):
            self()


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        return self

    def __next__(self):
        pass