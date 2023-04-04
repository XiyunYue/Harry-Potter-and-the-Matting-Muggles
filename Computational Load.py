import time

def my_function (Bayessian_matte1):
    # do some computational task here
    output = Bayessian_matte1 * 2
    return output

start_time = time.time()

# call the function with some input
result = my_function(5)

end_time = time.time()

# calculate the time taken to execute the function
time_taken = end_time - start_time

print(f"Time taken: {time_taken} seconds")



