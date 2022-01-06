import pickle
import csv
vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
model = pickle.load(open('model.sav','rb'))
testString = ["Back at it with @FanalystSteph  HUHE WIN. BIG predictions. It's all here on LLN. \nLeafsForever \nAppleapplepodcasts"]

out = vectorizer.transform(testString)
pred = model.predict(out)
data = []
with open('processed.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:        
        data.append(row[0])   


vector_data = vectorizer.transform(data)
preds =  model.predict(vector_data)
print(preds)

print(round(sum(preds)/len(preds)))