from tensorflow.keras.layers import Embedding, Bidirectional, GRU, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import PReLU, ELU, BatchNormalization


def NaiveModel(vocab_size): #70% accuracy
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
def NaiveIteration(vocab_size):
    model = Sequential([
        Embedding(vocab_size, 64),
        Bidirectional(GRU(64, return_sequences=True,dropout=0.35)),
        Bidirectional(GRU(64, return_sequences=True,dropout=0.25)),
        Bidirectional(GRU(64)),
        BatchNormalization(),
        Dense(128, activation=PReLU),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
def WideandDeep(vocab_size):
    pass


