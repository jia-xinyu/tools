#!/usr/bin/python
# plot results

import matplotlib.pyplot as plt
import os
import numpy as np

def create_figures():
	input_csv = os.getcwd() + '/data/ctrl_data.csv'
	with open(input_csv) as file:
		rows = np.loadtxt(file, dtype=str, delimiter='\t')

		num = []
		q_des_1 = []; q_data_1 = []; qd_des_1 = []; qd_data_1 = []; tau_des_1 = []; qd_hat_1 = []; disturb_1 = []; k_SMC_1 = []; q_error_1 = []
		q_des_2 = []; q_data_2 = []; qd_des_2 = []; qd_data_2 = []; tau_des_2 = []; qd_hat_2 = []; disturb_2 = []; k_SMC_2 = []; q_error_2 = []
		q_des_3 = []; q_data_3 = []; qd_des_3 = []; qd_data_3 = []; tau_des_3 = []; qd_hat_3 = []; disturb_3 = []; k_SMC_3 = []; q_error_3 = []
		q_des_4 = []; q_data_4 = []; qd_des_4 = []; qd_data_4 = []; tau_des_4 = []; qd_hat_4 = []; disturb_4 = []; k_SMC_4 = []; q_error_4 = []
		q_des_5 = []; q_data_5 = []; qd_des_5 = []; qd_data_5 = []; tau_des_5 = []; qd_hat_5 = []; disturb_5 = []; k_SMC_5 = []; q_error_5 = []
		q_des_6 = []; q_data_6 = []; qd_des_6 = []; qd_data_6 = []; tau_des_6 = []; qd_hat_6 = []; disturb_6 = []; k_SMC_6 = []; q_error_6 = []

		for row in rows:
			num.append(float(row[0]))

			q_des_2.append(float(row[2]))
			q_data_2.append(float(row[2 +6]))
			qd_des_2.append(float(row[2 +6*2]))
			qd_data_2.append(float(row[2 +6*3]))
			tau_des_2.append(float(row[2 +6*4]))
			qd_hat_2.append(float(row[2 +6*5]))
			disturb_2.append(float(row[2 +6*6]))
			k_SMC_2.append(float(row[2 +6*7]))

			q_des_3.append(float(row[3]))
			q_data_3.append(float(row[3 +6]))
			qd_des_3.append(float(row[3 +6*2]))
			qd_data_3.append(float(row[3 +6*3]))
			tau_des_3.append(float(row[3 +6*4]))
			qd_hat_3.append(float(row[3 +6*5]))
			disturb_3.append(float(row[3 +6*6]))
			k_SMC_3.append(float(row[3 +6*7]))

			q_des_5.append(float(row[5]))
			q_data_5.append(float(row[5 +6]))
			qd_des_5.append(float(row[5 +6*2]))
			qd_data_5.append(float(row[5 +6*3]))
			tau_des_5.append(float(row[5 +6*4]))
			qd_hat_5.append(float(row[5 +6*5]))
			disturb_5.append(float(row[5 +6*6]))
			k_SMC_5.append(float(row[5 +6*7]))

	# list -> arrary
	q_error_2 = np.array(q_des_2) - np.array(q_data_2)
	q_error_3 = np.array(q_des_3) - np.array(q_data_3)
	q_error_5 = np.array(q_des_5) - np.array(q_data_5)

	fig1 = plt.figure(figsize = (8,9))

	# ------------------------- Joint 2 -------------------------
	# plot q_cmd & q_data of joint 2
	ax1 = plt.subplot(3,3,1)
	ax1.plot(num, q_des_2, color='blue', label='q_des_2')
	ax1.plot(num, q_data_2, color='green', label='q_data_2')
	ax1.plot(num, tau_des_2, color='red', label='tau_des_2')
	ax1.plot(num, disturb_2, color='pink', label='disturb_2')
	plt.xlabel('time (s)')
	plt.ylabel('pos (rad) / torque (N.m)')
	ax1.grid(True)
	ax1.legend(loc='upper right')

	# plot q_error of joint 2
	ax2 = plt.subplot(3,3,2)
	ax2.plot(num, q_error_2, color='blue', label='q_error_2')
	plt.xlabel('time (s)')
	plt.ylabel('pos error (rad)')
	ax2.grid(True)
	ax2.legend(loc='upper right')

	# plot control gain of joint 2
	ax3 = plt.subplot(3,3,3)
	ax3.plot(num, k_SMC_2, color='blue', label='k_SMC_2')
	plt.xlabel('time (s)')
	plt.ylabel('control gain')
	ax3.grid(True)
	ax3.legend(loc='upper right')

	# ------------------------- Joint 3 -------------------------
	# plot q_cmd & q_data of joint 3
	ax4 = plt.subplot(3,3,4)
	ax4.plot(num, q_des_3, color='blue', label='q_des_3')
	ax4.plot(num, q_data_3, color='green', label='q_data_3')
	ax4.plot(num, tau_des_3, color='red', label='tau_des_3')
	ax4.plot(num, disturb_3, color='pink', label='disturb_3')
	plt.xlabel('time (s)')
	plt.ylabel('pos (rad) / torque (N.m)')
	ax4.grid(True)
	ax4.legend(loc='upper right')

	# plot q_error of joint 3
	ax5 = plt.subplot(3,3,5)
	ax5.plot(num, q_error_3, color='blue', label='q_error_3')
	plt.xlabel('time (s)')
	plt.ylabel('pos error (rad)')
	ax5.grid(True)
	ax5.legend(loc='upper right')

	# plot control gain of joint 3
	ax6 = plt.subplot(3,3,6)
	ax6.plot(num, k_SMC_3, color='blue', label='k_SMC_3')
	plt.xlabel('time (s)')
	plt.ylabel('control gain')
	ax6.grid(True)
	ax6.legend(loc='upper right')

	# ------------------------- Joint 5 -------------------------
	# plot q_cmd & q_data of joint 5
	ax7 = plt.subplot(3,3,7)
	ax7.plot(num, q_des_5, color='blue', label='q_des_5')
	ax7.plot(num, q_data_5, color='green', label='q_data_5')
	ax7.plot(num, tau_des_5, color='red', label='tau_des_5')
	ax7.plot(num, disturb_5, color='pink', label='disturb_5')
	plt.xlabel('time (s)')
	plt.ylabel('pos (rad) / torque (N.m)')
	ax7.grid(True)
	ax7.legend(loc='upper right')

	# plot q_error of joint 5
	ax8 = plt.subplot(3,3,8)
	ax8.plot(num, q_error_5, color='blue', label='q_error_5')
	plt.xlabel('time (s)')
	plt.ylabel('pos error (rad)')
	ax8.grid(True)
	ax8.legend(loc='upper right')

	# plot control gain of joint 5
	ax9 = plt.subplot(3,3,9)
	ax9.plot(num, k_SMC_5, color='blue', label='k_SMC_5')
	plt.xlabel('time (s)')
	plt.ylabel('control gain')
	ax9.grid(True)
	ax9.legend(loc='upper right')


	# ---------------------- Levant Observer ----------------------
	'''
	# list -> arrary
	qd_error_2 = np.array(qd_hat_2) - np.array(qd_data_2)
	qd_error_3 = np.array(qd_hat_3) - np.array(qd_data_3)
	qd_error_5 = np.array(qd_hat_5) - np.array(qd_data_5)

	fig2 = plt.figure(figsize = (8,9))

	# plot qd_cmd, qd_data, qd_hat of joint 2
	ax1 = plt.subplot(3,2,1)
	ax1.plot(num, qd_des_2, color='blue', label='qd_des_2')
	ax1.plot(num, qd_data_2, color='green', label='qd_data_2')
	ax1.plot(num, qd_hat_2, color='pink', label='qd_hat_2')
	plt.xlabel('time (s)')
	plt.ylabel('vel (rad/s)')
	ax1.grid(True)
	ax1.legend(loc='upper right')

	# plot qd_error of joint 2
	ax2 = plt.subplot(3,2,2)
	ax2.plot(num, qd_error_2, color='blue', label='qd_error_2')
	plt.xlabel('time (s)')
	plt.ylabel('vel error (rad/s)')
	ax2.grid(True)
	ax2.legend(loc='upper right')

	# plot qd_cmd, qd_data, qd_hat of joint 3
	ax3 = plt.subplot(3,2,3)
	ax3.plot(num, qd_des_3, color='blue', label='qd_des_3')
	ax3.plot(num, qd_data_3, color='green', label='qd_data_3')
	ax3.plot(num, qd_hat_3, color='pink', label='qd_hat_3')
	plt.xlabel('time (s)')
	plt.ylabel('vel (rad/s)')
	ax3.grid(True)
	ax3.legend(loc='upper right')

	# plot qd_error of joint 3
	ax4 = plt.subplot(3,2,4)
	ax4.plot(num, qd_error_3, color='blue', label='qd_error_3')
	plt.xlabel('time (s)')
	plt.ylabel('vel error (rad/s)')
	ax4.grid(True)
	ax4.legend(loc='upper right')

	# plot qd_cmd, qd_data, qd_hat of joint 5
	ax5 = plt.subplot(3,2,5)
	ax5.plot(num, qd_des_5, color='blue', label='qd_des_5')
	ax5.plot(num, qd_data_5, color='green', label='qd_data_5')
	ax5.plot(num, qd_hat_5, color='pink', label='qd_hat_5')
	plt.xlabel('time (s)')
	plt.ylabel('vel (rad/s)')
	ax5.grid(True)
	ax5.legend(loc='upper right')

	# plot qd_error of joint 5
	ax6 = plt.subplot(3,2,6)
	ax6.plot(num, qd_error_5, color='blue', label='qd_error_5')
	plt.xlabel('time (s)')
	plt.ylabel('vel error (rad/s)')
	ax6.grid(True)
	ax6.legend(loc='upper right')
	'''


if __name__ == "__main__":
    create_figures()
    plt.show()
    # fig.savefig('data.png')
    # plt.close(fig)
