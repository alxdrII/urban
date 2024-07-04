class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs          # число входов в слой
        self.outputs = outputs        # число выходов слоя (целые числа)
        self.activation = activation  # функция активации (строка, например: 'linear', 'relu', 'sigmoid')
        self.name = "Dense"


class NetworkIterator:
