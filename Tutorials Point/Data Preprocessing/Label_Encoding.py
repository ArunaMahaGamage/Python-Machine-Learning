from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
input_classes = ['suzuki', 'ford', 'suzuki', 'toyota', 'ford', 'bmw']
label_encoder.fit(input_classes)
print ("\nClass mapping:")
for i, item in enumerate(label_encoder.classes_):
	print (item, '-->', i)


#As shown in above output, the words have been changed into 0-indexed numbers. Now,
#when we deal with a set of labels, we can transform them as follows:


labels = ['toyota', 'ford', 'suzuki','bmw']
encoded_labels = label_encoder.transform(labels)
print ("\nLabels =", labels)
print ("Encoded labels =", list(encoded_labels))

#This is efficient than manually maintaining mapping between words and numbers. You can
#check by transforming numbers back to word labels as shown in the code here:


encoded_labels = [3, 2, 0, 2, 1]
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print ("\nEncoded labels =", encoded_labels)
print ("Decoded labels =", list(decoded_labels))
