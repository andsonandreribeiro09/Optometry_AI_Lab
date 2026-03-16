from reportlab.pdfgen import canvas

def generate_report(name,pd,myopia):

    file = f"{name}_report.pdf"

    c = canvas.Canvas(file)

    c.drawString(100,750,"Optometry AI Lab Report")

    c.drawString(100,700,f"Paciente: {name}")
    c.drawString(100,680,f"Distância Pupilar: {pd}")
    c.drawString(100,660,f"Miopia estimada: {myopia}")

    c.save()

    return file