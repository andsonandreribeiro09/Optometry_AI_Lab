# ai_models/myopia_model.py

import torch
import torch.nn as nn

# -----------------------------
# REDE NEURAL PARA MIOPIA
# -----------------------------
class MyopiaNet(nn.Module):
    def __init__(self):
        super().__init__()
        # Modelo simples com 3 camadas densas
        self.model = nn.Sequential(
            nn.Linear(10, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1)  # saída contínua
        )

    def forward(self, x):
        return self.model(x)


# -----------------------------
# FUNÇÃO DE PREDIÇÃO
# -----------------------------
def predict_myopia(input_list):
    """
    input_list: lista ou array com 10 valores numéricos (características do paciente)
    Retorna: valor previsto de miopia
    """
    # Garantir tipo tensor
    input_tensor = torch.tensor(input_list, dtype=torch.float32).unsqueeze(0)  # batch 1
    # Inicializar modelo
    model = MyopiaNet()
    model.eval()
    # Rodar predição
    with torch.no_grad():
        output = model(input_tensor)
    return output.item()