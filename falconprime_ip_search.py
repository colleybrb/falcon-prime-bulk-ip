from falconpy import Intel
import json
import pandas as pd
from tqdm import tqdm
import getpass
#from argparse import ArgumentParser, RawTextHelpFormatter
CLIENT_ID = getpass.getpass('What is your client-id')
CLIENT_SECRET = getpass.getpass('What is your secret')
CLIENT_BASE = getpass.getpass('What is your base url')
#Q=input('What is your query IP')



def get_ip(ip, CLIENT_ID, CLIENT_SECRET, CLIENT_BASE):
    falcon = Intel(client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET, base_url=CLIENT_BASE)

    response = falcon.QueryIntelIndicatorEntities(offset=0,
                                                limit=5000,
                                                filter=f"id:*'ip_address_{ip}'",

                                                include_deleted=False,
                                                include_relations=True
                                                )
    #CNT = len(response["body"]["resources"])
    data = response["body"]["resources"]

    desired_indicators = []
    SHOW_JSON = True
    for intel_ind in data:
        indicator = str(intel_ind['indicator'])
        if indicator.startswith('51.116'):
            desired_indicators.append(intel_ind)

    if SHOW_JSON:
        # Serializing json
        json_object = json.dumps(response["body"]["resources"], indent=4)
        print(json_object)
        return(json_object)
IP_DF = pd.read_csv (r'C:\Users\user\Downloads\IP_LIST_BULK_SEARCH.csv',skip_blank_lines=True) 
for index,row in tqdm(IP_DF.iterrows()):
    ip = row['IP']
    data=get_ip(ip, CLIENT_ID, CLIENT_SECRET, CLIENT_BASE)
    IP_DF.at[index,'data'] = data
IP_DF.to_csv(r"C:\Users\user\Downloads\IP_DF3.csv", encoding='utf-8', index=False)
#else:
   # print("resources returned: ", CNT)
    #if CNT > 0:
     #   for x in range(CNT):
      #      print(response["body"]["resources"][x]['indicator'])
       #     print('malware_families: ',
        #          response["body"]["resources"][x]['malware_families'])
         #   print('Actors: ', response["body"]["resources"][x]['actors'])
          #  print('reports: ', response["body"]["resources"][x]['reports'])
           # print('malicious_confidence: ',
            #      response["body"]["resources"][x]['malicious_confidence'])
            #print('-----')