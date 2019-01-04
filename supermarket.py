from MarketClass import Market

market = Market("Safeway","7 AM to 10 PM","50 total employees",10)

print (market.name)
print (market.store_hours)
print (market.employees)

market.buy("eggs",3)
market.buy("chips",1)

market.returning("chips")
