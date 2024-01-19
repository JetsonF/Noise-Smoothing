import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility (optional)
np.random.seed(1)

# Adjust height and width as required
width = 50
height = 50
volume = height * width

# Generate random noise (you can adjust the size as needed)
noise_size = (height, width)
random_noise = np.random.normal(0, 1, noise_size)

# Save each value in a 1D array sequentially
sequential_values = random_noise.flatten()
sequential_values = sequential_values[:volume]

# Create empty arrays to hold future values
smoothed_values = np.empty(volume)
temp_values = np.empty(volume)

# Fill empty values with existing values
for i in range(volume):
   temp_values[i] = sequential_values[i]

# Iterations of smoothings (larger plots require more smoothing)
smoothings = 12

# Average values for each point with all neighbors, careful to exclude non-present neighbors
def smooth(iterations):
    for n in range(iterations):
        for i in range(volume):
            if i==0: # Top left corner
                smoothed_values[i] = (temp_values[i] + temp_values[i+1] + temp_values[i+width])/3
            elif i==(width-1): # Top right corner
                smoothed_values[i] = (temp_values[i] + temp_values[i-1] + temp_values[i+width])/3
            elif i==(volume-width): # Bottom left corner
                smoothed_values[i] = (temp_values[i] + temp_values[i+1] + temp_values[i-width])/3
            elif i==(volume-1): # Bottom right corner
                smoothed_values[i] = (temp_values[i] + temp_values[i-1] + temp_values[i-width])/3
            elif i<=(width-1): # Top edge
                smoothed_values[i] = (temp_values[i] + temp_values[i+1] + temp_values[i-1] + temp_values[i+width])/4
            elif i>=(volume-width): # Bottom edge
                    smoothed_values[i] = (temp_values[i] + temp_values[i+1] + temp_values[i-1] + temp_values[i-width])/4
            elif i%width==0: # Left edge
                smoothed_values[i] = (temp_values[i] + temp_values[i+1] + temp_values[i-width] + temp_values[i+width])/4
            elif (i+1)%width==0: # Right edge
                smoothed_values[i] = (temp_values[i] + temp_values[i-1] + temp_values[i-width] + temp_values[i+width])/4
            else:
                smoothed_values[i] = (temp_values[i] + temp_values[i+1] + temp_values[i-1] + temp_values[i-width] + temp_values[i+width])/5

        # Resets smoothed values for further iterations        
        for m in range(volume):
            temp_values[m] = smoothed_values[m]
    
# Run code
smooth(smoothings)

smoothed_grid = smoothed_values.reshape((width, height))


plt.imshow(smoothed_grid, cmap='terrain') # Cool colors = 'magma', 'tab20b', 'terrain', 'twilight', 
# Display the random noise (optional)
# plt.imshow(random_noise, cmap='gray')
plt.title('Smoothed Random Noise')
plt.colorbar()
plt.show()

