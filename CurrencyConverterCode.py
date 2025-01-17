# This Code will convert the top 10 worlwide currencies using a base amount of 100 USD
import requests 

# Get your own API_KEY using https://www.exchangerate-api.com/, then replace it below
API_KEY = 'ecad770deb5e20e6f44f00dc'

# BASE_URL gathers the data on ExchnageRates-API
BASE_URL = 'https://v6.exchangerate-api.com/v6'

# List of top 10 worldwide currencies 
currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'HKD', 'NZD']

# This function retrieves the exchange rates
def get_exchange_rates(base_currency):
    url = f'{BASE_URL}/{API_KEY}/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']

# This function converts the amount of one currency to another
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != to_currency:
        rate = rates[to_currency]
        return amount * rate
    return amount

# This is the main currency for the basis of conversion
def main():
    # Base currency for conversion
    base_currency = 'USD' 
    # Amount being converted 
    amount = 100  

    rates = get_exchange_rates(base_currency)

# This wil generate a nice message above the output
    print("Hello User!, Your Currency Conversion is: ")

    for currency in currencies:
        converted_amount = convert_currency(amount, base_currency, currency, rates)
        print(f'{amount} {base_currency} = {converted_amount:.2f} {currency}')

if __name__ == '__main__':
    main()