clicks3 = np.array([29.2,24.9,15.5,26.9,27.3,19,13.8,18.1,15.7,19,25.3,22.5,12,29.7,15.8])

print('The 25th percentile of the click data is: ', get_quants(clicks3)[0])
print('The 50th percentile of the click data is: ', get_quants(clicks3)[1])
print('The 75th percentile of the click data is: ', get_quants(clicks3)[2])
print('The 95th percentile of the click data is: ', get_quants(clicks3)[3])
print('The mode of the click data is: ', get_quants(clicks3)[4])
