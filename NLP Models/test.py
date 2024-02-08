import torch,time

# Set the seed for reproducibility
torch.manual_seed(42)

# Generate a PyTorch tensor with random integers
random_tensor = torch.randint(low=1, high=50000, size=(1, 100))

# Print the generated tensor

print(random_tensor)

print('Decoding Tensor ... ... ... ')
time.sleep(5)
print('dEcoded o/p')

