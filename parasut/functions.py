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

    """### Sales ###"""

    # Sales: Invoices
    def indexInvoice(self, makeRequest):
        """Sales: Invoices Index via GET
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL)
        return makeRequest(url, 'GET')

    def createInvoice(self, makeRequest, data):
        """Sales: Invoices Create via POST
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL)
        return makeRequest(url, 'POST', data)

    def showInvoice(self, makeRequest, pk):
        """Sales: Invoices Show via GET
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def editInvoice(self, makeRequest, data, pk):
        """Sales: Invoices Edit via PUT
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk)
        return makeRequest(url, 'PUT', data)

    def deleteInvoice(self, makeRequest, pk):
        """Sales: Invoices Delete via DELETE
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    def payInvoice(self, makeRequest, data, pk):
        """Sales: Invoices Pay via POST
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk + '/payments')
        return makeRequest(url, 'POST', data)

    def cancelInvoice(self, makeRequest, pk):
        """Sales: Invoices Cancel via DELETE
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk + '/cancel')
        return makeRequest(url, 'DELETE')

    def recoverInvoice(self, makeRequest, pk):
        """Sales: Invoices Recover via PATCH
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk + '/recover')
        return makeRequest(url, 'PATCH')

    def archiveInvoice(self, makeRequest, pk):
        """Sales: Invoices Archive via PATCH
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk + '/archive')
        return makeRequest(url, 'PATCH')

    def unarchiveInvoice(self, makeRequest, pk):
        """Sales: Invoices Unarchive via PATCH
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk +
                              '/unarchive')
        return makeRequest(url, 'PATCH')

    def convertEstimateInvoice(self, makeRequest, data, pk):
        """Sales: Invoices Recover via PATCH
        """
        url = self.replaceUrl(urls.SALES_INVOICES_URL + '/' + pk +
                              '/corvert_to_invoice')
        return makeRequest(url, 'PATCH', data)

    # Sales: Contacts (or Expenses Contacts)
    def indexContact(self, makeRequest):
        """Sales: Contacts List via GET
        """
        url = self.replaceUrl(urls.CONTACTS_URL)
        return makeRequest(url, 'GET')

    def createContact(self, makeRequest, data):
        """Sales: Contacts Create via POST
        """
        url = self.replaceUrl(urls.CONTACTS_URL)
        return makeRequest(url, 'POST', data)

    def showContact(self, makeRequest, pk):
        """Sales: Contacts Show via GET
        """
        url = self.replaceUrl(urls.CONTACTS_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def editContact(self, makeRequest, data, pk):
        """Sales: Contacts Edit via POST
        """
        url = self.replaceUrl(urls.CONTACTS_URL + '/' + pk)
        return makeRequest(url, 'PUT', data)

    def deleteContact(self, makeRequest, pk):
        """Sales: Contacts Delete via DELETE
        """
        url = self.replaceUrl(urls.CONTACTS_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    def transtactionsContact(self, makeRequest, data, pk):
        """Sales: Contacts Debit Transactions via POST
        """
        url = self.replaceUrl(urls.CONTACTS_URL + '/' + pk +
                              '/contact_debit_transactions')
        return makeRequest(url, 'POST', data)

    def payContact(self, makeRequest, data, pk):
        """Sales: Contacts Debit Transactions via POST
        """
        url = self.replaceUrl(urls.CONTACTS_URL + '/' + pk +
                              '/contact_credit_transactions')
        return makeRequest(url, 'POST', data)

    """### Expenses ###"""

    # Expenses: Bills
    def indexBill(self, makeRequest):
        """Expenses: Purchase Bills Index via GET
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL)
        return makeRequest(url, 'GET')

    def createBasicBill(self, makeRequest, data):
        """Expenses: Purchase Bills Create Basic via POST
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '#basic')
        return makeRequest(url, 'POST', data)

    def createDetailedBill(self, makeRequest, data):
        """Expenses: Purchase Bills Create Detailed via POST
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '#detailed')
        return makeRequest(url, 'POST', data)

    def showBill(self, makeRequest, pk):
        """Expenses: Purchase Bills Show via GET
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def deleteBill(self, makeRequest, pk):
        """Expenses: Purchase Bills DELETE via DELETE
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    def editBasicBill(self, makeRequest, data, pk):
        """Expenses: Purchase Bills Edit Basic via PUT
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '#basic')
        return makeRequest(url, 'PUT', data)

    def editDetailedBill(self, makeRequest, data, pk):
        """Expenses: Purchase Bills Edit Detailed via PUT
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '#detailed')
        return makeRequest(url, 'PUT', data)

    def payBill(self, makeRequest, data, pk):
        """Expenses: Purchase Bills Pay via POST
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '/payments')
        return makeRequest(url, 'POST', data)

    def cancelBill(self, makeRequest, pk):
        """Expenses: Purchase Bills Cancel via DELETE
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    def recoverBill(self, makeRequest, pk):
        """Expenses: Purchase Bills Recover via PATCH
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '/recover')
        return makeRequest(url, 'PATCH')

    def archiveBill(self, makeRequest, pk):
        """Expenses: Purchase Bills Archive via PATCH
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '/archive')
        return makeRequest(url, 'PATCH')

    def unarchiveBill(self, makeRequest, pk):
        """Expenses: Purchase Bills Unarchive via PATCH
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk +
                              '/unarchive')
        return makeRequest(url, 'PATCH')

    # Expenses: Bank Fees
    def createBankFee(self, makeRequest, data):
        """Expenses: Bank Fees Create via POST
        """
        url = self.replaceUrl(urls.BANK_FEES_URL)
        return makeRequest(url, 'POST', data)

    def showBankFee(self, makeRequest, pk):
        """Expenses: Bank Fees Show via GET
        """
        url = self.replaceUrl(urls.BANK_FEES_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def editBankFee(self, makeRequest, data):
        """Expenses: Bank Fees Edit via PUT
        """
        url = self.replaceUrl(urls.BANK_FEES_URL)
        return makeRequest(url, 'PUT', data)

    def deleteBankFee(self, makeRequest, pk):
        """Expenses: Bank Fees Delete via DELETE
        """
        url = self.replaceUrl(urls.BANK_FEES_URL)
        return makeRequest(url, 'DELETE')

    def archiveBankFee(self, makeRequest, pk):
        """Expenses: Bank Fees Archive via PATCH
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk + '/archive')
        return makeRequest(url, 'PATCH')

    def unarchiveBankFee(self, makeRequest, pk):
        """Expenses: Bank Fees Unarchive via PATCH
        """
        url = self.replaceUrl(urls.PURCHASE_BILLS_URL + '/' + pk +
                              '/unarchive')
        return makeRequest(url, 'PATCH')

    def payBankFee(self, makeRequest, data, pk):
        """Expenses: Bank Fees Pay via POST
        """
        url = self.replaceUrl(urls.BANK_FEES_URL + '/' + pk + '/payments')
        return makeRequest(url, 'POST', data)

    # Expenses: Salaries
    def indexSalary(self, makeRequest):
        """Expenses: Salaries Index via GET
        """
        url = self.replaceUrl(urls.SALARIES_URL)
        return makeRequest(url, 'GET')

    def createSalary(self, makeRequest, data):
        """Expenses: Salaries Create via POST
        """
        url = self.replaceUrl(urls.SALARIES_URL)
        return makeRequest(url, 'POST', data)

    def showSalary(self, makeRequest, pk):
        """Expenses: Salaries Show via GET
        """
        url = self.replaceUrl(urls.SALARIES_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def editSalary(self, makeRequest, data, pk):
        """Expenses: Salaries Edit via PUT
        """
        url = self.replaceUrl(urls.SALARIES_URL + '/' + pk)
        return makeRequest(url, 'PUT', data)

    def deleteSalary(self, makeRequest, pk):
        """Expenses: Salaries Delete via DELETE
        """
        url = self.replaceUrl(urls.SALARIES_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    def archiveSalary(self, makeRequest, pk):
        """Expenses: Salaries Archive via PATCH
        """
        url = self.replaceUrl(urls.SALARIES_URL + '/' + pk + '/archive')
        return makeRequest(url, 'PATCH')

    def unarchiveSalary(self, makeRequest, pk):
        """Expenses: Salaries unarchive via PATCH
        """
        url = self.replaceUrl(urls.SALARIES_URL + '/' + pk + '/unarchive')
        return makeRequest(url, 'PATCH')

    def paySalary(self, makeRequest, data, pk):
        """Expenses: Salaries Pay via POST
        """
        url = self.replaceUrl(urls.SALARIES_URL + '/' + pk + '/payments')
        return makeRequest(url, 'POST', data)

    # Expenses: Taxes
    def indexTax(self, makeRequest):
        """Expenses: Taxes Index via GET
        """
        url = self.replaceUrl(urls.TAXES_URL)
        return makeRequest(url, 'GET')

    def createTax(self, makeRequest, data):
        """Expenses: Taxes Create via POST
        """
        url = self.replaceUrl(urls.TAXES_URL)
        return makeRequest(url, 'POST', data)

    def showTax(self, makeRequest, pk):
        """Expenses: Taxes Show via GET
        """
        url = self.replaceUrl(urls.TAXES_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def editTax(self, makeRequest, data, pk):
        """Expenses: Taxes Edit via PUT
        """
        url = self.replaceUrl(urls.TAXES_URL + '/' + pk)
        return makeRequest(url, 'PUT', data)

    def deleteTax(self, makeRequest, pk):
        """Expenses: Taxes Delete via DELETE
        """
        url = self.replaceUrl(urls.TAXES_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    def archiveTax(self, makeRequest, pk):
        """Expenses: Taxes Archive via PATCH
        """
        url = self.replaceUrl(urls.TAXES_URL + '/' + pk + '/archive')
        return makeRequest(url, 'PATCH')

    def unarchiveTax(self, makeRequest, pk):
        """Expenses: Taxes unarchive via PATCH
        """
        url = self.replaceUrl(urls.TAXES_URL + '/' + pk + '/unarchive')
        return makeRequest(url, 'PATCH')

    def payTax(self, makeRequest, data, pk):
        """Expenses: Taxes Pay via POST
        """
        url = self.replaceUrl(urls.TAXES_URL + '/' + pk + '/payments')
        return makeRequest(url, 'POST', data)

    # Expenses: Employees
    def indexEmployee(self, makeRequest):
        """Expenses: Employees Index via GET
        """
        url = self.replaceUrl(urls.EMPLOYEES_URL)
        return makeRequest(url, 'GET')

    def createEmployee(self, makeRequest, data):
        """Expenses: TaxesEmployees Create via POST
        """
        url = self.replaceUrl(urls.EMPLOYEES_URL)
        return makeRequest(url, 'POST', data)

    def showEmployee(self, makeRequest, pk):
        """Expenses: Employees Show via GET
        """
        url = self.replaceUrl(urls.EMPLOYEES_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def editEmployee(self, makeRequest, data, pk):
        """Expenses: Employees Edit via PUT
        """
        url = self.replaceUrl(urls.EMPLOYEES_URL + '/' + pk)
        return makeRequest(url, 'PUT', data)

    def deleteEmployee(self, makeRequest, pk):
        """Expenses: Employees Delete via DELETE
        """
        url = self.replaceUrl(urls.EMPLOYEES_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    def archiveEmployee(self, makeRequest, pk):
        """Expenses: Employees Archive via PATCH
        """
        url = self.replaceUrl(urls.EMPLOYEES_URL + '/' + pk + '/archive')
        return makeRequest(url, 'PATCH')

    def unarchiveEmployee(self, makeRequest, pk):
        """Expenses: Employees unarchive via PATCH
        """
        url = self.replaceUrl(urls.EMPLOYEES_URL + '/' + pk + '/unarchive')
        return makeRequest(url, 'PATCH')

    """### Legalize ###"""

    # Legalize: E-Invoice Inboxes
    def indexEInvoiceInbox(self, makeRequest):
        """Legelize: E-Invoice Inboxes Index via GET
        """
        url = self.replaceUrl(urls.E_INVOICE_INBOX_URL)
        return makeRequest(url, 'GET')

    # Legalize: E-Archives
    def createEArchive(self, makeRequest, data):
        """Legalize: E-Arhives Create via POST
        """
        url = self.replaceUrl(urls.E_ARCHIVES_URL)
        return makeRequest(url, 'POST', data)

    def showEArchive(self, makeRequest, data, pk):
        """Legalize: E-Arhives Show via GET
        """
        url = self.replaceUrl(urls.E_ARCHIVES_URL + '/' + pk)
        return makeRequest(url, 'GET', data)

    def showEArchivePDF(self, makeRequest, data, pk):
        """Legalize: E-Arhives Show PDF via GET
        """
        url = self.replaceUrl(urls.E_ARCHIVES_URL + '/' + pk + '/pdf')
        return makeRequest(url, 'GET', data)

    # Legalize: E-Invoices
    def createEInvoice(self, makeRequest, data):
        """Legalize: E-Invoices Create via POST
        """
        url = self.replaceUrl(urls.E_INVOICE_URL)
        return makeRequest(url, 'POST', data)

    def showEInvoice(self, makeRequest, data, pk):
        """Legalize: E-Invoices Show via GET
        """
        url = self.replaceUrl(urls.E_INVOICE_URL + '/' + pk)
        return makeRequest(url, 'GET', data)

    def showEInvoicePDF(self, makeRequest, data, pk):
        """Legalize: E-Invoices Show PDF via GET
        """
        url = self.replaceUrl(urls.E_INVOICE_URL + '/' + pk + '/pdf')
        return makeRequest(url, 'GET', data)

    # Legalize: E-SMM
    def createEsmm(self, makeRequest, data):
        """Legalize: E-SMM Create via POST
        """
        url = self.replaceUrl(urls.E_SMMS_URL)
        return makeRequest(url, 'POST', data)

    def showEsmm(self, makeRequest, data, pk):
        """Legalize: E-SMM Show via GET
        """
        url = self.replaceUrl(urls.E_SMMS_URL + '/' + pk)
        return makeRequest(url, 'GET', data)

    def showEsmmPDF(self, makeRequest, data, pk):
        """Legalize: E-SMM Show PDF via GET
        """
        url = self.replaceUrl(urls.E_SMMS_URL + '/' + pk + '/pdf')
        return makeRequest(url, 'GET', data)

    """### Cash ###"""

    # Cash: Accounts
    def indexAccount(self, makeRequest):
        """Cash: Accounts Index via GET
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL)
        return makeRequest(url, 'GET')

    def createAccount(self, makeRequest, data):
        """Cash: Accounts Create via POST
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL)
        return makeRequest(url, 'POST', data)

    def showAccount(self, makeRequest, pk):
        """Cash: Accounts Show via GET
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def editAccount(self, makeRequest, data, pk):
        """Cash: Accounts Edit via PUT
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk)
        return makeRequest(url, 'PUT', data)

    def deleteAccount(self, makeRequest, pk):
        """Cash: Accounts Delete via DELETE
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    def transactionsAccount(self, makeRequest, pk):
        """Cash: Accounts Transactions Get via GET
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk + '/transactions')
        return makeRequest(url, 'GET')

    def debitTransactionAccount(self, makeRequest, data, pk):
        """Cash: Accounts Debit Transaction via POST
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk +
                              '/debit_transactions')
        return makeRequest(url, 'POST', data)

    def creditTransactionAccount(self, makeRequest, data, pk):
        """Cash: Accounts Credit Transaction via POST
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk +
                              '/credit_transactions')
        return makeRequest(url, 'POST', data)

    # Cash: Transactions
    def showTransaction(self, makeRequest, pk):
        """Cash: Accounts Show via GET
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk)
        return makeRequest(url, 'GET')

    def deleteTransaction(self, makeRequest, pk):
        """Cash: Accounts Delete via DELETE
        """
        url = self.replaceUrl(urls.ACCOUNTS_URL + '/' + pk)
        return makeRequest(url, 'DELETE')

    """### Stock/Hoard ###"""
    """### Settings ###"""
    """### Other ###"""
