import pandas as pd
import tensorflow as tf
import torch
from transformers import BertTokenizer, BertModel

# Load the dataset
df = pd.read_csv("instrumentation_issues.csv")

# Preprocess the data
# Split the descriptions into words and encode them as integers
tokenizer = tf.keras.preprocessing.text.Tokenizer(oov_token='<OOV>', lower=False, split=' ')
tokenizer.fit_on_texts(df['description'])
sequences = tokenizer.texts_to_sequences(df['description'])
padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, padding='post')

# Load the BERT model
model = tf.keras.models.load_model('C:/Users/shahidan.idris/tensorflow_datasets/bert-base-uncased/tf_model.h5')

# Predict the labels for each description
predictions = model.predict(padded_sequences)

# Extract the predicted labels
predicted_labels = [tokenizer.index_word[prediction.argmax()] for prediction in predictions]

# Add the predicted labels as a new column in the dataset
df['predicted_label'] = predicted_labels

# Save the labeled dataset to a CSV file
df.to_csv("labeled_instrumentation_issues.csv", index=False)


# # Preprocess the data
# # Split the descriptions into words and encode them as integers
# tokenizer = BertTokenizer.from_pretrained("C:/Users/shahidan.idris/tensorflow_datasets/bert-base-uncased")
# input_ids = tokenizer.batch_encode_plus(df['description'], return_tensors='pt', pad_to_max_length=True)['input_ids']

# # Load the BERT model
# model = BertModel.from_pretrained("C:/Users/shahidan.idris/tensorflow_datasets/bert-base-uncased")

# print(type(model))

# # Predict the labels for each description
# predictions = model.predict(input_ids)

# # Extract the predicted labels
# predicted_labels = [tokenizer.convert_ids_to_tokens(prediction.argmax(axis=2)) for prediction in predictions]

# # Add the predicted labels as a new column in the dataset
# df['predicted_label'] = predicted_labels

# # Save the labeled dataset to a CSV file
# df.to_csv("labeled_instrumentation_issues.csv", index=False)