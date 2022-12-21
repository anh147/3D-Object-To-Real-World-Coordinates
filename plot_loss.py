# importing two required module
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches

A = [1, 2, 3, 4 ,5,6,7,8,9,10]
#image 5
measure = np.array([[30.4, 7.4], [29.8, 7.1], [19.6,10.5], [29.4,5.8], [27.6,8.5], [27,11.8], [26.3,10.4], [23.1,5.7]])
predict = np.array([[30.472, 6.97], [29.87, 6.86], [19.63,9.93], [29.59,5.33], [27.72,8.16], [27.17, 11.54], [26.29, 10.14], [22.91, 5.15]])

#image 6
measure6 = np.array([[6.7, 7.5], [9.45,9.35], [14.4,10], [6.8, 4.45], [18.6, 8.1], [8.55,3.65], [20.7,11.1], [24.3,6.2], [16, 4.9], [20.05, 3.9]])
predict6 = np.array([[6.73, 7.45],[9.54, 9.3],[14.46, 9.9],[6.84, 4.35],[18.62, 8.02],[8.61, 3.72],[20.8, 11.1],[24.41, 6.07],[16.09, 4.8],[20.07,3.8]])
print(np.shape(measure))

#image3D
measure3D = np.array([[29.8, 7.2], [27.1, 14], [23.2, 4.1], [24.8, 14.4], [23.8, 8.9], [22.2, 9.1], [17.5, 9], [30.55, 3.9]])
predict3D = np.array([[29.77, 7.08], [27.27, 13.42] , [23.48, 4.1], [25.06, 14.02], [24.15, 8.73], [22.62, 9.08], [17.55, 8.97], [30.45, 4.07]])

# plt.scatter(measure6[:,0], measure6[:,1], color = 'black')


# # Plotting point using scatter method
# plt.scatter(predict6[:,0], predict6[:,1], color='red')

# for i_x, i_y in zip(measure3D[:,0], measure3D[:,1]):
#     plt.text(i_x +0.2, i_y +0.7, '({}, {})'.format(i_x, i_y))

# for i_x, i_y in zip(predict3D[:,0], predict3D[:,1]):
#     plt.text(i_x +0.2, i_y+0.1, '({}, {})'.format(i_x, i_y),  color='red')

# plt.text(1,10, 'Red: Dự đoán',  color='red')
# plt.text(1,9.2, 'Black: Đo',  color='black')
# plt.text(1,8.4, 'Green: Lỗi',  color='green')
# # Create a Rectangle patch
# rect = patches.Rectangle((2.5, 10), 2, 2, linewidth=1, edgecolor='r', facecolor='none')

# plt.scatter(abs(measure6[:,0]-predict6[:,0]), abs(measure6[:,1]-predict6[:,1]), color='green')
# plt.text(0.2,0.12, 'Green: Lỗi',  color='green')
# for i_x, i_y in zip(abs(measure3D[:,0]-predict3D[:,0]), abs(measure3D[:,1]-predict3D[:,1])):
#     plt.text(np.round(i_x,2) , np.round(i_y,2), '({}, {})'.format(np.round(i_x,2), np.round(i_y,2)),  color='green')


# Sai số trên trục x
plt.scatter(A,abs(measure6[:,0]-predict6[:,0]),  color='red')
for i_x, i_y in zip(abs(measure6[:,0]-predict6[:,0]), A):
    plt.text(np.round(i_y,2)+0.1 , np.round(i_x,2), '{}'.format(np.round(i_x,2)),  color='red')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Sai số theo trục x với 10 mẫu 2D (cm)",fontsize=15)
plt.show()
    
