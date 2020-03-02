from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Embedding, Bidirectional, GRU, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.regularizers import l2, l1, l1_l2


def NaiveModel(vocab_size):  # 70% accuracy
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
        Bidirectional(GRU(64, return_sequences=True, dropout=0.5, recurrent_dropout=0.5)),
        Bidirectional(GRU(64,return_sequences=True, dropout=0.5, recurrent_dropout=0.5)),
        BatchNormalization(),
        Dense(64, activation='relu',kernel_regularizer=l1_l2()),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    return model


def WideandDeep(vocab_size):
    pass
