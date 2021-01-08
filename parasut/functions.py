from . import urls


class Functions(object):
    """Functions for API Endpoints

    """
    def __init__(self, **kwargs):
        if 'base_url' in kwargs:
            self.baseUrl = kwargs.get('base_url')
        else:
            self.baseUrl = None
        if 'company_id' not in kwargs:
            raise TypeError("You must provide company_id")
        else:
            self.company_id = kwargs.get('company_id')
        if 'make_request' not in kwargs:
            raise TypeError("You must provide maka_request function)")
        else:
            self.makeRequest = kwargs.get('make_request')
        super(Functions, self).__init__()

    def replaceUrl(self, url):
        url_obj = url.replace(':company_id', self.company_id)
        if self.baseUrl:
            url_obj = url_obj.replace(urls.BASE_URL, self.baseUrl)
        return url_obj

    def indexGeneral(self, uri):
        url = self.replaceUrl(uri)
        return self.makeRequest(url, 'GET')

    def createGeneral(self, uri, data):
        url = self.replaceUrl(uri)
        return self.makeRequest(url, 'POST', data)

    def showGeneral(self, uri, pk):
        url = self.replaceUrl(uri + '/' + pk)
        return self.makeRequest(url, 'GET')

    def editGeneral(self, uri, data, pk):
        url = self.replaceUrl(uri + '/' + pk)
        return self.makeRequest(url, 'PUT', data)

    def deleteGeneral(self, uri, pk):
        url = self.replaceUrl(uri + '/' + pk)
        return self.makeRequest(url, 'DELETE')

    def cancelGeneral(self, uri, pk):
        url = self.replaceUrl(uri + '/' + pk + '/cancel')
        return self.makeRequest(url, 'DELETE')

    def recoverGeneral(self, uri, pk):
        url = self.replaceUrl(uri + '/' + pk + '/recover')
        return self.makeRequest(url, 'PATCH')

    def archiveGeneral(self, uri, pk):
        url = self.replaceUrl(uri + '/' + pk + '/archive')
        return self.makeRequest(url, 'PATCH')

    def unarchiveGeneral(self, uri, pk):
        url = self.replaceUrl(uri + '/' + pk +
                              '/unarchive')
        return self.makeRequest(url, 'PATCH')

    """### Sales ###"""

    # Sales: Invoices
    def indexInvoice(self):
        """Sales: Invoices Index via GET
        """
        return self.indexGeneral(urls.SALES_INVOICES_URL)

    def createInvoice(self, data):
        """Sales: Invoices Create via POST
        """
        return self.createGeneral(urls.SALES_INVOICES_URL, data)

    def showInvoice(self, pk):
        """Sales: Invoices Show via GET
        """
        return self.showGeneral(urls.SALES_INVOICES_URL, pk)

    def editInvoice(self, data, pk):
        """Sales: Invoices Edit via PUT
        """
        return self.editGeneral(urls.SALES_INVOICES_URL, data, pk)

    def deleteInvoice(self, pk):
        """Sales: Invoices Delete via DELETE
        """
        return self.deleteGeneral(urls.SALES_INVOICES_URL, pk)

    def payInvoice(self, data, pk):
        """Sales: Invoices Pay via POST
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk + '/payments')
        return self.makeRequest(url, 'POST', data)

    def cancelInvoice(self, pk):
        """Sales: Invoices Cancel via DELETE
        """
        return self.cancelGeneral(urls.SALES_INVOICES_URL, pk)

    def recoverInvoice(self, pk):
        """Sales: Invoices Recover via PATCH
        """
        return self.recoverGeneral(urls.SALES_INVOICES_URL, pk)

    def archiveInvoice(self, pk):
        """Sales: Invoices Archive via PATCH
        """
        return self.archiveGeneral(urls.SALES_INVOICES_URL, pk)

    def unarchiveInvoice(self, pk):
        """Sales: Invoices Unarchive via PATCH
        """
        return self.unarchiveGeneral(urls.SALES_INVOICES_URL, pk)

    def convertEstimateInvoice(self, data, pk):
        """Sales: Invoices Recover via PATCH
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk +
                              '/corvert_to_invoice')
        return self.makeRequest(url, 'PATCH', data)

    # Sales: Contacts (or Expenses Contacts)
    def indexContact(self):
        """Sales: Contacts List via GET
        """
        return self.indexGeneral(urls.CONTACTS_URL)

    def createContact(self, data):
        """Sales: Contacts Create via POST
        """
        return self.createGeneral(urls.CONTACTS_URL, data)

    def showContact(self, pk):
        """Sales: Contacts Show via GET
        """
        return self.showGeneral(urls.CONTACTS_URL, pk)

    def editContact(self, data, pk):
        """Sales: Contacts Edit via POST
        """
        return self.editGeneral(urls.CONTACTS_URL, data, pk)

    def deleteContact(self, pk):
        """Sales: Contacts Delete via DELETE
        """
        return self.deleteGeneral(urls.CONTACTS_URL, pk)

    def transactionsContact(self, data, pk):
        """Sales: Contacts Debit Transactions via POST
        """
        url = self.replaceUrl(urls.CONTACTS_URL + '/' + pk +
                              '/contact_debit_transactions')
        return self.makeRequest(url, 'POST', data)

    def payContact(self, data, pk):
        """Sales: Contacts Debit Transactions via POST
        """
        url = self.replaceUrl(urls.CONTACTS_URL + '/' + pk +
                              '/contact_credit_transactions')
        return self.makeRequest(url, 'POST', data)

    """### Expenses ###"""

    # Expenses: Bills
    def indexBill(self):
        """Expenses: Purchase Bills Index via GET
        """
        return self.indexGeneral(urls.PURCHASE_BILLS_URL)

    def createBasicBill(self, data):
        """Expenses: Purchase Bills Create Basic via POST
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '#basic')
        return self.makeRequest(url, 'POST', data)

    def createDetailedBill(self, data):
        """Expenses: Purchase Bills Create Detailed via POST
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '#detailed')
        return self.makeRequest(url, 'POST', data)

    def showBill(self, pk):
        """Expenses: Purchase Bills Show via GET
        """
        return self.showGeneral(urls.PURCHASE_BILLS_URL, pk)

    def deleteBill(self, pk):
        """Expenses: Purchase Bills DELETE via DELETE
        """
        return self.deleteGeneral(urls.PURCHASE_BILLS_URL, pk)

    def editBasicBill(self, data, pk):
        """Expenses: Purchase Bills Edit Basic via PUT
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '#basic')
        return self.makeRequest(url, 'PUT', data)

    def editDetailedBill(self, data, pk):
        """Expenses: Purchase Bills Edit Detailed via PUT
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '#detailed')
        return self.makeRequest(url, 'PUT', data)

    def payBill(self, data, pk):
        """Expenses: Purchase Bills Pay via POST
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '/payments')
        return self.makeRequest(url, 'POST', data)

    def cancelBill(self, pk):
        """Expenses: Purchase Bills Cancel via DELETE
        """
        return self.cancelGeneral(urls.PURCHASE_BILLS_URL, pk)

    def recoverBill(self, pk):
        """Expenses: Purchase Bills Recover via PATCH
        """
        return self.recoverGeneral(urls.PURCHASE_BILLS_URL, pk)

    def archiveBill(self, pk):
        """Expenses: Purchase Bills Archive via PATCH
        """
        return self.archiveGeneral(urls.PURCHASE_BILLS_URL, pk)

    def unarchiveBill(self, pk):
        """Expenses: Purchase Bills Unarchive via PATCH
        """
        return self.unarchiveGeneral(urls.PURCHASE_BILLS_URL, pk)

    # Expenses: Bank Fees
    def createBankFee(self, data):
        """Expenses: Bank Fees Create via POST
        """
        return self.createGeneral(urls.BANK_FEES_URL, data)

    def showBankFee(self, pk):
        """Expenses: Bank Fees Show via GET
        """
        return self.showGeneral(urls.BANK_FEES_URL, pk)

    def editBankFee(self, data, pk):
        """Expenses: Bank Fees Edit via PUT
        """
        return self.editGeneral(urls.BANK_FEES_URL, data, pk)

    def deleteBankFee(self, pk):
        """Expenses: Bank Fees Delete via DELETE
        """
        return self.deleteGeneral(urls.BANK_FEES_URL, pk)

    def archiveBankFee(self, pk):
        """Expenses: Bank Fees Archive via PATCH
        """
        return self.archiveGeneral(urls.BANK_FEES_URL, pk)

    def unarchiveBankFee(self, pk):
        """Expenses: Bank Fees Unarchive via PATCH
        """
        return self.unarchiveGeneral(urls.BANK_FEES_URL, pk)

    def payBankFee(self, data, pk):
        """Expenses: Bank Fees Pay via POST
        """
        url = self.replaceUrl(urls.BANK_FEES_URL + '/' + pk + '/payments')
        return self.makeRequest(url, 'POST', data)

    # Expenses: Salaries
    def indexSalary(self):
        """Expenses: Salaries Index via GET
        """
        return self.indexGeneral(urls.SALARIES_URL)

    def createSalary(self, data):
        """Expenses: Salaries Create via POST
        """
        return self.createGeneral(urls.SALARIES_URL, data)

    def showSalary(self, pk):
        """Expenses: Salaries Show via GET
        """
        return self.showGeneral(urls.SALARIES_URL, pk)

    def editSalary(self, data, pk):
        """Expenses: Salaries Edit via PUT
        """
        return self.editGeneral(urls.SALARIES_URL, data, pk)

    def deleteSalary(self, pk):
        """Expenses: Salaries Delete via DELETE
        """
        return self.deleteGeneral(urls.SALARIES_URL, pk)

    def archiveSalary(self, pk):
        """Expenses: Salaries Archive via PATCH
        """
        return self.archiveGeneral(urls.SALARIES_URL, pk)

    def unarchiveSalary(self, pk):
        """Expenses: Salaries unarchive via PATCH
        """
        return self.unarchiveGeneral(urls.SALARIES_URL, pk)

    def paySalary(self, data, pk):
        """Expenses: Salaries Pay via POST
        """
        url = self.replaceUrl(urls.SALARIES_URL + '/' + pk + '/payments')
        return self.makeRequest(url, 'POST', data)

    # Expenses: Taxes
    def indexTax(self):
        """Expenses: Taxes Index via GET
        """
        return self.indexGeneral(urls.TAXES_URL)

    def createTax(self, data):
        """Expenses: Taxes Create via POST
        """
        return self.createGeneral(urls.TAXES_URL, data)

    def showTax(self, pk):
        """Expenses: Taxes Show via GET
        """
        return self.showGeneral(urls.TAXES_URL, pk)

    def editTax(self, data, pk):
        """Expenses: Taxes Edit via PUT
        """
        return self.editGeneral(urls.TAXES_URL, data, pk)

    def deleteTax(self, pk):
        """Expenses: Taxes Delete via DELETE
        """
        return self.deleteGeneral(urls.TAXES_URL, pk)

    def archiveTax(self, pk):
        """Expenses: Taxes Archive via PATCH
        """
        return self.archiveGeneral(urls.TAXES_URL, pk)

    def unarchiveTax(self, pk):
        """Expenses: Taxes unarchive via PATCH
        """
        return self.unarchiveGeneral(urls.TAXES_URL, pk)

    def payTax(self, data, pk):
        """Expenses: Taxes Pay via POST
        """
        url = self.replaceUrl(urls.TAXES_URL + '/' + pk + '/payments')
        return self.makeRequest(url, 'POST', data)

    # Expenses: Employees
    def indexEmployee(self):
        """Expenses: Employees Index via GET
        """
        return self.indexGeneral(urls.EMPLOYEES_URL)

    def createEmployee(self, data):
        """Expenses: TaxesEmployees Create via POST
        """
        return self.createGeneral(urls.EMPLOYEES_URL, data)

    def showEmployee(self, pk):
        """Expenses: Employees Show via GET
        """
        return self.showGeneral(urls.EMPLOYEES_URL, pk)

    def editEmployee(self, data, pk):
        """Expenses: Employees Edit via PUT
        """
        return self.editGeneral(urls.EMPLOYEES_URL, data, pk)

    def deleteEmployee(self, pk):
        """Expenses: Employees Delete via DELETE
        """
        return self.deleteGeneral(urls.EMPLOYEES_URL, pk)

    def archiveEmployee(self, pk):
        """Expenses: Employees Archive via PATCH
        """
        return self.archiveGeneral(urls.EMPLOYEES_URL, pk)

    def unarchiveEmployee(self, pk):
        """Expenses: Employees unarchive via PATCH
        """
        return self.unarchiveGeneral(urls.EMPLOYEES_URL, pk)

    """### Legalize ###"""

    # Legalize: E-Invoice Inboxes
    def indexEInvoiceInbox(self, vkn):
        """Legelize: E-Invoice Inboxes Index via GET
        """
        url = self.replaceUrl(urls.E_INVOICE_INBOX_URL + "?filter[vkn]=" + vkn)
        return self.makeRequest(url, 'GET')

    # Legalize: E-Archives
    def createEArchive(self, data):
        """Legalize: E-Arhives Create via POST
        """
        return self.createGeneral(urls.E_ARCHIVES_URL, data)

    def showEArchive(self, pk):
        """Legalize: E-Arhives Show via GET
        """
        return self.showGeneral(urls.E_ARCHIVES_URL, pk)

    def showEArchivePDF(self, data, pk):
        """Legalize: E-Arhives Show PDF via GET
        """
        url = self.replaceUrl(urls.E_ARCHIVES_URL + '/' + pk + '/pdf')
        return self.makeRequest(url, 'GET', data)

    # Legalize: E-Invoices
    def createEInvoice(self, data):
        """Legalize: E-Invoices Create via POST
        """
        return self.createGeneral(urls.E_INVOICE_URL, data)

    def showEInvoice(self, pk):
        """Legalize: E-Invoices Show via GET
        """
        return self.showGeneral(urls.E_INVOICE_URL, pk)

    def showEInvoicePDF(self, pk):
        """Legalize: E-Invoices Show PDF via GET
        """
        url = self.replaceUrl(urls.E_INVOICE_URL + '/' + pk + '/pdf')
        return self.makeRequest(url, 'GET')

    # Legalize: E-SMM
    def createEsmm(self, data):
        """Legalize: E-SMM Create via POST
        """
        return self.createGeneral(urls.E_SMMS_URL, data)

    def showEsmm(self, pk):
        """Legalize: E-SMM Show via GET
        """
        return self.showGeneral(urls.E_SMMS_URL, pk)

    def showEsmmPDF(self, pk):
        """Legalize: E-SMM Show PDF via GET
        """
        url = self.replaceUrl(urls.E_SMMS_URL + '/' + pk + '/pdf')
        return self.makeRequest(url, 'GET')

    """### Cash ###"""

    # Cash: Accounts
    def indexAccount(self):
        """Cash: Accounts Index via GET
        """
        return self.indexGeneral(urls.ACCOUNTS_URL)

    def createAccount(self, data):
        """Cash: Accounts Create via POST
        """
        return self.createGeneral(urls.ACCOUNTS_URL, data)

    def showAccount(self, pk):
        """Cash: Accounts Show via GET
        """
        return self.showGeneral(urls.ACCOUNTS_URL, pk)

    def editAccount(self, data, pk):
        """Cash: Accounts Edit via PUT
        """
        return self.editGeneral(urls.ACCOUNTS_URL, data, pk)

    def deleteAccount(self, pk):
        """Cash: Accounts Delete via DELETE
        """
        return self.deleteGeneral(urls.ACCOUNTS_URL, pk)

    def transactionsAccount(self, pk):
        """Cash: Accounts Transactions Get via GET
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk + '/transactions')
        return self.makeRequest(url, 'GET')

    def debitTransactionAccount(self, data, pk):
        """Cash: Accounts Debit Transaction via POST
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk +
                              '/debit_transactions')
        return self.makeRequest(url, 'POST', data)

    def creditTransactionAccount(self, data, pk):
        """Cash: Accounts Credit Transaction via POST
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk +
                              '/credit_transactions')
        return self.makeRequest(url, 'POST', data)

    # Cash: Transactions
    def showTransaction(self, pk):
        """Cash: Accounts Show via GET
        """
        return self.showGeneral(urls.ACCOUNTS_URL, pk)

    def deleteTransaction(self, pk):
        """Cash: Accounts Delete via DELETE
        """
        return self.deleteGeneral(urls.ACCOUNTS_URL, pk)

    """### Stock/Hoard ###"""

    # Stock: Products
    def indexProduct(self):
        """Stock: Products Index via GET
        """
        return self.indexGeneral(urls.PRODUCTS_URL)

    def createProduct(self, data):
        """Stock: Products Create via POST
        """
        return self.createGeneral(urls.PRODUCTS_URL, data)

    def showProduct(self, pk):
        """Stock: Products Show via GET
        """
        return self.showGeneral(urls.PRODUCTS_URL, pk)

    def editProduct(self, data, pk):
        """Stock: Products Edit via PUT
        """
        return self.editGeneral(urls.PRODUCTS_URL, data, pk)

    def deleteProduct(self, pk):
        """Stock: Products Delete via DELETE
        """
        return self.deleteGeneral(urls.PRODUCTS_URL, pk)

    # Stock: Shipment Documents
    def indexShipmentDocument(self):
        """Stock: Shipment Documents Index via GET
        """
        return self.indexGeneral(urls.SHIPMENT_DOCUMENTS_URL)

    def createShipmentDocument(self, data):
        """Stock: Shipment Documents Create via POST
        """
        return self.createGeneral(urls.SHIPMENT_DOCUMENTS_URL, data)

    def showShipmentDocument(self, pk):
        """Stock: Shipment Documents Show via GET
        """
        return self.showGeneral(urls.SHIPMENT_DOCUMENTS_URL, pk)

    def editShipmentDocument(self, data, pk):
        """Stock: Shipment Documents Edit via PUT
        """
        return self.editGeneral(urls.SHIPMENT_DOCUMENTS_URL, data, pk)

    def deleteShipmentDocument(self, pk):
        """Stock: Shipment Documents Delete via DELETE
        """
        return self.deleteGeneral(urls.SHIPMENT_DOCUMENTS_URL, pk)

    # Stocks: Stock Movements
    def indexStockMovement(self):
        """Stock: Stock Movements Index via GET
        """
        return self.indexGeneral(urls.STOCK_MOVEMENTS_URL)

    """### Settings ###"""

    # Settings: Item Categories
    def indexItemCategory(self):
        """Settings: Item Categories Index via GET
        """
        return self.indexGeneral(urls.CATEGORIES_URL)

    def createItemCategory(self, data):
        """Settings: Item Categories Create via POST
        """
        return self.createGeneral(urls.CATEGORIES_URL, data)

    def showItemCategory(self, pk):
        """Settings: Item Categories Show via GET
        """
        return self.showGeneral(urls.CATEGORIES_URL, pk)

    def editItemCategory(self, data, pk):
        """Settings: Item Categories Edit via PUT
        """
        return self.editGeneral(urls.CATEGORIES_URL, data, pk)

    def deleteItemCategory(self, pk):
        """Settings: Item Categories Delete via DELETE
        """
        return self.deleteGeneral(urls.CATEGORIES_URL, pk)

    # Settings: Tags
    def indexTag(self):
        """Settings: Tags Index via GET
        """
        return self.indexGeneral(urls.TAGS_URL)

    def createTag(self, data):
        """Settings: Tags Create via POST
        """
        return self.createGeneral(urls.TAGS_URL, data)

    def showTag(self, pk):
        """Settings: Tags Show via GET
        """
        return self.showGeneral(urls.TAGS_URL, pk)

    def editTag(self, data, pk):
        """Settings: Tags Edit via PUT
        """
        return self.editGeneral(urls.TAGS_URL, data, pk)

    def deleteTag(self, pk):
        """Settings: Tags Delete via DELETE
        """
        return self.deleteGeneral(urls.TAGS_URL, pk)

    """### Other ###"""

    # Other: API Home
    def showAPIHome(self, pk):
        """Other: API Home via GET
        """
        return self.showGeneral(urls.ME_URL)

    # Other: Tackable Job
    def showTrackableJob(self, pk):
        """Other: Tackable Job Show via GET
        """
        return self.showGeneral(urls.TRACKABLE_JOB, pk)

    def activeEDocument(self, pk):
        """Other: Activate E-Document via GET
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk + "/?include=active_e_document")
        return self.makeRequest(url, 'GET')

    
