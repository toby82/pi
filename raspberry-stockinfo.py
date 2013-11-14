#  Copyright (c) 2007-2008, Corey Goldberg (corey@goldb.org) 
# 
#  2013 
#  Minnor imporvements added 
#  - get_prev_close(symbol) 
#  - get_open(symbol) 
# 
#   by Pitis Daniel - Florin    
# 
#  license: GNU LGPL 
# 
#  This library is free software; you can redistribute it and/or 
#  modify it under the terms of the GNU Lesser General Public 
#  License as published by the Free Software Foundation; either 
#  version 2.1 of the License, or (at your option) any later version. 
  
import urllib 
import time 
import RPi.GPIO as GPIO 
  
LCD_RS = 25
LCD_E  = 24
LCD_D4 = 23 
LCD_D5 = 17
LCD_D6 = 18
LCD_D7 = 22
   
LCD_WIDTH = 16 
LCD_CHR = True
LCD_CMD = False
   
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0 
   
E_PULSE = 0.00005
E_DELAY = 0.00005
  
def main(): 
   
  GPIO.setmode(GPIO.BCM)        
  GPIO.setup(LCD_E, GPIO.OUT)   
  GPIO.setup(LCD_RS, GPIO.OUT)  
  GPIO.setup(LCD_D4, GPIO.OUT)  
  GPIO.setup(LCD_D5, GPIO.OUT)  
  GPIO.setup(LCD_D6, GPIO.OUT)  
  GPIO.setup(LCD_D7, GPIO.OUT)  
   
  lcd_init() 
   
  # Here we show the message on the LCD screen 
  google_information = 'Close ' + get_prev_close('GOOG') 
  lcd_byte(LCD_LINE_1, LCD_CMD) 
  lcd_string("Google stock",2) 
  lcd_byte(LCD_LINE_2, LCD_CMD) 
  lcd_string(google_information,2) 
   
def lcd_init(): 
  lcd_byte(0x33,LCD_CMD) 
  lcd_byte(0x32,LCD_CMD) 
  lcd_byte(0x28,LCD_CMD) 
  lcd_byte(0x0C,LCD_CMD)   
  lcd_byte(0x06,LCD_CMD) 
  lcd_byte(0x01,LCD_CMD)   
   
def lcd_string(message,style): 
  # Send string to display 
  # style=1 Left justified 
  # style=2 Centered 
  # style=3 Right justified 
   
  if style==1: 
    message = message.ljust(LCD_WIDTH," ")   
  elif style==2: 
    message = message.center(LCD_WIDTH," ") 
  elif style==3: 
    message = message.rjust(LCD_WIDTH," ") 
   
  for i in range(LCD_WIDTH): 
    lcd_byte(ord(message[i]),LCD_CHR) 
   
def lcd_byte(bits, mode): 
  GPIO.output(LCD_RS, mode)  
   
  GPIO.output(LCD_D4, False) 
  GPIO.output(LCD_D5, False) 
  GPIO.output(LCD_D6, False) 
  GPIO.output(LCD_D7, False) 
  if bits&0x10==0x10: 
    GPIO.output(LCD_D4, True) 
  if bits&0x20==0x20: 
    GPIO.output(LCD_D5, True) 
  if bits&0x40==0x40: 
    GPIO.output(LCD_D6, True) 
  if bits&0x80==0x80: 
    GPIO.output(LCD_D7, True) 
   
  time.sleep(E_DELAY)     
  GPIO.output(LCD_E, True)   
  time.sleep(E_PULSE) 
  GPIO.output(LCD_E, False)   
  time.sleep(E_DELAY)       
   
  GPIO.output(LCD_D4, False) 
  GPIO.output(LCD_D5, False) 
  GPIO.output(LCD_D6, False) 
  GPIO.output(LCD_D7, False) 
  if bits&0x01==0x01: 
    GPIO.output(LCD_D4, True) 
  if bits&0x02==0x02: 
    GPIO.output(LCD_D5, True) 
  if bits&0x04==0x04: 
    GPIO.output(LCD_D6, True) 
  if bits&0x08==0x08: 
    GPIO.output(LCD_D7, True) 
   
  time.sleep(E_DELAY)     
  GPIO.output(LCD_E, True)   
  time.sleep(E_PULSE) 
  GPIO.output(LCD_E, False)   
  time.sleep(E_DELAY)    
  
