from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, black, white

W, H = A4
OUT = "nota_corretagem_ficticia.pdf"

def br(v, d=2):
    s = f"{v:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

# ---------- dados fictícios ----------
ops = [
    # (C/V, mercado, ativo, obs, qtd, preço)
    ("C", "FRACIONARIO", "ALFAMED        ON", "D", 10, 12.40),
    ("V", "FRACIONARIO", "ALFAMED        ON", "D", 10, 12.55),
    ("C", "VISTA",       "BETACOM        ON  NM", "", 100, 8.20),
    ("C", "FRACIONARIO", "BETACOM        ON  NM", "", 37, 8.21),
    ("V", "FRACIONARIO", "GAMAPAR        ON", "", 25, 31.10),
    ("V", "VISTA",       "GAMAPAR        ON", "", 100, 31.05),
    ("C", "FRACIONARIO", "DELTAGRO       PN  N1", "D", 48, 4.76),
    ("V", "FRACIONARIO", "DELTAGRO       PN  N1", "D", 48, 4.81),
    ("C", "VISTA",       "ZETAENER       ON  NM", "", 200, 22.35),
    ("V", "FRACIONARIO", "ZETAENER       ON  NM", "", 14, 22.60),
    ("C", "FRACIONARIO", "INDEXA11       CI", "", 5, 112.30),
    ("V", "FRACIONARIO", "OMEGALOG       ON", "", 63, 6.90),
    ("C", "FRACIONARIO", "OMEGALOG       ON", "", 63, 6.84),
    ("V", "VISTA",       "KAPPATEC       PN  N2", "", 150, 15.72),
]
rows = []
for cv, mer, ativo, obs, q, p in ops:
    val = round(q * p, 2)
    rows.append((cv, mer, ativo, obs, q, p, val, "C" if cv == "V" else "D"))

compras = sum(r[6] for r in rows if r[0] == "C")
vendas = sum(r[6] for r in rows if r[0] == "V")
compras_vista = sum(r[6] for r in rows if r[0] == "C" and r[1] == "VISTA")
vendas_vista = sum(r[6] for r in rows if r[0] == "V" and r[1] == "VISTA")
tot_ops = compras + vendas
liq_ops = vendas - compras  # crédito se positivo
taxa_liq = round(tot_ops * 0.000275, 2)
taxa_reg = 0.00
total_cblc = taxa_liq + taxa_reg
emol = round(tot_ops * 0.000325, 2)
total_bov = emol
corretagem = 4.90
iss = round(corretagem * 0.05, 2)
total_corr = corretagem + iss
liquido = liq_ops - total_cblc - total_bov - total_corr

# ---------- desenho ----------
c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Nota de Corretagem (modelo fictício)")
c.setAuthor("Documento fictício para fins de estudo")
LM, RM = 28, W - 28
GRAY = Color(0.85, 0.85, 0.85)

def box(x1, y1, x2, y2, lw=0.6, fill=None):
    c.setLineWidth(lw)
    if fill is not None:
        c.setFillColor(fill)
        c.rect(x1, y1, x2 - x1, y2 - y1, stroke=1, fill=1)
        c.setFillColor(black)
    else:
        c.rect(x1, y1, x2 - x1, y2 - y1, stroke=1, fill=0)

def t(x, y, s, size=7, bold=False, align="l"):
    c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    if align == "r":
        c.drawRightString(x, y, s)
    elif align == "c":
        c.drawCentredString(x, y, s)
    else:
        c.drawString(x, y, s)

def label(x, y, s):
    t(x, y, s, 5, False)

# título
t(LM + 4, H - 30, "NOTA DE CORRETAGEM", 9, True)
t(W / 2, H - 30, "(documento fictício, sem valor fiscal)", 6.5, False, "c")

# nr nota / folha / data
bx = RM - 175
box(bx, H - 52, RM, H - 36)
label(bx + 3, H - 41, "Nr. nota"); label(bx + 80, H - 41, "Folha"); label(bx + 112, H - 41, "Data pregão")
t(bx + 38, H - 49, "000123", 8, False, "r"); t(bx + 98, H - 49, "1", 8, False, "r"); t(RM - 5, H - 49, "06/11/2026", 8, False, "r")

# cabeçalho corretora
box(LM, H - 118, RM, H - 58)
c.setFillColor(Color(0.1, 0.35, 0.6)); c.circle(LM + 28, H - 88, 17, stroke=0, fill=1); c.setFillColor(black)
t(LM + 55, H - 92, "exemplo", 17, True)
t(LM + 135, H - 72, "CORRETORA EXEMPLO S.A. - GRUPO MODELO", 7.5, True)
t(LM + 135, H - 82, "Av. Modelo de Teste, 1000 - 10º Andar - Bairro Fictício", 7)
t(LM + 135, H - 91, "Tel. 0000-0000   Fax: (00) -", 7)
t(LM + 135, H - 100, "Internet: www.corretora-exemplo.invalid  SAC: 0800-000-0000", 7)
t(LM + 135, H - 109, "C.N.P.J: 00.000.000/0001-00", 7)
t(LM + 135, H - 117 + 1, "Ouvidoria: Tel. 0800-000-0001", 7)
t(RM - 195, H - 72, "00000-000", 7)
t(RM - 4, H - 72, "CIDADE MODELO - UF", 7, False, "r")
t(RM - 195, H - 91, "e-mail: atendimento@corretora-exemplo.invalid", 7)
t(RM - 195, H - 100, "Carta Patente: 0000/0000", 7)
t(RM - 195, H - 109, "e-mail ouvidoria: ouvidoria@corretora-exemplo.invalid", 7)

