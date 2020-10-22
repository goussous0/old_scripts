import datetime
import time
import random

date = [1580593646270,1580593432333,1580589463587]


    
def check_trade(trade_time,ttl):
    ## get the current system time to compare to the trade time
    current_time = int(time.time())
    ## trade time passed from the binance API
    trade_time = int(trade_time)/1000
    ## up_time in mins
    up_time = (((int(current_time))-int(trade_time))/60)
    ## ttl time to live for trade
    
   
    print (str(ttl) + " <-----------this is the time to live for each trade")
    ## an if statement that check for the time if it over the ttl it get canceled and removed from the logs
    
    if float(ttl)<= float(up_time):
        print ("cancling trade because ttl is over")
    else:
        print (str(float(ttl)-float(up_time))+ "mins left for canceling trade")
    
    print (up_time)
    return


for item in date:
    trade_time = item
    ttl = random.randrange(100, 1440)
    check_trade(trade_time,ttl)
#    
    #st =int(time.time())
    #t_d =(int(item)/1000)
    
    
         
    #x = ((t_d-st)*-1)/60/60
    #print (x)
    #print ((float(x)-float(int(x)))*60)
    
    #trade_date =  str((datetime.datetime.fromtimestamp(int(item)/1000))).split()
    #print (trade_date[1])
