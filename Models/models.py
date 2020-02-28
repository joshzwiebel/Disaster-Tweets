from tensorflow.keras.layers import Embedding, Bidirectional, GRU, Dense
from tensorflow.keras.models import Sequential


def NaiveModel(vocab_size):
    model = Sequential([
        Embedding(vocab_size, 64),
        Bidirectional(GRU(64, return_sequences=True)),
        Bidirectional(GRU(64, return_sequences=True)),
        Bidirectional(GRU(64, return_sequences=True)),
        Bidirectional(GRU(64, return_sequences=True)),
        Bidirectional(GRU(64)),
        Dense(128, activation='tanh'),
        Dense(1, activation='sigmoid')
    ])
    return model
