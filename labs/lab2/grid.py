from distutils.file_util import move_file
from email import message
from operator import index
import numpy as np
import random

# Function to rotate the matrix
#  degree clockwise
from contextlib import nullcontext


def rotate_clockwise(M,n):
	#print("starting rotate_clockwise...")
	m_r = M.copy()
	for i in range(0,n):
		N = len(m_r[0])
		for i in range(N // 2):
			for j in range(i, N - i - 1):
				temp = m_r[i][j]
				m_r[i][j] = m_r[N - 1 - j][i]
				m_r[N - 1 - j][i] = m_r[N - 1 - i][N - 1 - j]
				m_r[N - 1 - i][N - 1 - j] = m_r[j][N - 1 - i]
				m_r[j][N - 1 - i] = temp
	return m_r

def find_net(k,m):
	#print("starting find_net...")
	m_net = m.copy()
	rand_index = random.randint(0,3)
	index_arr = np.array([],dtype=np.int64)
	for n in range(1,k**2+1):
		flag = 0
		occurance = 0
		for i in range(len(m_net[0])):
			for j in range(len(m_net[0])):
				if (m_net[i,j] == n):
					if (occurance == rand_index):
						index_arr = np.append([i,j],index_arr)
						flag = 1
						break
					occurance +=1
			if flag == 1:
				break
	index_arr = index_arr.reshape(k**2,2)
	index_arr = index_arr[np.lexsort(index_arr.T[::-1])]
	return index_arr

def rotate_index(index_arr,k):
	#print("starting rotate_index...")
	arr = index_arr.copy()
	arr = (np.flip(arr))
	new_index = np.array([],dtype=np.int64)
	N = k**2
	for n in range(k**2):
		j,i = arr[n]
		temp = i
		i = j
		j = N - temp - 1
		new_index = np.append(new_index,[i,j])
	new_index = new_index.reshape(k**2,2)
	new_index = new_index[np.lexsort(new_index.T[::-1])]
	return new_index

def encrypt(k,msg):
	print("encrypting...")
	m = np.arange(1,(k**2)+1)
	m = m.reshape(k,k)
	m_upper = np.hstack((m,rotate_clockwise(m,1)))
	m_bottom = np.hstack((rotate_clockwise(m,3),rotate_clockwise(m,2)))
	m_final = np.vstack((m_upper,m_bottom))
	index_arr = find_net(k,m_final)
	
	msg = list(msg)
	
	arr = [[]]
	for q in range(k**2-1):
		arr.append([])

	count = 0
	for char in msg:
		if char == ' ':
			continue
		if count == k**2:
			index_arr = rotate_index(index_arr,k)
			count = 0
		i,j = index_arr[count]
		count += 1
		arr[i].insert(j,char)
	final_code = ""
	for i in range(len(arr)):
		for j in range(len(arr)):
			final_code = final_code + arr[i][j]
	print("Encoded message: ",final_code)
		

msg = input("введите сообщение:", )
size = 2
count = 0
for char in msg:
		if char == ' ':
			continue
		count+=1
while(count > ((2*size)*(2*size))):
	size+=1

encrypt(size,msg)	