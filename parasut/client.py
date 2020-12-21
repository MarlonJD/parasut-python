from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import LegacyApplicationClient, TokenExpiredError
import json
from . import functions
from . import urls


class Client(object):
    """Documentation for Client
    """
    def __init__(self, **kwargs):
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.token = None
        self.request = None
        self.companyId = None

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
        token = self.request.fetch_token(
            token_url='https://api.parasut.com/oauth/token',
            username=self.username,
            password=self.password,
            client_id=self.client_id,
            client_secret=self.client_secret)
        self.saveToken(token)

    def refreshToken(self, token):
        update_token = self.request.refresh_token(
            token_url='https://api.parasut.com/oauth/token',
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
                    headers={
                        'Content-Type': 'application/json'},
                    data=json.dumps(data))
            except TokenExpiredError:
                self.refreshToken()
                return self.request.post(
                    url=url,
                    headers={
                        'Content-Type': 'application/json'},
                    data=json.dumps(data))
        if method == 'PUT':
            try:
                return self.request.put(
                    url=url,
                    headers={
                        'Content-Type': 'application/json'},
                    data=json.dumps(data))
            except TokenExpiredError:
                self.refreshToken()
                return self.request.put(
                    url=url,
                    headers={
                        'Content-Type': 'application/json'},
                    data=json.dumps(data))
        if method == 'DELETE':
            try:
                return self.request.delete(
                    url=url,
                    headers={
                        'Content-Type': 'application/json'},
                    data=json.dumps(data))
            except TokenExpiredError:
                self.refreshToken()
                return self.request.delete(
                    url=url,
                    headers={
                        'Content-Type': 'application/json'},
                    data=json.dumps(data))
        if method == 'PATCH':
            try:
                return self.request.patch(
                    url=url,
                    headers={
                        'Content-Type': 'application/json'},
                    data=json.dumps(data))
            except TokenExpiredError:
                self.refreshToken()
                return self.request.patch(
                    url=url,
                    headers={
                        'Content-Type': 'application/json'},
                    data=json.dumps(data))

    def response(self, obj):
        return obj.json()

    def getCompanyId(self):
        try:
            r = self.request.get(url=urls.ME_URL)
        except TokenExpiredError:
            self.refreshToken()
            self.request.get(url=urls.ME_URL)
        res = json.loads(json.dumps(r.json()))
        cid = None
        for v in res['included']:
            if v['type'] == 'companies':
                cid = v['id']

        if cid:
            self.companyId = cid

    def createContact(self, data):
        if not self.request:
            self.authorize()

        if not self.token:
            self.getToken()

        if not self.companyId:
            self.getCompanyId()

        return functions.createContact(self.makeRequest, self.companyId, data)
