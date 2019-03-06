from random import randint
from matplotlib import pyplot as plt


class KalmanFilter():

    def __init__(self, init_val):
        self.est = init_val[0]
        self.est_err = init_val[1]
        self.msmt = init_val[2]
        self.msmt_err = init_val[3]

    def update(self, msmt_val):
        self.kalman_gain = self.est_err / (self.est_err + self. msmt_err)
        self.est = self.est + self.kalman_gain * (msmt_val - self.est)
        self.est_err = (1 - self.kalman_gain) * self.est_err

    def run(self):
        print('Msmt, Est_err, KG, Est')
        for i in range(len(self.msmt)):
            self.update(self.msmt[i])
            print(self.msmt[i], "{:.2f} {:.2f} {:.2f}".format(
                self.est_err, self.kalman_gain, self.est))
            estimates.append(self.est)


estimates = []
measurements = [75 + randint(-4, 4) for i in range(100)]
initial_estimate = randint(72, 76)
initial_error = 4
measurement_error = 2
kf = KalmanFilter((initial_estimate, initial_error, measurements, measurement_error))
kf.run()
plt.ylim(bottom=50, top=90)
plt.plot(measurements)
plt.plot(estimates)
plt.axhline(y=75, color='r', linestyle='-')
plt.plot(75)
plt.show()
