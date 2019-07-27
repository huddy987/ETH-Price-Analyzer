import time  # For sleep

import util  # Project-related utility functions
import exchange_API.exchange_manager as exchange_manager # Exchange class manager

debug = True

if __name__ == "__main__":
    exchanges = exchange_manager.initialize_exchange_dict()

    while(True):
        ETH_dict = exchange_manager.get_ETH_price_dict(exchanges)
        bid_dict = exchange_manager.get_ETH_bid_dict(exchanges)
        ask_dict = exchange_manager.get_ETH_ask_dict(exchanges)

        lowest_price, lowest_exchange_name = util.get_min_ETH_price(ETH_dict)
        highest_price, highest_exchange_name = util.get_max_ETH_price(ETH_dict)
        average_price = util.get_average_ETH_price(ETH_dict)

        if(debug):
            print("DEBUG stats:")
            print("lowest_exchange: " + lowest_exchange_name)
            print("highest_exchange: " + highest_exchange_name)
            print("lowest_price: " + str(lowest_price))
            print("average_price: " + str(average_price))
            print("highest_price: " + str(highest_price))

        # If the highest price is 2% higher than the lowest price, initiate a buy
        if((lowest_price + lowest_price * 0.02) < highest_price):

            # Convert all USDT in the account to ETH
            exchanges[lowest_exchange_name].ETH_bal += exchanges[lowest_exchange_name].USDT_bal / lowest_price
            exchanges[lowest_exchange_name] = 0

            if(debug):
                print("New ETH Bal on " + lowest_exchange_name +
                      ": " + exchanges[lowest_exchange_name].ETH_bal)
                print("New USDT Bal on " + lowest_exchange_name +
                      ": " + exchanges[lowest_exchange_name].USDT_bal)

            # Continually check if we should sell
            while(True):
                lowest_price = exchanges[lowest_exchange_name].get_ETH_price()
                if(lowest_price >= average_price):
                    # Sell condition
                    exchanges[lowest_exchange_name].USDT_bal += exchanges[lowest_exchange].ETH_bal / lowest_price
                    exchanges[lowest_exchange_name] = 0

                    if(debug):
                        print("New ETH Bal on " + lowest_exchange_name +
                              ": " + exchanges[lowest_exchange_name].ETH_bal)
                        print("New USDT Bal on " + lowest_exchange_name +
                              ": " + exchanges[lowest_exchange_name].USDT_bal)
                    break
        else:
            print("Done a cycle, no buy detected. Sleep for 30s")
            time.sleep(30)
