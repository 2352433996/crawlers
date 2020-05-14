import socket
# import robots


# import sys
# from apscheduler.schedulers.blocking import BlockingScheduler
# from dingding import jq_data as dd
# from iftime import d_time
# import time


def list_data(stockCode):  # 接受服务器下发的数据并提取出list字典
	try:
		recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = "121.41.29.58"  # 测试: 121.199.77.150:8008
		port = 8008  # 线上: 121.41.29.58:8008
		recv_socket.connect((host, port))
		sum = ''
		send_data = '{"channel":{"version":"2.0","sub":"quant","unsub":""},"user":{"id":"","sign":"91529d7d5a6303d286877bfb5dcd6484","device_id":"2019-12-18 15:58:33.477421 +0800 CST m=+0.109975980","ts":"1573733347"},"params":{"quant":{"encoding":"json","min_time":"","stock_code":"'+stockCode+'"}}}\n'
		recv_socket.send(send_data.encode(encoding='UTF-8', errors='ignore'))
		# a = recv_socket.recv(10240).decode('ascii')
		# errors='ignore' 忽略错误的字节
		a = recv_socket.recv(10240).decode('utf-8', errors='ignore')
		while a:
			sum += a
			a = recv_socket.recv(10240).decode('utf-8', errors='ignore')
			if a == '':
				# print(sum + '\n')
				recv_socket.close()
				break

		# print(type(sum))
		# print(sum.index('{'))
		# print(sum[sum.index('{'):])
		lists = eval(sum[sum.index('{'):])
		# print(lists)
		# return stockCode, lists["data"]["list"]
		print(stockCode, lists["data"]["list"])
	except:
		print("分时之巅连接失败")
		list_data(stockCode)


list_data("600600.SS")

# def ifzb(stockCode, lists, type):   # 判断是否缺数据和数据错误
#     date = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')[-4:]
#     if list[-1][0] != date:
#         text = type+":"+stockCode+"分时之巅延迟！！！当前时间："+datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H:%M:%S')[8:]+",最新数据："+ str(list[-1])
#         # print(text)
#         dd(text)
#     else:
#         print(type+":"+stockCode+"分时之巅在%s正常"% datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H:%M:%S')[8:])
#
#
# def fszd_run():
#     try:
#         item = [["01678.HK", "港股"], ["127011.SZ", "可转债"], ["600812.SS","A股"]]
#         for list1 in item:
#             data, code = list_data(list1[0])
#             ifzb(data,code,list1[1])
#         print('-------------------------------------------------')
#
#     except:
#         # for i in range(4):
#         #  s = "\r本次连接失败，正在重新连接 %s" % ("." * i)
#         #  # s="\r%d%% %s"%(i,"#"*i)   #\r表示回车但是不换行，利用这个原理进行百分比的刷新
#         #  sys.stdout.write(s)  # 向标准输出终端写内容
#         #  sys.stdout.flush()  # 立即将缓存的内容刷新到标准输出
#         #  time.sleep(0.7)  # 设置延迟查看效果
#         print("本次连接失败，正在重新连接中。。。")
#         fszd_run()
#
#
# def main():
#     scheduler = BlockingScheduler()  # 调度器
#     scheduler.add_job(fszd_run, 'interval', seconds=60)
#     scheduler.start()
#
# if __name__ == "__main__":
#     scheduler = BlockingScheduler()  # 调度器
# # 需要执行的方法（不要括号）    星期一到星期五        14:14:5启动
# scheduler.add_job(main, 'cron', day_of_week='1-5', hour=9, minute=30, second=30)
# scheduler.start()
# scheduler.shutdown()
#
# scheduler.add_job(fszd_run, 'interval', seconds=60)
# scheduler.start()
#
# fszd_run()
