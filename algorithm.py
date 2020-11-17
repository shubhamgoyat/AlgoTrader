from yahoo_fin.stock_info import *

exit_main = 0
Balance = 100000
owned_shares = 0
count = 0
owned_stocks_symbol = ["AAPL"]
owned_stocks_volume = [0]
i = 0
exit1 = 0
exit2 = 0

while exit_main == 0:
    stock = raw_input("Enter Symbol: ")
    stock_price = get_live_price(stock)
    print ("Current Stock Price of " + stock + ":")
    print (stock_price)
    print ("Current Account Balance:")
    print (Balance)
    print ("Number of Shares owned of " + stock + ":")
    print (owned_shares)

    while exit1 == 0:
        command = raw_input(
            "\n Enter Stats to get Statistics \n Enter Sheet to get Balance Sheet \n Enter Val to get Valuation Stats \n Enter AnalyInfo to get Analysts Info \n Enter Holders to get Holders info \n Enter Trade to buy or sell stock \n Enter Exit to Quit the Program : \n")
        if command == "Stats":
            print (get_stats(stock))
        elif command == "Sheet":
            print (get_balance_sheet(stock))
        elif command == "Val":
            print (get_stats_valuation(stock))
        elif command == "AnalyInfo":
            print (get_analysts_info(stock))
        elif command == "Holders":
            print (get_holders(stock))
        elif command == "Exit":
            count = 1
            break
        elif command == "Trade":
            while count == 0:
                order = raw_input("Enter Buy or Sell to place order(Or Exit to exit): \n")
                if order == "Exit":
                    count = 1
                    break
                else:
                    volume = input("Enter Volume of Stocks to Buy or Sell: \n")
                    if order == "Buy":
                        if Balance < 0 or (Balance - (stock_price * volume)) < 0:
                            print ("Insuffecient Balance to execute the order.\n")
                        else:
                            owned_shares = owned_shares + volume
                            Balance = Balance - (stock_price * volume)
                            for i in range(len(owned_stocks_symbol)):
                                if stock == owned_stocks_symbol[i]:
                                    owned_stocks_volume[i] = volume + owned_stocks_volume[i]
                                    break
                                else:
                                    owned_stocks_symbol.append(stock)
                                    owned_stocks_volume.append(volume)
                            print ("Stocks owned on Account are: ")
                            print ("(Symbol, Vol)")
                            for i in range(len(owned_stocks_symbol)):
                                print (owned_stocks_symbol[i], owned_stocks_volume[i])
                    elif order == "Sell":
                        if owned_shares < 0:
                            print ("Insuffecient Balance to execute the order.\n")
                        else:
                            owned_shares = owned_shares - volume
                            Balance = Balance + (stock_price * volume)
                            for i in range(len(owned_stocks_symbol)):
                                if stock == owned_stocks_symbol[i]:
                                    owned_stocks_volume[i] = owned_stocks_volume[i] - volume
                            print ("Stocks owned on Account are: ")
                            print ("(Symbol, Vol)")
                            for i in range(len(owned_stocks_symbol)):
                                print (owned_stocks_symbol[i], owned_stocks_volume[i])
                    elif order == "Exit":
                        count = 1
                        break

    print ("Current Stock Price of " + stock + ":")
    print (stock_price)
    print ("Current Balance:")
    print (Balance)
    print ("Number of Shares owned of " + stock + ": ")
    print (owned_shares)
    print ("Stocks owned on Account are: ")
    print ("(Symbol, Vol)")
    for i in range(len(owned_stocks_symbol)):
        print (owned_stocks_symbol[i], owned_stocks_volume[i])

