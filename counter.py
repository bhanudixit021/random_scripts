import re
def func(input):
  item_list = ()
  count = 0
  temp = dict()
  temp['mid']= re.findall(r'mid: "(.*?)"', input.content)
  temp['peak']=re.findall(r'peak: (.*?) ', input.content)
  temp['average']= re.findall(r'average: (.*?)}', input.content)
  item_list.append(temp)
  return item_list

