import requests

class HighLow:
    """Retrives the peaks and bottoms of stock prices for a desired stock symbol""" 

    def __init__ (self, symbol, apikey, alert):
       self.symbol = symbol 
       self.apikey = apikey
       self.alertPercent = alert

    def data(self):
        """Retrives percentage of current price from peaks and bottoms"""

        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + self.symbol + "&apikey=" + self.apikey
        r = requests.get(url)
        data = r.json()
        pricesList = []
        timeSeriesValues = (data['Time Series (Daily)'])#retrieves values under data
        
        largestNum = -99999999.00
        lowestNum = 99999999.00

     
        for x in timeSeriesValues:
            price = timeSeriesValues[x]['4. close'] #retrieves the price
            pricesList.append(price)
            price = float(price)
          
            if price > largestNum: 
                largestNum = price #retrieves the peak price
                highDate = x
            if price < lowestNum:
                lowestNum = price #retreives the bottom price
                lowDate = x
                
        currentPrice = float(pricesList[0]) #retrieves current price from all prices
       
        currentToHigher = round(((currentPrice/largestNum)*100),2) #current price is x percent of the peak
        currentToLower = round(((currentPrice/lowestNum)*100),2) #current price is x percentage of the bottom 
        higherToLower = round(((largestNum/lowestNum)*100),2) #overall range 
 	 
        percentToHigher = 100 - currentToHigher #retrievs percentage
        percentToLower = currentToLower - 100
        
        if percentToHigher <= self.alertPercent or percentToLower <= self.alertPercent : #sets alert conditions
            return str(self.symbol) + ":\n Current price is " + str(currentToHigher)+ "% of the peak" + "\n Current price is " + str(currentToLower) + "% of the bottom" + "\n The peak is " + str(higherToLower) + "% higher than the bottom\n" + "It is a favourable time to buy or sell stocks.\n\n"  
        else: 
            return "None"
      
   	
	
