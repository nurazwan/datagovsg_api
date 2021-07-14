# Author: Nurazwan Hasan
# Date created: 10 July 2021
# Date modified: 14 July 2021
# Description: This script is design to call API to retrive all data in https://data.gov.sg


def dataframe_builder(resource_id):
    ''' This function will create a pandas dataframe.
    Parameter: resource_id in parenthesis'''
    import requests
    import pandas as pd
    init_url= 'https://data.gov.sg/api/action/datastore_search?resource_id=' + resource_id + '&limit=1'
    init_request=requests.get(init_url)
    init_request=init_request.json()
    init_request_count = init_request['result']['total']
    url = 'https://data.gov.sg/api/action/datastore_search?resource_id=' + resource_id + str('&limit=') +str(init_request_count)
    data_req= requests.get(url)
    data = data_req.json()['result']['records']
    dataframe = pd.DataFrame(data)
    dataframe = dataframe.set_index('_id')
    return dataframe
