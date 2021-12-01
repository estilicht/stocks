msg1 = "Welcome to the stocks program"
print(msg1)
ticker_to_Name  = {
    'AAPL' : 'Apple', 
    'ABNB' : 'Airbnb',
    'AMZN' : 'Amazon', 
    'CVS' : 'CVS Health', 
    'F' : 'Ford Motor', 
    'K' : 'Kellogg', 
    'MSFT' : 'Microsoft', 
    'TSLA' : 'Tesla', 
    'NYT' : 'The New York Times', 
    'WMT' : 'Walmart'
}

ticker_to_value = {
    'AAPL' : '$151', 
    'ABNB' : '$207',
    'AMZN' : '$3540', 
    'CVS' : '$92', 
    'F' : '$204', 
    'K' : '$63', 
    'MSFT' : '$400', 
    'TSLA' : '$1055', 
    'NYT' : '$48', 
    'WMT' : '$144'
}
for key in ticker_to_Name:
    print (f"Use the ticker {key} for {ticker_to_Name[key]}")

msg2 = "To see the value of a stock, type the ticker symbol. Use capitol letters only."
print(msg2)
x = input()

if x in ticker_to_value:
    print(f"The value of {x} is {ticker_to_value[x]}")
else:
    msg3 = "Stock not found" 
    print(msg3)
    
input('Press ENTER to exit')