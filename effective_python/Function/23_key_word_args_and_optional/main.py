def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_parameters(alpha=1.5, beta=9, gamma=4)

#  optional paramter
#  period is optional.
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

weight_diff, time_diff = 100, 50
print(flow_rate(weight_diff, time_diff))