def __request(symbol, stat): 
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat) 
    return urllib.urlopen(url).read().strip().strip('"') 
  
  
def get_all(symbol): 
    """ 
    Get all available quote data for the given ticker symbol. 
      
    Returns a dictionary. 
    """
    values = __request(symbol, 'l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7').split(',') 
    stock_data = {} 
    stock_data['price'] = values[0] 
    stock_data['change'] = values[1] 
    stock_data['volume'] = values[2] 
    stock_data['avg_daily_volume'] = values[3] 
    stock_data['stock_exchange'] = values[4] 
    stock_data['market_cap'] = values[5] 
    stock_data['book_value'] = values[6] 
    stock_data['ebitda'] = values[7] 
    stock_data['dividend_per_share'] = values[8] 
    stock_data['dividend_yield'] = values[9] 
    stock_data['earnings_per_share'] = values[10] 
    stock_data['52_week_high'] = values[11] 
    stock_data['52_week_low'] = values[12] 
    stock_data['50day_moving_avg'] = values[13] 
    stock_data['200day_moving_avg'] = values[14] 
    stock_data['price_earnings_ratio'] = values[15] 
    stock_data['price_earnings_growth_ratio'] = values[16] 
    stock_data['price_sales_ratio'] = values[17] 
    stock_data['price_book_ratio'] = values[18] 
    stock_data['short_ratio'] = values[19] 
    return stock_data 
      
      
def get_price(symbol):  
    return __request(symbol, 'l1') # get Last Trade (Price Only) 
  
  
def get_change(symbol): 
    return __request(symbol, 'c1') # get Change 
      
      
def get_volume(symbol):  
    return __request(symbol, 'v') # get more info 
  
  
def get_avg_daily_volume(symbol):  
    return __request(symbol, 'a2') # get Average Daily Volume 
      
      
def get_stock_exchange(symbol):  
    return __request(symbol, 'x') # get Stock Exchange 
      
      
def get_market_cap(symbol): 
    return __request(symbol, 'j1') # get Market Capitalization 
     
     
def get_book_value(symbol): 
    return __request(symbol, 'b4') # get Book Value 
  
  
def get_ebitda(symbol):  
    return __request(symbol, 'j4') # get EBITDA 
      
      
def get_dividend_per_share(symbol): 
    return __request(symbol, 'd') # get Divident per share 
  
  
def get_dividend_yield(symbol):  
    return __request(symbol, 'y') # get Dividend Yield 
      
      
def get_earnings_per_share(symbol):  
    return __request(symbol, 'e') # get Earnings per Share 
  
  
def get_52_week_high(symbol):  
    return __request(symbol, 'k') # get 52 Week High 
      
      
def get_52_week_low(symbol):  
    return __request(symbol, 'j') # get 52 week Low 
  
  
def get_50day_moving_avg(symbol):  
    return __request(symbol, 'm3') # get 50 Day Moving Average 
      
      
def get_200day_moving_avg(symbol):  # get 200 Day Moving Average 
    return __request(symbol, 'm4') 
      
      
def get_price_earnings_ratio(symbol):  
    return __request(symbol, 'r') # get P/E Ratio 
  
  
def get_price_earnings_growth_ratio(symbol):  
    return __request(symbol, 'r5') # get PEG Ratio 
  
  
def get_price_sales_ratio(symbol):  
    return __request(symbol, 'p5') # get Price / Sales 
      
      
def get_price_book_ratio(symbol):  
    return __request(symbol, 'p6') # get Price / Book 
         
         
def get_short_ratio(symbol):  
    return __request(symbol, 's7') # get Short Ratio 
      
def get_prev_close(symbol): 
    return __request(symbol, 'p') # get Prev close     
  
def get_open(symbol): 
    return __request(symbol, 'o') # get Open 
  
if __name__ == '__main__': 
    main()

