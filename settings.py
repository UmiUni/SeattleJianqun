# -*- coding: UTF-8 -*-
import datetime
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 
  global ADMIN
  global previousDay

  chatGroups =[
  u'西雅图拼车接机',
  u'西雅图租房',
  u'西雅图周末活动',
  u'西雅图美食',
  u'西雅图二手',
  u'西雅图实名制',
  u'西雅图工作实习内推',
  u'Chuck郭律师',
  u'Pokemon Go北美交流总群',
  u'北美区块链技术交流总群',
  u'Zillow内推面试刷题群',
  u'Amazon内推面试刷题群',
  u'Microsoft内推面试刷题群',
  u'北美股市Trading技术交流总群1'
  ]

  v0= u"您好,UW西雅图加群建群小助手为您服务:)\n"
  v00=u"每天只能加1个群哦;\n"
  v1= u"回复 0 加西雅图拼车接机群;\n"
  v2= u"回复 1 加西雅图租房群;\n"
  v3= u"回复 2 加西雅图周末活动群;\n"
  v4= u"回复 3 加西雅图美食约饭群;\n"
  v5= u"回复 4 加西雅图二手货群;\n"
  v6= u"回复 5 加西雅图实名制华人群;\n"
  v7= u"回复 6 加西雅图工作实习内推总群;\n"
  v8= u"回复 7 加Chuck郭律师美帝绿卡讨论群;\n"
  v9= u"回复 8 Pokemon Go北美交流总群;\n"
  v10= u"回复 9 北美区块链技术交流总群;\n"
  v11= u"回复 10 Zillow内推面试刷题群;\n"
  v12= u"回复 11 Amazon内推面试刷题群;\n"
  v13= u"回复 12 Microsoft内推面试刷题群;\n"
  v14= u"回复 99 查看【北美加群小助手Jogchat.com】\n微信公众号, 加纽约、硅谷等地群(无次数限制)\n"
  v15= u"回复 100 加北美股市Trading技术交流总群1(无次数限制)\n"
  vT =v0+v00+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15
  
  usersDict = {}
  admins = []
  ADMIN = u'西雅图加群助手jogchat.com'


  save = [
  u'天天刷题',
  u'北美CPA',
  u'北美妈妈',
  u'北美信用',
  u'线上KTV',
  u'北美表情分享',
  u'UW西雅图_周末活动']

  v7= u"回复 1 加北美CS刷题竞赛面试总群;\n"
  v8= u"回复 6 加北美CPA,REG天天刷题群;\n"
  v9= u"回复 7 加北美妈妈母婴总群;\n"
  v10= u"回复 8 北美信用卡爱好者总群;\n"
  v11= u"回复 9 加线上KTV开嗓🎙️北美总群;\n"
  v12= u"回复 10 加北美表情分享总群;\n"
  v13= u"回复 11 加UW西雅图_周末活动群;\n"
  previousDay = datetime.datetime.now().day
