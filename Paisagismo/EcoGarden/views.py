from django.shortcuts import render, redirect

def inspiracoes(request):
    return render(request, 'inspiracoes.html')
    
def home(request):
    return render(request, 'home.html', {"Servicos": SERVICOS})

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        retorno = nome
        return render(request, 'contato.html', {'retorno': retorno})
    return render(request, 'contato.html', {})

SERVICOS = [
    {"nome": "Paisagismo Sustentável", "descricao": "Planejamento e criação de jardins com espécies nativas e de baixa manutenção.", "preco": 1500.0},
    {"nome": "Irrigação Eficiente", "descricao": "Instalação de sistemas de irrigação por gotejamento que reduzem o consumo de água.", "preco": 800.0},
    {"nome": "Compostagem Doméstica", "descricao": "Implantação de composteiras para reciclagem de resíduos orgânicos em adubo natural.", "preco": 450.0},
    {"nome": "Telhado Verde", "descricao": "Instalação de cobertura verde para melhorar o isolamento térmico e reduzir a poluição.", "preco": 3000.0},
    {"nome": "Horta Orgânica", "descricao": "Montagem de hortas caseiras com técnicas agroecológicas.", "preco": 900.0},
    {"nome": "Captação de Água da Chuva", "descricao": "Sistema para coletar e armazenar água da chuva para irrigação.", "preco": 1200.0},
    {"nome": "Jardim Vertical", "descricao": "Criação de paredes vivas para embelezar ambientes e melhorar a qualidade do ar.", "preco": 2000.0},
]

def listar_servico(request): 
    return render(request, "home.html", {"Servicos": SERVICOS})

def add_servico(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        
        if nome and descricao and preco:
            try:
                preco = float(preco)
                SERVICOS.append({"nome": nome, "descricao": descricao, "preco": preco})
            except:
                pass
            
        return redirect("home")
    return render(request, "adicionar.html")

def calcular_valor(request):
    resultado = None
    erro = None
 
    if request.method == 'POST':
        try:
            area = float(request.POST.get('area'))
            preco_m2 = 55
 
            if area <= 0:
                erro = "Área deve ser maiores que zero."
            else:
                valor_total = area * preco_m2
                resultado = f"Valor estimado: R$ {valor_total:.2f}"
        except (ValueError, TypeError):
            erro = "Valores inválidos. Por favor, insira números válidos."
 
    return render(request, 'calculadora.html', {
        'resultado': resultado,
        'erro': erro
    })
 
def economia_agua(request):
    resultado = None
   
    if request.method == "POST":
        try:
            area = float(request.POST.get("area"))  
            nativas = float(request.POST.get("nativas"))  
 
           
            fator = 10  
            economia = area * (nativas / 100) * fator
 
            resultado = f"Seu jardim pode economizar aproximadamente {economia:.1f} litros de água por mês."
        except:
            resultado = "Erro: verifique os valores informados."
 
    return render(request, "economia_agua.html", {"resultado": resultado})
