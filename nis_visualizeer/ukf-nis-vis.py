import matplotlib.pyplot as plt

"""
A chi square (X2) statistic is used to investigate whether distributions
of categorical variables differ from one another. Here we consider 3 degrees
of freedom for our system. Plotted against 95% line"""

lidar_nis = []
with open('NISvals_laser.txt') as f:
    for line in f:
        lidar_nis.append(line.strip())

print("Number of LIDAR Measurements :\t", len(lidar_nis))

radar_nis = []
with open('NISvals_radar.txt') as f:
    for line in f:
        radar_nis.append(line.strip())

print("Number of RADAR Measurements :\t", len(radar_nis))

k = [7.815 for x in range(len(lidar_nis))]

# We skip the first row to cut out the unrealistically high NIS value 
# from the first measurement.  The Kalman filter has not found its groove yet.

lidar_nis = lidar_nis[1:]
radar_nis = radar_nis[1:]

plt.plot(lidar_nis)
plt.plot(k)
plt.title("LIDAR NIS")
plt.xlabel("Measurement Instance")
plt.ylabel("NIS")
plt.show()

plt.plot(radar_nis)
plt.plot(k)
plt.title("RADAR NIS")
plt.xlabel("Measurement Instance")
plt.ylabel("NIS")
plt.ylim(0, 20)
plt.show()
