import requests
import feedparser
import pprint
from flask import Flask

product={'Unleaded Petrol':1,'Premium Unleaded':2,'Diesel':4,'LPG':5, '98 RON':6,'E85':10,'Brand diesel':11}

'''
The list of A_Tod and list of B_Tmw are parsing RSS data from fuelwatch based on the product and the date. 
Eventually, this list will be build based on the region and the suburb. 
These two lists includes dictionaries with various information
For the purpose of this project, we only need to take few variables i.e: price, address and etc
To achive this, a sets of loops where defined to extract required varibales and store them within a list 
and finally create a new list. 
At the end, this list was sorted for a fuel price.    
    
    
'''


def Product_Type(prod):
    response_today = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(prod)+'&Day=today')  
    response_tmw = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(prod)+'&Day=tomorrow')
    feed_today = feedparser.parse(response_today.content)        
    feed_tmw = feedparser.parse(response_tmw.content)      
    A_Tod=feed_today['entries']
    B_Tmw=feed_tmw['entries']
    price = [A_Tod[i]['price'] for i in range(len(A_Tod))]
    price_tmw=[B_Tmw[i]['price'] for i in range(len(B_Tmw))]
    brand = [A_Tod[i]['brand'] for i in range(len(A_Tod))]
    brand_tmw=[B_Tmw[i]['brand'] for i in range(len(B_Tmw))]
    address = [A_Tod[i]['address'] for i in range(len(A_Tod))]  
    address_tmw=[B_Tmw[i]['address'] for i in range(len(B_Tmw))]    
    A_Tod_list= list(zip(price, address, brand)) 
    A_Tod_list.sort(reverse=True)
    print(*A_Tod_list,sep='\n')
    B_Tmw_list=list(zip(price_tmw, address_tmw, brand_tmw))
    B_Tmw_list.sort(reverse=True)
#   pprint.pprint(A_Tod_list)
#   print(len(B_Tmw_list),len(A_Tod_list))
#   pprint.pprint(B_Tmw_list)
    return A_Tod_list

#Product_Type(product['Premium Unleaded'])  

''' need to define a function to generate HTML '''
app = Flask(__name__)
@app.route('/Render_html')

def Render_html():
    website = request.args.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(prod)+'&Day=today')
    Product_Type(product['Premium Unleaded'])  
    return <h1>The website value is: {}'''.format(website)

    
        <h1>This is a form</h1>
        <form>
            <input type="text" name="abc" value="{abc_value}" />
            <input type="submit" value="submit" />
        </form>
    
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')