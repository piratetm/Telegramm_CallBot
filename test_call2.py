import os, requests


   operation=genCall
   sipuid="0042656976"
   password="VaLiUnOv1"
   SrcPhone="0042656976@sipnet.ru"
   DstPhone="79952354128"
   [Delay=1]
   [prompt=<ссылка на звуковой файл приветствия>]
   [format={0,1,2}]
   [lang={ru}]
url = "https://api.sipnet.ru/cgi-bin/Exchange.dll/sip_balance?operation=balance&sipuid=" + sipuid + "&password=" + password
#   https://api.sipnet.ru/cgi-bin/Exchange.dll/sip_balance?operation=genCall&sipuid=0042656976&password=VaLiUnOv1&SrcPhone=0042656976@sipnet.ru&DstPhone=79952354128



