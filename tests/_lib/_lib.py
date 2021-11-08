import urllib
import os
import datetime
import logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

class UIActions(object):
    @classmethod
    def clear_clipboard(cls):
        from java.awt.datatransfer import StringSelection
        from java.awt import Toolkit
        toolkit = Toolkit.getDefaultToolkit()
        clipboard = toolkit.getSystemClipboard()
        clipboard.setContents(StringSelection(""), None)

class Reporting(object):
    @classmethod
    def test_log(cls, message):
        '''Print info in the Report.html, Console and Jenkins output'''
        label_timestamp = "[" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S] TEST_LOG: ')

        # print in console and Jenkins
        message_console_jenkins = str(label_timestamp) + str(message)
        logging.info(message_console_jenkins)
        
        # print in Report.html
        message_report_html = str(label_timestamp) + str(message)
        print(message_report_html)
