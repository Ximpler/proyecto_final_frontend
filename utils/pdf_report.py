from fpdf import FPDF
import os

def generar_pdf(session_state):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, 'Informe de Estimación de Construcción', 0, 1, 'C')

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Camas: {session_state.beds}", 0, 1)
    pdf.cell(0, 10, f"Tamaño: {session_state.size} m²", 0, 1)
    pdf.cell(0, 10, f"Baños: {session_state.bathrooms}", 0, 1)
    pdf.cell(0, 10, f"Presupuesto estimado: ${session_state.presupuesto:,.2f}", 0, 1)

    # Crear una tabla de costos
    pdf.cell(0, 10, "Desglose de Costos:", 0, 1)
    pdf.set_font("Arial", size=10)

    # Columnas
    pdf.cell(60, 10, 'Componente', 1)
    pdf.cell(60, 10, 'Costo ($)', 1)
    pdf.ln()

    for index, row in session_state.df_costos.iterrows():
        pdf.cell(60, 10, row['Componentes'], 1)
        pdf.cell(60, 10, str(row['Costo ($)']), 1)
        pdf.ln()

    # Guardar el PDF en el directorio actual
    pdf_path = os.path.join("Informe_estimacion.pdf")
    pdf.output(pdf_path)

    return pdf_path
