from . import urls


class Functions(object):
    """Functions for API Endpoints

    """
    def __init__(self, **kwargs):
        self.company_id = kwargs.get('company_id')
        if 'base_url' in kwargs:
            self.baseUrl = kwargs.get('base_url')
        else:
            self.baseUrl = None
        if 'company_id' not in kwargs:
            raise TypeError("You must provide company_id")
        super(Functions, self).__init__()

    def replaceUrl(self, url):
        url_obj = url.replace(':company_id', self.company_id)
        if self.baseUrl:
            url_obj = url_obj(urls.BASE_URL, self.baseUrl)
        return url_obj

    # Sales
    def createContact(self, makeRequest, company_id, data):
        '''Sales: Contacts: Create via POST
        '''
        url = self.replaceUrl(urls.CONTACTS_URL)
        return makeRequest(url, 'POST', data)