# cliente
y0 = H - 124
box(LM, y0 - 50, RM, y0)
label(LM + 3, y0 - 6, "Cliente")
t(LM + 3, y0 - 16, "0000001", 7)
t(LM + 135, y0 - 16, "CLIENTE MODELO DA SILVA", 7.5, True)
t(LM + 135, y0 - 26, "RUA DOS TESTES, 123 APTO 45", 7)
t(LM + 135, y0 - 36, "00000-000 CIDADE MODELO - UF", 7)
t(LM + 300, y0 - 26, "Tel: (00) 90000-0000", 7)
box(RM - 135, y0 - 50, RM, y0)
label(RM - 132, y0 - 6, "C.P.F./C.N.P.J./C.V.M./C.O.B.")
t(RM - 132, y0 - 16, "000.000.000-00", 7)
label(RM - 132, y0 - 26, "Código cliente"); label(RM - 40, y0 - 26, "Assessor")
t(RM - 132, y0 - 36, "100-0   0000001", 7); t(RM - 8, y0 - 36, "0", 7, False, "r")

# linhas de campos
def campos(ytop, cols, vals):
    box(LM, ytop - 22, RM, ytop)
    for (x, lab), v in zip(cols, vals):
        c.line(x, ytop, x, ytop - 22) if x > LM else None
        label(x + 3, ytop - 6, lab)
        t(x + 3, ytop - 17, v, 7)

y1 = y0 - 54
campos(y1, [(LM, "Participante destino do repasse"), (LM + 255, "Cliente"), (LM + 330, "Valor"),
            (LM + 410, "Custodiante"), (RM - 28, "C.I.")], ["-0", "-", "0", "", "N"])
y2 = y1 - 22
campos(y2, [(LM, "Banco"), (LM + 40, "Agência"), (LM + 115, "Conta corrente"), (LM + 225, "Acionista"),
            (LM + 330, "Administrador"), (LM + 410, "Complemento nome"), (RM - 28, "P. Vinc")],
       ["000", "00000", "00000000", "", "", "", "N"])

# negócios realizados
yn = y2 - 48
t(LM + 4, yn + 12, "Negócios realizados", 7.5)
cols = {"Q": LM + 4, "Negociação": LM + 18, "C/V": LM + 94, "Tipo mercado": LM + 114, "Prazo": LM + 183,
        "Especificação do título": LM + 215, "Obs. (*)": LM + 300}
for k, x in cols.items():
    t(x, yn, k, 6.5, True)
t(395, yn, "Quantidade", 6.5, True, "r")
t(455, yn, "Preço / Ajuste", 6.5, True, "r")
t(545, yn, "Valor Operação / Ajuste", 6.5, True, "r")
t(RM - 4, yn, "D/C", 6.5, True, "r")
c.line(LM, yn - 3, RM, yn - 3)
yy = yn - 13
for i, (cv, mer, ativo, obs, q, p, val, dc) in enumerate(rows):
    if i % 2 == 0:
        c.setFillColor(Color(0.95, 0.95, 0.95)); c.rect(LM, yy - 2.5, RM - LM, 10.5, stroke=0, fill=1); c.setFillColor(black)
    t(cols["Negociação"], yy, "1-BOVESPA", 6.5)
    t(cols["C/V"] + 6, yy, cv, 6.5)
    t(cols["Tipo mercado"], yy, mer, 6.5)
    t(cols["Especificação do título"], yy, ativo, 6.5)
    t(cols["Obs. (*)"] + 8, yy, obs, 6.5)
    t(395, yy, str(q), 6.5, False, "r")
    t(455, yy, br(p), 6.5, False, "r")
    t(545, yy, br(val), 6.5, False, "r")
    t(RM - 4, yy, dc, 6.5, False, "r")
    yy -= 11

# quadros inferiores
top = 345
bot = 58
mid = LM + (RM - LM) / 2 + 1
box(LM, bot, mid, top)
box(mid, bot, RM, top)

# --- Resumo dos Negócios
box(LM, top - 11, mid, top, fill=None)
t(LM + 3, top - 8, "Resumo dos Negócios", 6.5, True)
resumo = [("Debêntures", 0.0), ("Vendas à vista", vendas_vista), ("Compras à vista", compras_vista),
          ("Opções - compras", 0.0), ("Opções - vendas", 0.0), ("Operações à termo", 0.0),
          ("Valor das oper. c/ títulos públ. (v. nom.)", 0.0), ("Valor das operações", tot_ops)]
