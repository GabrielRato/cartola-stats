

import urllib2, json, pandas, requests,database as db


# Getting Teams
url = 'https://api.cartolafc.globo.com/clubes'

headers = {
    'cache-control': "no-cache",
    'postman-token': "5ec8d3c0-d69d-28b4-18f4-94814f3ca7b6"
    }

json_club =json.loads( requests.request("GET", url, headers=headers).text)


time_nome = []
time_id = []

for i in json_club.keys():
    time_nome.append( json_club[i]['nome'])
    time_id.append( json_club[i]['id'])

data = {'id': pandas.Series(time_id), 'nome': pandas.Series(time_nome)}
df_clubes = pandas.DataFrame(data)


#Getting Formations
url = 'https://api.cartolafc.globo.com/esquemas'
headers = {
    'cache-control': "no-cache",
    'postman-token': "d475b4f4-514a-3548-fe87-0908bc5ef7f8"
    }
str = "{\"esquema\": "+requests.request("GET", url, headers=headers).text+"}"

json_esquema = json.loads(str)
nome_esq = []
id_esq = []
for esquemas in json_esquema['esquema']:
    nome_esq.append(esquemas['nome'])
    id_esq.append(esquemas[ 'esquema_id'])
data = {'id': pandas.Series(id_esq), 'nome': pandas.Series(nome_esq)}
df_esquema = pandas.DataFrame(data)

#Getting players

url = 'https://api.cartolafc.globo.com/atletas/mercado'

json_atleta = urllib2.urlopen(url)

data = json.load(json_atleta)

nome_atl = []
apelido_atl = []
id_atl = []
clube_atl = []
status_atl = []
pontosnum = []
preco_num = []
variacao_num = []
media_num = []
jogos_num = []
posicao_id = []

tam = len(data['atletas'])
ca = [0] * tam
fc = [0] * tam
fd = [0] * tam
ff = [0] * tam
fs = [0] * tam
im = [0] * tam
pe = [0] * tam
rb = [0] * tam
dd = [0] * tam
gs = [0] * tam
a = [0] * tam
ft = [0] * tam
g = [0] * tam
sg = [0] * tam
pp = [0] * tam
cv = [0] * tam
dp = [0] * tam
gc = [0] * tam
scts = []
i = 0
j= 0

for item in data['atletas']:
    posicao_id.append(item['posicao_id'])
    nome_atl.append(item['nome'])
    apelido_atl.append(item['apelido'])
    id_atl.append(item['atleta_id'])
    clube_atl.append(item['clube_id'])
    status_atl.append(item['status_id'])
    pontosnum.append(item['pontos_num'])
    preco_num.append(item['preco_num'])
    variacao_num.append(item['variacao_num'])
    media_num.append(item['media_num'])
    jogos_num.append(item['jogos_num'])
    for scouts in (item['scout']).keys():

        scts.append(scouts)
        if(scts[i] == 'CA'):
            ca[j]=( item['scout'][scouts])
        if(scts[i] == 'FC'):
            fc[j]=( item['scout'][scouts])
        if (scts[i] == 'FD'):
            fd[j]=(item['scout'][scouts])
        if(scts[i] == 'FF'):
            ff[j]=( item['scout'][scouts])
        if(scts[i] == 'FS'):
            fs[j]=( item['scout'][scouts])
        if(scts[i] == 'I'):
            im[j]=( item['scout'][scouts])
        if(scts[i] == 'PE'):
            pe[j]=( item['scout'][scouts])
        if(scts[i] == 'RB'):
            rb[j]=( item['scout'][scouts])
        if(scts[i] == 'DD'):
            dd[j]=( item['scout'][scouts])
        if(scts[i] == 'GS'):
            gs[j]=( item['scout'][scouts])
        if(scts[i] == 'A'):
            a[j]=( item['scout'][scouts])
        if(scts[i] == 'FT'):
            ft[j]=( item['scout'][scouts])
        if(scts[i] == 'G'):
            g[j]=( item['scout'][scouts])
        if(scts[i] == 'SG'):
            sg[j]=( item['scout'][scouts])
        if(scts[i] == 'PP'):
            pp[j]=( item['scout'][scouts])
        if(scts[i] == 'CV'):
            cv[j]=( item['scout'][scouts])
        if(scts[i] == 'DP'):
            dp[j]=( item['scout'][scouts])
        if(scts[i] == 'GC'):
            gc[j]=( item['scout'][scouts])

        i+=1
    j+=1

tab_players = {'id': pandas.Series(id_atl),'posicao_id': pandas.Series(posicao_id), 'nome': pandas.Series(nome_atl),'clube_id': pandas.Series(clube_atl), 'apelido': pandas.Series(apelido_atl), 'status': pandas.Series(status_atl), 'pontosnum': pandas.Series(pontosnum), 'preco_num': pandas.Series(preco_num), 'variacao_num': pandas.Series(variacao_num), 'media_num': pandas.Series(media_num), 'jogos_num': pandas.Series(jogos_num), 'CA': pandas.Series(ca), 'FC': pandas.Series(fc), 'FD': pandas.Series(fd), 'FF': pandas.Series(ff), 'FS': pandas.Series(fs), 'I': pandas.Series(im), 'PE': pandas.Series(pe), 'RB': pandas.Series(rb), 'DD': pandas.Series(dd), 'GS': pandas.Series(gs), 'A': pandas.Series(a), 'FT': pandas.Series(ft), 'G': pandas.Series(g), 'SG': pandas.Series(sg), 'PP': pandas.Series(pp), 'CV': pandas.Series(cv), 'DP': pandas.Series(dp), 'GC': pandas.Series(gc)}
tab_players = pandas.DataFrame(tab_players)


url = 'https://api.cartolafc.globo.com/partidas'
json_partidas = urllib2.urlopen(url)

part = json.load(json_partidas)
part_data = []
clu_casa = []
clu_casa_pos = []
clu_vis = []
clu_vis_pos = []
local = []

for partida in part['partidas']:
    part_data.append(partida['partida_data'])
    clu_casa.append(partida['clube_casa_id'])
    clu_casa_pos.append(partida['clube_casa_posicao'])
    clu_vis.append(partida['clube_visitante_id'])
    clu_vis_pos.append(partida['clube_visitante_posicao'])
    local.append(partida['local'])
tab_partida = {'casa': pandas.Series(clu_casa),'visitante': pandas.Series(clu_vis),'casa_pos': pandas.Series(clu_casa_pos),'visit_pos': pandas.Series(clu_vis_pos),'data': pandas.Series(part_data),'local': pandas.Series(local)}
tab_partida = pandas.DataFrame(tab_partida)


#Passing all the data to sql
db.df2sqlite(tab_players,"cartola_fc","players")
db.df2sqlite(df_esquema,"cartola_fc","esquemas")
db.df2sqlite(df_clubes,"cartola_fc","times")
db.df2sqlite(tab_partida,"cartola_fc","partidas")
