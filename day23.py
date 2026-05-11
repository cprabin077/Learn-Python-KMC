import requests

# print("FROM URL-----------------------------------------------------------------------------------------")
# url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json() ['response']
#     for i in data:
#         print(i['indices'], i['percentage_change'])
#         # break
#     # print(type(data))
#     # print(data.keys())
#     # print(data) # <Response [200]>
# else:
#     print("Failure")

# print("FROM URL-1-----------------------------------------------------------------------------------------")
# url1 = 'https://markets.onlinekhabar.com/smtm/home/date-wise-market-calendar'

# req = requests.get(url1)
# if req.status_code == 200:
#     data = req.json() ['response']
#     # print(type(data))
#     # print(data.keys())
#     for i in data:
#         print(i['date'],"-", i['ticker'],"-", i['company_name'],"-", i['message'],"-")
#         #  break

# else:
#     print("Fail")

# print("FROM URL-2------------------------------------------------------------------------------------------")
# url2 = 'https://markets.onlinekhabar.com/smtm/home/most-searched-stocks'

# req = requests.get(url2)
# if req.status_code == 200:
#     data = req.json() ['response']
#     # print(type(data))
#     # print(data.keys())
#     for i in data:
#         print(i)
#         # print(i['date'],"-", i['ticker'],"-", i['company_name'],"-", i['message'],"-")
#         #  break

# else:
#     print("Fail")

print("FROM URL-3---------------------------------------------------------------------------------------")
url3 = 'https://markets.onlinekhabar.com/smtm/home/gainers-losers/Microfinance'

req = requests.get(url3)
if req.status_code == 200:
    data = req.json() 
    print(type(data))
    print(data.keys())
    data1 = data['response']
    print(type(data1))
    print(data1.keys())

    # top gainer
    top_gainer = data1['topGainer']
    print(type(top_gainer))
    print(top_gainer.keys())
    print(top_gainer['ticker_name'], top_gainer['ltp'])
    # for i in result:
        # print(type(result))

    # top loser
    top_loser = data1['topLoser']
    print(type(top_loser))
    print(top_loser.keys())
    print(top_loser['ticker_name'], top_loser['ltp'])

else:
    print("Fail")

# print("FROM URL-4---------------------------------------------------------------------------------------------")