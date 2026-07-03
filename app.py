import streamlit as st
from datetime import datetime, date

# Configuração da página do site
st.set_page_config(page_title="Controle de Validade - Cozinha", page_icon="🍳", layout="wide")

# Título principal do Site
st.title("🍳 Sistema de Controle da Cozinha")
st.write("Sistema ativo. Aguardando comandos do cozinheiro **Victor**.")

# Banco de dados zerado (começa totalmente vazio)
if "produtos" not in st.session_state:
    st.session_state.produtos = []

# Divisão da tela em duas colunas
col1, col2 = st.columns([1, 2])

# COLUNA 1: Formulário para o Victor digitar os produtos
with col1:
    st.header("📥 Cadastrar Novo Produto")
    
    nome = st.text_input("Nome do Alimento / Bebida:", placeholder="Ex: Queijo, Leite, Carne...")
    
    # Seus eletrodomésticos exatos da cozinha
    local = st.selectbox("Onde este produto será guardado?", [
        "Geladeira Principal (1)", 
        "Freezer Branco", 
        "Freezer Red Bull", 
        "Freezer Grande"
    ])
    
    data_val = st.date_input("Data de Validade do Produto:", min_value=date.today())
    
    # Botão para salvar
    if st.button("Adicionar ao Estoque"):
        if nome:
            # Salva o produto digitado no banco de dados
            st.session_state.produtos.append({
                "nome": nome.strip(), 
                "local": local, 
                "validade": data_val
            })
            st.success(f"🟢 {nome} adicionado com sucesso!")
        else:
            st.error("⚠️ Por favor, digite o nome do produto antes de adicionar.")

# COLUNA 2: O painel de Alarmes Automáticos
with col2:
    st.header("🚨 Alarmes e Estoque Atual")
    
    # Se não tiver nada cadastrado, mostra que o estoque está zerado
    if len(st.session_state.produtos) == 0:
        st.info("O estoque está completamente vazio. Victor pode começar a enviar os produtos!")
    else:
        # Botão secreto caso você queira zerar tudo de novo no futuro
        if st.button("🗑️ Limpar Todo o Estoque"):
            st.session_state.produtos = []
            st.rerun()
            
        st.write("---")
        
        # Lista os produtos e calcula o alarme automático de dias restantes
        for item in st.session_state.produtos:
            hoje = date.today()
            dias_restantes = (item["validade"] - hoje).days
            
            # Lógica Inteligente do Alarme Automático
            if dias_restantes < 0:
                status_texto = f"❌ VENCIDO HÁ {abs(dias_restantes)} DIAS!"
                cor_alarme = "#ef4444" # Vermelho escuro
                cor_fundo = "#fee2e2"
            elif dias_restantes <= 3:
                status_texto = f"🚨 CRÍTICO! Vence em {dias_restantes} dias."
                cor_alarme = "#dc2626" # Vermelho
                cor_fundo = "#fee2e2"
            elif dias_restantes <= 7:
                status_texto = f"⚠️ ATENÇÃO! Vence em {dias_restantes} dias."
                cor_alarme = "#d97706" # Laranja/Amarelo
                cor_fundo = "#fef3c7"
            else:
                status_texto = f"✅ Seguro ({dias_restantes} dias restantes)"
                cor_alarme = "#16a34a" # Verde
                cor_fundo = "#dcfce7"
            
           # Lista os produtos e calcula o alarme automático de dias restantes
        for item in st.session_state.produtos:
            hoje = date.today()
            dias_restantes = (item["validade"] - hoje).days
            
            # Lógica Inteligente do Alarme Automático
            if dias_restantes < 0:
                status_texto = f"❌ VENCIDO HÁ {abs(dias_restantes)} DIAS!"
                cor_alarme = "#ef4444" # Vermelho escuro
                cor_fundo = "#fee2e2"
            elif dias_restantes <= 3:
                status_texto = f"🚨 CRÍTICO! Vence em {dias_restantes} dias."
                cor_alarme = "#dc2626" # Vermelho
                cor_fundo = "#fee2e2"
            elif dias_restantes <= 7:
                status_texto = f"⚠️ ATENÇÃO! Vence em {dias_restantes} dias."
                cor_alarme = "#d97706" # Laranja/Amarelo
                cor_fundo = "#fef3c7"
            else:
                status_texto = f"✅ Seguro ({dias_restantes} dias restantes)"
                cor_alarme = "#16a34a" # Verde
                cor_fundo = "#dcfce7"
            
            # CÓDIGO CORRIGIDO COM AS CHAVES DUPLAS {{ }} PARA O CSS NÃO DAR CONFLITO
            st.markdown(f"""
            <div style="padding: 12px; border-radius: 8px; border-left: 6px solid {cor_alarme}; background-color: {cor_fundo}; margin-bottom: 12px; color: #1e293b;">
                <span style="font-size: 12pt; font-weight: bold;">{item['nome']}</span> <br>
                <span style="font-size: 10pt;">📍 Local: <b>{item['local']}</b> | Validade: {item['validade'].strftime('%d/%m/%Y')}</span><br>
                <span style="font-size: 10.5pt; font-weight: bold; color: {cor_alarme};">{status_texto}</span>
            </div>
            """, unsafe_allow_code=True)
