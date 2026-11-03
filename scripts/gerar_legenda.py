import json,re
segs=json.load(open('/home/claude/asr/segs.json'))
T=[
"Como pediatra, eu vou te dar hoje 5 motivos para colocar o teu filho na luta. E não, não é só pra ele aprender a lutar. É por tudo o que a luta faz no cérebro do teu filho. Primeiro, regulação emocional. Na luta, a criança perde, perde muito.",
"Perde na frente dos outros, sem poder gritar, sem poder desistir no meio. Ela aprende a sentir raiva, frustração e cansaço sem agir por impulso. Isso é autorregulação acontecendo num ambiente seguro e supervisionado. E é exatamente a habilidade que mais falta na vida adulta.",
"Segundo, consciência corporal. Esse é o motivo mais pediátrico de todos e quase ninguém fala. A criança aprende a cair, aprende onde o corpo dela começa e termina, como distribuir o peso, como se equilibrar. Isso se chama propriocepção, e numa geração que passa o dia sentada, é uma das coisas que mais está em déficit. Terceiro,",
"atenção sustentada. Uma sequência de movimentos, técnica, correção, repetição. Não tem como fazer isso com meia atenção. A criança treina foco por um período contínuo. Algo cada vez mais raro num cérebro acostumado a vídeos de 15 segundos.",
"Quarto, autoestima construída em cima de competência real. Não é elogio vazio. Ela aprendeu uma técnica que não sabia, passou de faixa, conseguiu algo que exigiu esforço. A mensagem que fica é...",
"Eu sou capaz. E ela vem de evidências, não de alguém dizendo pra ela. Quinto, contato físico e hierarquia. A criança aprende a tocar e ser tocada dentro de uma regra clara. A respeitar o mestre. A cumprimentar o adversário depois de perder. É socialização com limite. Isso tem um valor enorme numa fase em que boa parte da convivência virou tela.",
"Agora, duas coisas importantes. Luta não substitui acompanhamento em saúde mental quando necessário. É ferramenta, não tratamento. E o que faz a diferença é o mestre, é o professor. Lugar que humilha, que força a criança a competir antes da hora, ou que trata derrota como vergonha...",
"não desenvolve nada disso. Visite a academia antes, observe a aula. Quem ensina importa muito mais do que a modalidade. E aí, você já conhecia alguns desses benefícios? Me conta aqui nos comentários.",
]
assert len(T)==len(segs),(len(T),len(segs))
HL={'regulação','emocional','raiva','frustração','cansaço','autorregulação','consciência','corporal','propriocepção','atenção','foco','autoestima','competência','capaz','evidências','hierarquia','respeitar','saúde','mental','professor','comentários','perde','cair'}
def ts(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60; return f"{h}:{m:02d}:{s:05.2f}"
ev=[]
for sg,txt in zip(segs,T):
    words=txt.split(); tot=sum(len(w)+1 for w in words); t=sg['start']; dur=sg['end']-sg['start']
    chunks=[];cur=[]
    for w in words:
        cur.append(w)
        if len(' '.join(cur))>=15 or re.search(r'[.!?,…]$',w) and len(' '.join(cur))>=8 or len(cur)>=4 and len(' '.join(cur))>=12:
            chunks.append(cur);cur=[]
    if cur: chunks.append(cur)
    for c in chunks:
        L=sum(len(w)+1 for w in c); d=dur*L/tot
        txt2=' '.join(('{\\c&H00DDFF&}'+w.upper()+'{\\c&HFFFFFF&}') if re.sub(r'[.,!?…]','',w.lower()) in HL else w.upper() for w in c)
        ev.append((t,t+d-0.03,txt2)); t+=d
END=113.1
lines=["[Script Info]","ScriptType: v4.00+","PlayResX: 1080","PlayResY: 1920","WrapStyle: 2","","[V4+ Styles]",
"Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding",
"Style: S,Anton,88,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,6,2,2,60,60,300,1","","[Events]","Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text"]
for a,b,x in ev:
    if a>=END: continue
    lines.append(f"Dialogue: 0,{ts(a)},{ts(min(b,END))},S,,0,0,0,,{{\\fad(70,0)\\fscx90\\fscy90\\t(0,90,\\fscx100\\fscy100)}}{x}")
open('/home/claude/v2/subs3.ass','w').write('\n'.join(lines)); print(len(ev))