ry = top - 22
for nome, v in resumo:
    t(LM + 3, ry, nome, 6.5)
    t(mid - 5, ry, br(v), 6.5, False, "r")
    ry -= 9.5

c.line(LM, ry + 2, mid, ry + 2)
box(LM, ry - 9, mid, ry + 2)
t(LM + 3, ry - 6, "Especificações diversas", 6.5, True)
t(LM + 3, ry - 40, "A coluna Q indica liquidação no Agente do Qualificado.", 6.5)

# --- Observações
oy = 205
c.line(LM, oy, mid, oy)
t(LM + 3, oy - 12, "(*) Observações", 7.5, True)
obs_l = ["2 - Corretora responsável vinculada/atuou na conta parte.", "# - Negócio direto", "8 - Liquidação Institucional",
         "D - Day Trade", "F - Cobertura", "B - Debêntures"]
obs_m = ["A - Posição futuro", "C - Clubes e fundos de Ações", "P - Carteira Própria", "H - Home Broker",
         "X - Box", "U - Desmanche de Box", "L - Precatório"]
obs_r = ["T - Liquidação pelo Bruto", "I - PGF"]
yo = oy - 22
for s in obs_l[:1]: t(LM + 3, yo, s, 4.5)
for i, s in enumerate(obs_l[1:]): t(LM + 3, yo - 17 - i * 17, s, 4.5)
for i, s in enumerate(obs_m): t(LM + 105, yo + 5 - i * 15, s, 4.5)
for i, s in enumerate(obs_r): t(LM + 195, yo + 5 - i * 15, s, 4.5)

# --- Resumo Financeiro
def sec(y, title):
    box(mid, y - 9, RM, y + 2, fill=None)
    t(mid + 3, y - 6, title, 6.5, True)

def line(y, nome, v=None, dc=None, bold=False):
    t(mid + 3, y, nome, 6.5, bold)
    if v is not None:
        t(RM - 22, y, br(v), 6.5, bold, "r")
    if dc:
        t(RM - 5, y, dc, 6.5, bold, "r")

fy = top - 8
t(mid + 3, fy, "Resumo Financeiro", 6.5, True)
sec(fy - 10, "Clearing")
fy -= 30
line(fy, "Valor líquido das operações", abs(liq_ops), "C" if liq_ops >= 0 else "D"); fy -= 9.5
line(fy, "Taxa de liquidação", taxa_liq, "D"); fy -= 9.5
line(fy, "Taxa de Registro", taxa_reg, "D"); fy -= 4
c.setFillColor(GRAY); c.rect(mid, fy - 8, RM - mid, 10, stroke=0, fill=1); c.setFillColor(black)
line(fy - 5, "Total CBLC", total_cblc, "D", True); fy -= 20
sec(fy + 7, "Bolsa")
fy -= 8
line(fy, "Taxa de termo/opções", 0.0, "D"); fy -= 9.5
line(fy, "Taxa A.N.A.", 0.0, "D"); fy -= 9.5
line(fy, "Emolumentos", emol, "D"); fy -= 4
c.setFillColor(GRAY); c.rect(mid, fy - 8, RM - mid, 10, stroke=0, fill=1); c.setFillColor(black)
line(fy - 5, "Total Bovespa / Soma", total_bov, "D", True)
t(RM - 90, fy - 5, "CONTINUA...", 6.5, False, "r")
fy -= 20
sec(fy + 7, "Corretagem / Despesas")
fy -= 8
line(fy, "Clearing", 0.0, None); fy -= 9.5
line(fy, "Execução", corretagem, None); fy -= 9.5
line(fy, "Execução casa", 0.0, None); fy -= 9.5
line(fy, "ISS (CIDADE MODELO)", iss, None); fy -= 9.5
line(fy, "I.R.R.F. s/ operações, base R$ 0,00", 0.0, None); fy -= 9.5
line(fy, "Outras Bovespa", 0.0, None)
ty = bot + 38
c.setFillColor(GRAY); c.rect(mid, ty - 3, RM - mid, 10, stroke=0, fill=1); c.setFillColor(black)
line(ty, "Total corretagem / Despesas", total_corr, "D", True)
c.line(mid, ty - 3, RM, ty - 3)
t(mid + 3, ty - 12, "Líquido para 08/11/2026", 6.5, True)
t(RM - 22, ty - 12, br(abs(liquido)), 6.5, True, "r")
t(RM - 5, ty - 12, "C" if liquido >= 0 else "D", 6.5, True, "r")
t(mid + 3, ty - 22, "Observação: (1) As operações a termo não são computadas no líquido da fatura.", 5.5)

# rodapé
t(LM + 4, 35, "Capitais e regiões metropolitanas: 0000-0000 Demais localidades: 0800-000-0000 SAC: 0800-000-0001 Ouvidoria: 0800-000-0002", 6)
t(LM + 4, 25, "Documento gerado com dados fictícios, exclusivamente para estudo e testes de análise de dados.", 6)

c.save()
print(f"compras={compras:.2f} vendas={vendas:.2f} liquido={liquido:.2f}")