import requests

def Validate_NPI (npi_number,first_name,last_name,state):

    #example doctor: 1851510887 John AAGESEN IA
    
    #Search NPI registry on conditions <<npi_number,first_name,last_name,state>>
    url = f'https://npiregistry.cms.hhs.gov/api/?version=2.1&number={npi_number}&first_name={first_name}&last_name={last_name}&state={state}'

    #format the response
    response = requests.get(url)
    response = response.json()

    #returns Valid if person found in registry, returns Error if no one in registry of that detail
    if 'Errors' in response:
        return('Error')
    else:
        return('Valid')



Validate_NPI ('1851510887','JOHN','AAGESEN','IA')
