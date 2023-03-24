#!/usr/bin/python
# plot results

import matplotlib.pyplot as plt
import os

def create_figures():
	input_txt = os.getcwd() + '/data/joint_data.txt'
	f = open(input_txt)

	num = []
	q_des_1 = []; q_data_1 = []; qd_des_1 = []; qd_data_1 = []; tau_des_1 = []; tau_ff_1 = []; tau_data_1 = []
	q_des_2 = []; q_data_2 = []; qd_des_2 = []; qd_data_2 = []; tau_des_2 = []; tau_ff_2 = []; tau_data_2 = []
	q_des_3 = []; q_data_3 = []; qd_des_3 = []; qd_data_3 = []; tau_des_3 = []; tau_ff_3 = []; tau_data_3 = []
	q_des_4 = []; q_data_4 = []; qd_des_4 = []; qd_data_4 = []; tau_des_4 = []; tau_ff_4 = []; tau_data_4 = []
	q_des_5 = []; q_data_5 = []; qd_des_5 = []; qd_data_5 = []; tau_des_5 = []; tau_ff_5 = []; tau_data_5 = []
	q_des_6 = []; q_data_6 = []; qd_des_6 = []; qd_data_6 = []; tau_des_6 = []; tau_ff_6 = []; tau_data_6 = []

	# read from 2nd line
	for line in f.readlines()[2:]:
		line = line.strip('\n')
		line = line.split(' ')

		num.append(int(line[0]))

		q_des_1.append(float(line[1]))
		q_data_1.append(float(line[2]))
		qd_des_1.append(float(line[3]))
		qd_data_1.append(float(line[4]))
		tau_des_1.append(float(line[5]))
		tau_ff_1.append(float(line[6]))
		tau_data_1.append(float(line[7]))

		q_des_2.append(float(line[8]))
		q_data_2.append(float(line[9]))
		qd_des_2.append(float(line[10]))
		qd_data_2.append(float(line[11]))
		tau_des_2.append(float(line[12]))
		tau_ff_2.append(float(line[13]))
		tau_data_2.append(float(line[14]))

		q_des_3.append(float(line[15]))
		q_data_3.append(float(line[16]))
		qd_des_3.append(float(line[17]))
		qd_data_3.append(float(line[18]))
		tau_des_3.append(float(line[19]))
		tau_ff_3.append(float(line[20]))
		tau_data_3.append(float(line[21]))

		q_des_4.append(float(line[22]))
		q_data_4.append(float(line[23]))
		qd_des_4.append(float(line[24]))
		qd_data_4.append(float(line[25]))
		tau_des_4.append(float(line[26]))
		tau_ff_4.append(float(line[27]))
		tau_data_4.append(float(line[28]))

		q_des_5.append(float(line[29]))
		q_data_5.append(float(line[30]))
		qd_des_5.append(float(line[31]))
		qd_data_5.append(float(line[32]))
		tau_des_5.append(float(line[33]))
		tau_ff_5.append(float(line[34]))
		tau_data_5.append(float(line[35]))

		q_des_6.append(float(line[36]))
		q_data_6.append(float(line[37]))
		qd_des_6.append(float(line[38]))
		qd_data_6.append(float(line[39]))
		tau_des_6.append(float(line[40]))
		tau_ff_6.append(float(line[41]))
		tau_data_6.append(float(line[42]))

	# ---------------------------------------------------------
	fig1 = plt.figure(figsize = (8,6))

	# plot q_cmd & q_data of joint 1
	ax1 = plt.subplot(2,3,1)
	ax1.plot(num, q_des_1, color='blue', label='q_des_1')
	ax1.plot(num, q_data_1, color='green', label='q_data_1')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 1 Position (rad)')
	ax1.grid(True)
	ax1.legend(loc='upper right')

	# plot q_cmd & q_data of joint 2
	ax2 = plt.subplot(2,3,2)
	ax2.plot(num, q_des_2, color='blue', label='q_des_2')
	ax2.plot(num, q_data_2, color='green', label='q_data_2')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 2 Position (rad)')
	ax2.grid(True)
	ax2.legend(loc='upper right')

	# plot q_cmd & q_data of joint 3
	ax3 = plt.subplot(2,3,3)
	ax3.plot(num, q_des_3, color='blue', label='q_des_3')
	ax3.plot(num, q_data_3, color='green', label='q_data_3')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 3 Position (rad)')
	ax3.grid(True)
	ax3.legend(loc='upper right')

	# plot q_cmd & q_data of joint 4
	ax4 = plt.subplot(2,3,4)
	ax4.plot(num, q_des_4, color='blue', label='q_des_4')
	ax4.plot(num, q_data_4, color='green', label='q_data_4')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 4 Position (rad)')
	ax4.grid(True)
	ax4.legend(loc='upper right')

	# plot q_cmd & q_data of joint 5
	ax5 = plt.subplot(2,3,5)
	ax5.plot(num, q_des_5, color='blue', label='q_des_5')
	ax5.plot(num, q_data_5, color='green', label='q_data_5')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 5 Position (rad)')
	ax5.grid(True)
	ax5.legend(loc='upper right')

	# plot q_cmd & q_data of joint 6
	ax6 = plt.subplot(2,3,6)
	ax6.plot(num, q_des_6, color='blue', label='q_des_6')
	ax6.plot(num, q_data_6, color='green', label='q_data_6')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 6 Position (rad)')
	ax6.grid(True)
	ax6.legend(loc='upper right')

	# ---------------------------------------------------------
	fig2 = plt.figure(figsize = (8,6))

	# plot q_cmd & q_data of joint 1
	ax1 = plt.subplot(2,3,1)
	ax1.plot(num, qd_des_1, color='darkorange', label='qd_des_1')
	ax1.plot(num, qd_data_1, color='teal', label='qd_data_1')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 1 Velcoity (rad)')
	ax1.grid(True)
	ax1.legend(loc='upper right')

	# plot q_cmd & q_data of joint 2
	ax2 = plt.subplot(2,3,2)
	ax2.plot(num, qd_des_2, color='darkorange', label='qd_des_2')
	ax2.plot(num, qd_data_2, color='teal', label='qd_data_2')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 2 Velcoity (rad)')
	ax2.grid(True)
	ax2.legend(loc='upper right')

	# plot q_cmd & q_data of joint 3
	ax3 = plt.subplot(2,3,3)
	ax3.plot(num, qd_des_3, color='darkorange', label='qd_des_3')
	ax3.plot(num, qd_data_3, color='teal', label='qd_data_3')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 3 Velcoity (rad)')
	ax3.grid(True)
	ax3.legend(loc='upper right')

	# plot q_cmd & q_data of joint 4
	ax4 = plt.subplot(2,3,4)
	ax4.plot(num, qd_des_4, color='darkorange', label='qd_des_4')
	ax4.plot(num, qd_data_4, color='teal', label='qd_data_4')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 4 Velcoity (rad)')
	ax4.grid(True)
	ax4.legend(loc='upper right')

	# plot q_cmd & q_data of joint 5
	ax5 = plt.subplot(2,3,5)
	ax5.plot(num, qd_des_5, color='darkorange', label='qd_des_5')
	ax5.plot(num, qd_data_5, color='teal', label='qd_data_5')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 5 Velcoity (rad)')
	ax5.grid(True)
	ax5.legend(loc='upper right')

	# plot q_cmd & q_data of joint 6
	ax6 = plt.subplot(2,3,6)
	ax6.plot(num, qd_des_6, color='darkorange', label='qd_des_6')
	ax6.plot(num, qd_data_6, color='teal', label='qd_data_6')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 6 Velcoity (rad)')
	ax6.grid(True)
	ax6.legend(loc='upper right')
	
	# ---------------------------------------------------------
	fig3 = plt.figure(figsize = (8,6))

	# plot torque of joint 1
	ax1 = plt.subplot(2,3,1)
	ax1.plot(num, tau_des_1, color='red', label='tau_des_1')
	ax1.plot(num, tau_ff_1, color='blueviolet', label='tau_ff_1')
	# ax1.plot(num, tau_data_1, color='magenta', label='tau_data_1')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 1 Torque (N.m)')
	ax1.grid(True)
	ax1.legend(loc='upper right')

	# plot torque of joint 2
	ax2 = plt.subplot(2,3,2)
	ax2.plot(num, tau_des_2, color='red', label='tau_des_2')
	ax2.plot(num, tau_ff_2, color='blueviolet', label='tau_ff_2')
	# ax2.plot(num, tau_data_2, color='magenta', label='tau_data_2')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 2 Torque (N.m)')
	ax2.grid(True)
	ax2.legend(loc='upper right')

	# plot torque of joint 3
	ax3 = plt.subplot(2,3,3)
	ax3.plot(num, tau_des_3, color='red', label='tau_des_3')
	ax3.plot(num, tau_ff_3, color='blueviolet', label='tau_ff_3')
	# ax3.plot(num, tau_data_3, color='magenta', label='tau_data_3')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 3 Torque (N.m)')
	ax3.grid(True)
	ax3.legend(loc='upper right')

	# plot torque of joint 4
	ax4 = plt.subplot(2,3,4)
	ax4.plot(num, tau_des_4, color='red', label='tau_des_4')
	ax4.plot(num, tau_ff_4, color='blueviolet', label='tau_ff_4')
	# ax4.plot(num, tau_data_4, color='magenta', label='tau_data_4')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 4 Torque (N.m)')
	ax4.grid(True)
	ax4.legend(loc='upper right')

	# plot torque of joint 5
	ax5 = plt.subplot(2,3,5)
	ax5.plot(num, tau_des_5, color='red', label='tau_des_5')
	ax5.plot(num, tau_ff_5, color='blueviolet', label='tau_ff_5')
	# ax5.plot(num, tau_data_5, color='magenta', label='tau_data_5')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 5 Torque (N.m)')
	ax5.grid(True)
	ax5.legend(loc='upper right')

	# plot torque of joint 6
	ax6 = plt.subplot(2,3,6)
	ax6.plot(num, tau_des_6, color='red', label='tau_des_6')
	ax6.plot(num, tau_ff_6, color='blueviolet', label='tau_ff_6')
	# ax6.plot(num, tau_data_6, color='magenta', label='tau_data_6')
	plt.xlabel('time (ms)')
	plt.ylabel('Joint 6 Torque (N.m)')
	ax6.grid(True)
	ax6.legend(loc='upper right')

if __name__ == "__main__":
    create_figures()
    plt.show()
    # fig.savefig('data.png')
    # plt.close(fig)
