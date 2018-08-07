#!/usr/bin/env python2
# -*- encoding=utf-8 -*-


import sys
from ..duerosTest.dueros.Bot import Bot
from ..duerosTest.dueros.directive.Display.RenderTemplate import RenderTemplate
from ..duerosTest.dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1

##reload(sys)
sys.setdefaultencoding('utf8')

class Test(Bot):

    def __init__(self, request_data):
        super(Test, self).__init__(request_data)
        self.add_launch_handler(self.launch_request)
        self.add_intent_handler('inquiry', self.getTaxSlot)

    def launch_request(self):
        """
        打开调用名
        """

        self.wait_answer()
        template = BodyTemplate1()
        template.set_title('查询天气')
        template.set_plain_text_content('欢迎进入小雨知天气')
        template.set_background_image('http://img3.imgtn.bdimg.com/it/u=903644294,1034575207&fm=27&gp=0.jpg')
        template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')
        renderTemplate = RenderTemplate(template)
        return {
            'directives': [renderTemplate],
            'outputSpeech': r'欢迎进入小雨知天气，请告诉我你想知道哪天哪个城市的天气吧！'
        }

    def getTaxSlot(self):
        """
        获取槽位及逻辑处理
        """
        date = self.get_slots('sys.date')
        city = self.get_slots('sys.city')
        foreign_city = self.get_slots('sys.foreign-city')
        if not city and foreign_city
            city = foreign_city
        
        if date and not city and not foreign_city:
            self.nlu.ask('sys.city')
            renderTemplate = self.getTemplate(r'你想知道哪个城市的天气？')

            return {
                'directives': [renderTemplate],
                'reprompt': r'你想知道哪个城市的天气？',
                'outputSpeech': r'你想知道哪个城市的天气？'
            }

        if city or foreign-city and not date:
            self.nlu.ask('sys.date')
            renderTemplate = self.getTemplate(r'你想知道哪天的天气？')

            return {
                'directives': [renderTemplate],
                'reprompt': r'你想知道哪天的天气？',
                'outputSpeech': r'你想知道哪天的天气？'
            }

        wehtherReport = self.weatherReport(date, city)
        content = r'你要查询的天气是' + str(weatherReport)
        renderTemplate = self.getTemplate(content)
        return {
            'directives': [renderTemplate],
            'outputSpeech': content
        }

    def getTemplate(self, content):
        template = BodyTemplate1()
        template.set_title('小雨知天气')
        template.set_plain_text_content(content)
        template.set_background_image('http://img3.imgtn.bdimg.com/it/u=903644294,1034575207&fm=27&gp=0.jpg')
        template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')
        renderTemplate = RenderTemplate(template)
        return renderTemplate

    def weatherReport(self, date, city):
        '''
        调用天气接口
        '''
        return '你要查询的天气是？'


def handler(event, context):

    bot = Test(event)
    result = bot.run()
    return result
