import os
import csv
import requests

class BotService(object):

    api_url = 'https://stooq.com/q/l/'

    def quote_stock(self, stock_code):
        """
            Retrieve a stock quote for the stock intent
        """

        stock_url = '{host}?f=sd2t2ohlcv&h&e=csv&s={stock_code}'.format(
            host=self.api_url,
            stock_code=stock_code
        )

        with requests.Session() as s:
            download = s.get(stock_url)
            line_iterator = (x for x in download.iter_lines(decode_unicode=True))

            cr = csv.reader(line_iterator, delimiter=',')
            lines = list(cr)
            
            if len(lines) == 2:
                return lines[1][3]
            else:
                return -1
        