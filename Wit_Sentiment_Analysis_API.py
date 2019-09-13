import pandas as pd
from wit import Wit
import threading
import multiprocessing
import json
import time
from wit_credential import access_token

access_token='TPGKFHFWL6UWQ2MNBTX7LBVKZP4FNYWN'

client = Wit(access_token)

tweets = pd.read_csv('three_com_for_fb.txt',index_col = 0, header = None)[1]
senti_input = tweets
alist = list(senti_input.index)
blist = list(senti_input)

f = open("Three_com_sentiment_analysis_wit_output.txt", "w")
count = 0
print("processed %d" % count)

while True:
    try:
        for a,b in zip(alist,blist):
            response = client.message(b)

            count += 1
            if count % 10 == 0:
                print("processed %d" % count)
            f.write(json.dumps(response))
            f.write('\n')
            f.flush()
            
    except Exception as e:
        print(e)
        time.sleep(30)