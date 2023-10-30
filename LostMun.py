#!/usr/bin/python3
# -*- coding:utf-8 -*-
# version:1.0 

def Utils(inputstr):
	inputlist = inputstr.split(",")
	numlist = [int(x) for x in inputlist]	
	total_numlist = sum(numlist)
	len1 = len(numlist)

	sum1 = 0 
	for i in range(0,len1+1):
		sum1+=i;
	lostnum = sum1 - total_numlist
	if lostnum-1 == numlist[len1-1]:
		print("没有缺失数字")
	else:
		print("缺失的数字是："+str(lostnum))

if __name__ == '__main__':
	print("寻找消失的数字")
	print("请输入需要寻找的测试数组,以逗号隔开,输入实例：0,1,2,3,4,5,7 ") # 
	print("注意如果不是0缺少，就一定需要输入0")

	inputstr  = input("请输入：")
	Utils(inputstr)


