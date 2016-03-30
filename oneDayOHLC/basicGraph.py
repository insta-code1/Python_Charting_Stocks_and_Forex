import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib
matplotlib.rcParams.update({'font.size': 10})

eachStock = 'TSLA','AAPL'

def graphData(stock):
    try:
        stockFile = stock+'.txt'    #change to different directory using '../directory'

        date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile,delimiter=',',unpack=True,
                                                              converters={ 0: mdates.strpdate2num('%Y%m%d')})

        fig = plt.figure()
        ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4)
        ax1.plot(date, openp)
        ax1.plot(date, highp)
        ax1.plot(date, lowp)
        ax1.plot(date, closep)
        plt.ylabel('Stock Price')
        ax1.grid(True)

        ax2 = plt.subplot2grid((5,4), (4,0), sharex=ax1, rowspan=4, colspan=4)
        ax2.bar(date, volume)
        ax2.axes.yaxis.set_ticklabels([])
        plt.ylabel('Volume')
        ax2.grid(True)

        ax1.xaxis.set_major_locator(mticker.MaxNLocator(12))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(90)

        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        plt.subplots_adjust(left=.10, bottom=.19, right=.93, top=.95, wspace=.20, hspace=.07)

        plt.xlabel('Date')

        plt.setp(ax1.get_xticklabels(), visible=False)

        plt.suptitle(stock+' Stock Price')

        plt.subplots_adjust(left=.09, bottom=.18, right=.94, top=.94, wspace=.20, hspace=0)
        plt.show()





    except Exception, e:
        print 'failed main loop',str(e)


for stock in eachStock:
    graphData(stock)
    time.sleep(555)