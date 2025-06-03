import statistics

data = [50,40,30,20,10,10]

def calc_variance(data):
	mean_v = sum(data) / len(data)
	var_value = sum((x - mean_v)**2 for x in data) / (len(data) -1)
	st_value = var_value ** 0.5
	print(f"{st_value}")
calc_variance(data)

def calc_variance(data):
	mean_v = sum(data) / len(data)
	var_value = sum((x - mean_v)**2 for x in data) / (len(data) -1)
	print(f"{var_value}")
calc_variance(data)

def calc_mode(data):
	return print(f"{statistics.mode(data)}")
calc_mode(data)

def calc_median(data):
	sorted_data = sorted(data)
	n = len(sorted_data)
	median1 = sorted_data[n//2 - 1]
	median2 = sorted_data[n//2]
	if n % 2 == 0:
		median_value = (median1+median2) / 2
	else:
		median_value = median2
	print(f"{median_value}")
calc_median(data)


def calc_mean(data):
	mean_value = sum(data)/len(data)
	print(f"{mean_value}")
calc_mean(data)