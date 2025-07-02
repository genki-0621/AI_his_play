import torch
import torch.nn as nn
import torch.optim as optim

# XORデータ + 手動カーネル特徴量（x1*x2）
X = torch.tensor([[0., 0., 0.],
                  [0., 1., 0.],
                  [1., 0., 0.],
                  [1., 1., 1.]])
y = torch.tensor([[0.],
                  [1.],
                  [1.],
                  [0.]])

class Perceptron(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(3, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))

model = Perceptron()
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(5000):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

with torch.no_grad():
    pred = torch.round(model(X))
    print(pred)

