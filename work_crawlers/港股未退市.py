# 初始框架
import requests
import json
import time


class df():

	def runner(self, kw):
		# print(kw)
		# https://www1.hkex.com.hk/hkexwidget/data/getstocksearch?lang=eng&token=evLtsLsBNAUVTPxtGqVeGz/Jij6sNYchJINwi8TYjK+TpVoxfPPbUlHW0XUW9m/w&pre=10&keyword=00700&qid=1588988292430&callback=jQuery311014730077554693044_1588937120138&_=1588937120231

		url = 'https://www1.hkex.com.hk/hkexwidget/data/getstocksearch'
		# headers = {
		# 	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
		# }
		# 参数
		params = {
			'lang': 'eng',
			'token': 'evLtsLsBNAUVTPxtGqVeGz/Jij6sNYchJINwi8TYjK+TpVoxfPPbUlHW0XUW9m/w',
			'pre': '10',
			'keyword': kw,
			'qid': time.time(),
			'callback': 'jQuery',
			'_': time.time()
		}
		try:
			# timeout 超时报错
			response = requests.get(url=url, params=params,  timeout=10).text  # string格式
		except:
			response = requests.get(url=url, params=params, timeout=10).text

		print(response)
		x = response.index('{')
		response = response[x: -1]

		# 转换为json格式
		list_data = json.loads(response)
		# 判断是否退市 stocklist字段为空为已退市
		if list_data['data']['stocklist'] == []:
			print("%s已退市" % kw, list_data)
			fp.write(kw+" ")
			json.dump(list_data, fp, ensure_ascii=False)
			fp.write('\n')
		else:
			print("%s未退市" % kw)


if __name__ == "__main__":
	d = df()
	# 读取股票名称
	f = open('港股统计.txt', 'r')
	f_new = open('港股统计_new.txt', 'a', encoding='utf-8')
	print("股票名称读取成功，请耐心等待......")
	fp = open('已退市名单.txt', 'a', encoding='utf-8')

	# 循环查找
	for a in f.read().split():

		d.runner(a)
		# time.sleep单位为秒
		time.sleep(0.5)
		f_new.write(a+'\n')

	print('【程序运行结束!】')
	f.close()
	fp.close()
	f_new.close()
