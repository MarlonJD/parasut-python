from . import urls


# Sales
def createContact(makeRequest, company_id, data):
    '''Sales: Contacts: Create via POST
    '''
    url = urls.CONTACTS_URL.replace(':company_id', company_id)
    print(url)
    return makeRequest(url, 'POST', data)
