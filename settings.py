# -*- coding: UTF-8 -*-
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 
  global ADMIN

  chatGroups =[
  u'UW西雅图拼车接机',
  u'UW西雅图租房',
  u'UW西雅图校友',
  u'UW西雅图美食',
  u'UW西雅图二手',
  u'西雅图实名制'
  ]

  v0= u"您好,UW西雅图加群建群小助手为您服务:)\n"
  v00=u"每天只能加4个群哦;\n"
  v1= u"回复 0 加UW西雅图拼车接机群;\n"
  v2= u"回复 1 加UW西雅图租房群;\n"
  v3= u"回复 2 加UW西雅图校友群;\n"
  v4= u"回复 3 加UW西雅图美食约饭群;\n"
  v5= u"回复 4 加UW西雅图二手货群;\n"
  v6= u"回复 5 加西雅图实名制华人群;\n"
  v14= u"回复 99 查看【北美加群小助手Jogchat.com】
         \n微信公众号, 加纽约、硅谷等地群\n"

  vT =v0+v00+v1+v2+v3+v4+v5+v6+v14
  
  usersDict = {}
  admins = []
  ADMIN = u'UW西雅图加群小助手'


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
