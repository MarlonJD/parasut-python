# URL Constants
BASE_URL = 'https://api.parasut.com/v4/'
TOKEN_URL = 'https://api.parasut.com/oauth/token'
SANDBOX_BASE_URL = 'https://api.heroku-staging.parasut.com/v4/'
SANDBOX_TOKEN_URL = 'https://api.heroku-staging.parasut.com/oauth/token'
COMPANY_ID = ':company_id'

# Sales
SALES_INVOICES_URL = BASE_URL + COMPANY_ID + '/sales_invoices'
SALES_INVOICES_URL = BASE_URL + COMPANY_ID + '/sales_invoices'
CONTACTS_URL = BASE_URL + COMPANY_ID + '/contacts'

# Expenses
PURCHASE_BILLS_URL = BASE_URL + COMPANY_ID + '/purchase_bills'
BANK_FEES_URL = BASE_URL + COMPANY_ID + '/bank_fees'
SALARIES_URL = BASE_URL + COMPANY_ID + '/salaries'
TAXES_URL = BASE_URL + COMPANY_ID + '/taxes'
EMPLOYEES_URL = BASE_URL + COMPANY_ID + '/employees'

# LEGALIZE
E_INVOICE_INBOX_URL = BASE_URL + COMPANY_ID + '/e_invoice_inboxes'
E_ARCHIVES_URL = BASE_URL + COMPANY_ID + '/e_archives'
E_INVOICE_URL = BASE_URL + COMPANY_ID + '/e_invoices'
E_SMMS_URL = BASE_URL + COMPANY_ID + '/e_smms'

# CASH
ACCOUNTS_URL = BASE_URL + COMPANY_ID + '/accounts'
TRANSACTIONS_URL = BASE_URL + COMPANY_ID + '/transactions'

# STOCK/HOARD
PRODUCTS_URL = BASE_URL + COMPANY_ID + '/products'
SHIPMENT_DOCUMENTS_URL = BASE_URL + COMPANY_ID + '/shipment_documents'
STOCK_MOVEMENTS_URL = BASE_URL + COMPANY_ID + '/stock_movements'

# SETTINGS
CATEGORIES_URL = BASE_URL + COMPANY_ID + '/item_categories'
TAGS_URL = BASE_URL + COMPANY_ID + '/tags'

# OTHER
ME_URL = BASE_URL + 'me'
SANDBOX_ME_URL = SANDBOX_BASE_URL + 'me'
TRACKABLE_JOB = BASE_URL + COMPANY_ID + '/trackable_jobs/'
