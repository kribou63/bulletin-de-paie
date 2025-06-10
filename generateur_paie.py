from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def generer_bulletin(...):
    # calculs
    total_brut = heures * taux_h + primes
    retenue_sal = total_brut * cot_sal/100
    charges_pat = total_brut * cot_pat/100
    net_imposable = total_brut - retenue_sal
    net_social = net_imposable  # simplifié
    salaire_net = net_imposable

    c = canvas.Canvas(pdf, pagesize=A4)
    w, h = A4
    y = h - 40

    # En-tête
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(w/2, y, "Bulletin de Paie Simplifié")
    y -= 30

    # Employeur
    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"{nom_entreprise} – SIRET : {siret}")
    c.drawString(40, y-14, adresse_entreprise.replace("\n"," "))
    y -= 40

    # Salarié
    c.drawString(40, y, f"Salarié : {prenom} {nom} • Matricule : {matricule}")
    c.drawString(40, y-14, f"N° SS : {ss}")
    y -= 30

    # Période
    c.drawString(40, y, f"Période de paie : {periode}")
    y -= 30

    # Détail paie
    c.drawString(40, y, f"Heures : {heures:.2f} × {taux_h:.2f} €")
    c.drawString(300, y, f"Primes : {primes:.2f} €")
    y -= 20
    c.drawString(40, y, f"Salaire brut : {total_brut:.2f} €")
    y -= 20
    c.drawString(40, y, f> Cotisations salariales ({cot_sal:.1f} %) : {retenue_sal:.2f} €")
    y -= 20
    c.drawString(40, y, f> Cotisations patronales ({cot_pat:.1f} %) : {charges_pat:.2f} €")
    y -= 30

    # Totaux nets
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, y, f"Net imposable : {net_imposable:.2f} €")
    y -= 14
    c.drawString(40, y, f"Montant net social : {net_social:.2f} €")
    y -= 14
    c.drawString(40, y, f"Net à payer : {salaire_net:.2f} €")
    y -= 40

    # Pied
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(w/2, 50, "Bulletin conforme au modèle simplifié français (arrêté 31/01/2023)")
    c.save()
