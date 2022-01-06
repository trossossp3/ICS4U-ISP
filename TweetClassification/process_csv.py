import csv
import re

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


with open('cat.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
s1 = data[6][0]
print(s1)
print('*'*80)
for i in range(len(data)):
    data[i][0] = re.sub(r'http\S+', '', data[i][0])
    data[i][0] = re.sub('#', '', data[i][0])
    data[i][0] = remove_emoji(data[i][0])
    data[i][0] = re.sub('\n', ' ', data[i][0])
    # print(data[i][0])
print(data)
def write_to_csv(out, data):

    csvFile = open(out, "w", newline=None, encoding='utf-8')
    csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_NONE, escapechar=' ')
    for tweet in data:
              
        csvWriter.writerow(tweet)
        # csvWriter.writerow(["*"*100])
    csvFile.close()

write_to_csv('processed.csv', data)
