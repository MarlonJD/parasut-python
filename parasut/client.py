from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import LegacyApplicationClient, TokenExpiredError
import json
from .functions import Functions
from . import urls
# from functools import wraps


class Client(object):
    """Documentation for Client
    """
    def __init__(self, **kwargs):
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')

        # Sandbox var if production or test
        self.sandbox = False
        if 'sandbox' in kwargs:
            self.sandbox = kwargs.get('sandbox')
        else:
            self.sandbox = False

        # BaseUrl settings for custom url
        self.baseUrl = None
        if 'base_url' in kwargs:
            self.baseUrl = kwargs.get('base_url')
        else:
            if self.sandbox:
                self.baseUrl = urls.SANDBOX_BASE_URL

        # TokenUrl settings if custom url
        self.tokenUrl = None
        if 'token_url' in kwargs:
            self.tokenUrl = kwargs.get('token_url')
        else:
            if self.tokenUrl:
                self.tokenUrl = urls.SANDBOX_TOKEN_URL

        self.token = None
        self.request = None
        self.companyId = None
        self.functions = None

        if 'client_id' not in kwargs:
            raise TypeError("You must provide client_id")

        if 'client_secret' not in kwargs:
            raise TypeError("You must provide client_secret")

        if 'username' not in kwargs:
            raise TypeError("You must provide username")

        if 'password' not in kwargs:
            raise TypeError("You must provide password")
        super(Client, self).__init__()

    def saveToken(self, new_token):
        self.token = new_token

    def authorize(self):
        oauth = OAuth2Session(client=LegacyApplicationClient(
            client_id=self.client_id))

        self.request = oauth

    def getToken(self):
        if not self.request:
            self.authorize()

        if self.tokenUrl:
            tokenUrl = self.tokenUrl
        else:
            if self.sandbox:
                tokenUrl = urls.SANDBOX_TOKEN_URL
            else:
                tokenUrl = urls.TOKEN_URL
        token = self.request.fetch_token(token_url=tokenUrl,
                                         username=self.username,
                                         password=self.password,
                                         client_id=self.client_id,
                                         client_secret=self.client_secret)
        self.saveToken(token)

    def refreshToken(self, token):
        if self.tokenUrl:
            tokenUrl = self.tokenUrl
        else:
            if self.sandbox:
                tokenUrl = urls.SANDBOX_TOKEN_URL
            else:
                tokenUrl = urls.TOKEN_URL
        update_token = self.request.refresh_token(
            token_url=tokenUrl,
            refresh_token=self.token.get('refresh_token'),
            client_id=self.client_id,
            client_secret=self.client_secret)
        self.token.update(update_token)

    def makeRequest(self, url, method, data=None):
        if not self.request:
            self.authorize()

        if not self.token:
            self.getToken()

        if method == 'GET':
            try:
                r = self.request.get(url=url)
            except TokenExpiredError:
                self.refreshToken()
                self.request.get(url=url)
            return r
        if method == 'POST':
            try:
                return self.request.post(
                    url=url,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(data))
            except TokenExpiredError:
                self.refreshToken()
                return self.request.post(
                    url=url,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(data))
        if method == 'PUT':
            try:
                return self.request.put(
                    url=url,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(data))
            except TokenExpiredError:
                self.refreshToken()
                return self.request.put(
                    url=url,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(data))
        if method == 'DELETE':
            try:
                return self.request.delete(
                    url=url,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(data))
            except TokenExpiredError:
                self.refreshToken()
                return self.request.delete(
                    url=url,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(data))
        if method == 'PATCH':
            try:
                return self.request.patch(
                    url=url,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(data))
            except TokenExpiredError:
                self.refreshToken()
                return self.request.patch(
                    url=url,
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(data))

    def response(self, obj):
        return obj.json()

    def getCompanyId(self):
        if not self.request:
            self.authorize()

        if not self.token:
            self.getToken()

        try:
            if self.sandbox:
                url = urls.SANDBOX_ME_URL
            else:
                url = urls.ME_URL
            r = self.request.get(url=url)
        except TokenExpiredError:
            self.refreshToken()
            if self.sandbox:
                url = urls.SANDBOX_ME_URL
            else:
                url = urls.ME_URL
            r = self.request.get(url=url)
        res = json.loads(json.dumps(r.json()))
        cid = None

        try:
            if res['errors']:
                raise KeyError("Not found company_id in /me")
        except KeyError:
            for v in res['included']:
                if v['type'] == 'companies':
                    cid = v['id']

        if cid:
            self.companyId = cid

    def getFunctionsClass(self):
        self.functions = Functions(company_id=self.companyId,
                                   base_url=self.baseUrl,
                                   make_request=self.makeRequest)

    def initialize(self):
        if not self.request:
            self.authorize()

        if not self.token:
            self.getToken()

        if not self.companyId:
            self.getCompanyId()

        if not self.functions:
            self.getFunctionsClass()

    # def initializeDec(func):
    #     @wraps(func)
    #     def wrapper(self, *args):
    #         if not self.request:
    #             self.authorize()

    #         if not self.token:
    #             self.getToken()

    #         if not self.companyId:
    #             self.getCompanyId()

    #         if not self.functions:
    #             self.getFunctionsClass()
    #         return func(self, *args)
    #     return wrapper

    # """### Sales"""

    # # Sales: Invoices
    # @initializeDec
    # def indexInvoice(self):
    #     return self.functions.indexInvoice()

    # @initializeDec
    # def createInvoice(self, data):
    #     return self.functions.createInvoice(data)

    # @initializeDec
    # def showInvoice(self, pk):
    #     return self.functions.showInvoice(pk)

    # @initializeDec
    # def editInvoice(self, data, pk):
    #     return self.functions.editInvoice(data, pk)

    # @initializeDec
    # def deleteInvoice(self, pk):
    #     return self.functions.deleteInvoice(pk)

    # @initializeDec
    # def payInvoice(self, data, pk):
    #     return self.functions.payInvoice(data, pk)

    # @initializeDec
    # def cancelInvoice(self, pk):
    #     return self.functions.cancelInvoice(pk)

    # @initializeDec
    # def recoverInvoice(self, pk):
    #     return self.functions.recoverInvoice(pk)

    # @initializeDec
    # def arciveInvoice(self, pk):
    #     return self.functions.archiveInvoice(pk)

    # @initializeDec
    # def unarchiveInvoice(self, pk):
    #     return self.functions.unarchiveInvoice(pk)

    # @initializeDec
    # def covertEstimateInvoice(self, data):
    #     return self.functions.convertEstimateInvoice(data)

    # # Sales: Contacts (or Expenses Contacts)
    # @initializeDec
    # def indexContact(self):
    #     return self.functions.IndexContact()

    # @initializeDec
    # def createContact(self, data):
    #     return self.functions.createContact(data)

    # @initializeDec
    # def showContact(self, pk):
    #     """ Show Contact endpoint via GET
    #     Args:
    #         data: JSON Request data
    #         contact_id: id parameter of contact for url
    #     """
    #     return self.functions.showContact(pk)

    # @initializeDec
    # def editContact(self, data, pk):
    #     return self.functions.editContact(data, pk)

    # @initializeDec
    # def deleteContact(self, pk):
    #     return self.functions.deleteContact(pk)

    # @initializeDec
    # def transactionsContact(self, data, pk):
    #     return self.functions.transactionsContact(data, pk)

    # @initializeDec
    # def payContact(self, data, pk):
    #     return self.functions.payContact(data, pk)

    # """### Expenses"""

    # # Expenses: Bills
    # @initializeDec
    # def indexBill(self):
    #     return self.functions.indexBill()

    # @initializeDec
    # def createBasicBill(self, data):
    #     return self.functions.createBasicBill(data)

    # @initializeDec
    # def createDetailedBill(self, data):
    #     return self.functions.createDetailedBill(data)

    # @initializeDec
    # def showBill(self, pk):
    #     return self.functions.showBill(pk)
