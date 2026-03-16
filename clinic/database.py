import sqlite3

# clinic/database.py

# Exemplo simples: salvar dados de paciente em memória (lista)
patients = []

def save_patient(name, age=None, notes=None):
    """
    Salva informações básicas do paciente.
    name: str - nome do paciente
    age: int ou None - idade do paciente
    notes: str ou None - observações
    """
    patient = {
        "name": name,
        "age": age,
        "notes": notes
    }
    patients.append(patient)
    return patient

def get_patients():
    """
    Retorna a lista de pacientes cadastrados
    """
    return patients