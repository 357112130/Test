# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.six import BytesIO
from MyQR import myqr
from django.http import HttpResponse
from django.shortcuts import render
import os
import random


# Create your views here.
def home(request):
	return render(request, "index.html")


def generate_Image(request):
	# 获取上传的地址
	website = request.POST.get("website", None)
	# 请求方法为POST时进行处理
	if request.method == "POST":
		# 获取上传的文件,若没有文件默认None
		File = request.FILES.get("myfile", None)
		if File is None:
			return HttpResponse("没有需要上传的文件")
		else:
			# 打开特定的文件进行二进制的写操作
			# print(os.path.exists('temp_file/'))
			with open("./%s" % File.name, "wb+") as f:
				# 分块写入文件
				for chunk in File.chunks():
					f.write(chunk)
				version, level, qr_name = myqr.run(
					words=website,  # 可以是字符串,也可以是网址(前面需要加http(s)://)
					version=1,  # 设置容错率为最高
					level='H',  # 控制纠错水平,范围是L、M、Q、H,从左到右依次升高
					picture="./%s",  # 将二维码和图片合成
					colorized=True,  # 彩色二维码
					contrast=1.0,  # 用以调节图片的对比度,1.0表示原始图片,更小的值表示更低的对比度,更大反之,默认为1.0
					brightness=1.0,  # 用来调节图片的亮度,其余用法和取值同上
					save_name="./%s" % "s" + File.name,  # 保存文件的名字,格式可以是jpg,png,bmp,gif
					save_dir=os.getcwd()  # 控制位置
				)
				return HttpResponse(File.name)
