import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

# Fonction de calcul du net à payer et des cotisations
def calcul_paie(salaire_brut, cotisation_salariale, cotisation_patronale, primes):
    total_brut = salaire_brut + primes
    retenue_salariale = total_brut * cotisation_salariale / 100
    charges_patronales = total_brut * cotisation_patronale / 100
    salaire_net = total_brut - retenue_salariale
    return total_brut, retenue_salariale, charges_patronales, salaire_net

# Fonction pour générer le bulletin de paie en PDF
def generer_bulletin(nom, prenom, mois, salaire_brut, primes, cot_salariale, cot_patronale, pdf_file):
    total_brut, retenue_salariale, charges_patronales, salaire_net = calcul_paie(
        salaire_brut, cot_salariale, cot_patronale, primes)
    
    c = canvas.Canvas(pdf_file, pagesize=A4)
    largeur, hauteur = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, hauteur - 50, "Bulletin de Paie Simplifié")

    c.setFont("Helvetica", 12)
    c.drawString(50, hauteur - 100, f"Salarié : {prenom} {nom}")
    c.drawString(50, hauteur - 120, f"Période : {mois}")

    c.drawString(50, hauteur - 160, f"Salaire de base : {salaire_brut:.2f} €")
    c.drawString(50, hauteur - 180, f"Primes : {primes:.2f} €")
    c.drawString(50, hauteur - 200, f"Total brut : {total_brut:.2f} €")
    c.drawString(50, hauteur - 220, f"Retenues salariales ({cot_salariale}%): {retenue_salariale:.2f} €")
    c.drawString(50, hauteur - 240, f"Charges patronales ({cot_patronale}%): {charges_patronales:.2f} €")
    c.drawString(50, hauteur - 260, f"Salaire net à payer : {salaire_net:.2f} €")

    c.line(50, hauteur - 270, 550, hauteur - 270)

    c.save()

# Streamlit app
st.title("📝 Générateur de Bulletin de Paie (France)")

with st.form("formulaire_paie"):
    col1, col2 = st.columns(2)
    with col1:
        nom = st.text_input("Nom du salarié", "Dupont")
        prenom = st.text_input("Prénom du salarié", "Jean")
        mois = st.text_input("Période (mois)", "Juin 2025")
    with col2:
        salaire_brut = st.number_input("Salaire de base (€)", value=2000.00, step=10.0)
        primes = st.number_input("Primes (€)", value=200.00, step=10.0)

    cot_salariale = st.number_input("Taux de cotisation salariale (%)", value=22.0, step=0.1)
    cot_patronale = st.number_input("Taux de cotisation patronale (%)", value=42.0, step=0.1)

    submitted = st.form_submit_button("Générer le bulletin de paie")

if submitted:
    pdf_buffer = BytesIO()
    generer_bulletin(nom, prenom, mois, salaire_brut, primes, cot_salariale, cot_patronale, pdf_buffer)
    st.success("✅ Bulletin de paie généré avec succès !")

    st.download_button(
        label="📥 Télécharger le bulletin de paie",
        data=pdf_buffer.getvalue(),
        file_name=f"Bulletin_de_paie_{nom}_{mois}.pdf",
        mime="application/pdf"
    )
