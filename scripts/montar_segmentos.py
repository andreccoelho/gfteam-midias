import subprocess, os, json, re
from PIL import Image, ImageDraw, ImageFont
U='/mnt/user-data/uploads/'; V=lambda n:U+n; P=lambda i:U+i+'-image.jpg'
FD='/home/claude/fonts/ttf/'; W,H=1080,1920
YEL=(255,221,0); WHITE=(255,255,255)
SECT={
 'intro':('JIU-JITSU INFANTIL',[[('5 MOTIVOS PARA',0)],[('COLOCAR SEU FILHO',0)],[('NA ',0),('LUTA.',1)]],'Por tudo o que a luta faz no cérebro.'),
 's1':('1º MOTIVO',[[('REGULAÇÃO ',1),('EMOCIONAL',0)]],'Perder, sentir raiva e não agir por impulso.'),
 's2':('2º MOTIVO',[[('CONSCIÊNCIA ',1),('CORPORAL',0)]],'Cair, equilibrar e saber onde o corpo começa e termina.'),
 's3':('3º MOTIVO',[[('ATENÇÃO ',1),('SUSTENTADA',0)]],'Foco contínuo num mundo de vídeos de 15 segundos.'),
 's4':('4º MOTIVO',[[('AUTOESTIMA',1)],[('CONSTRUÍDA EM CIMA',0)],[('DE ',0),('COMPETÊNCIA REAL.',1)]],'Não é elogio vazio. É evidência.'),
 's5':('5º MOTIVO',[[('CONTATO FÍSICO',0)],[('E ',0),('HIERARQUIA.',1)]],'Tocar e ser tocado dentro de uma regra clara.'),
 'close':('ANTES DE MATRICULAR',[[('DUAS COISAS',0)],[('IMPORTANTES.',1)]],'Quem ensina importa mais do que a modalidade.'),
}
def header(key):
    out=f'/home/claude/v2/hdr_{key}.png'
    if os.path.exists(out): return out
    tag,lines,sub=SECT[key]
    im=Image.new('RGBA',(W,H),(0,0,0,0)); px=im.load()
    for y in range(820):                      # top gradient
        a=int(240*(1-y/820)**1.05)
        for x in range(0,W): px[x,y]=(5,20,18,a)
    for y in range(1250,H):                   # bottom gradient
        a=int(200*((y-1250)/(H-1250))**1.4)
        for x in range(0,W): px[x,y]=(5,20,18,a)
    d=ImageDraw.Draw(im)
    fa=ImageFont.truetype(FD+'Anton.ttf',46); fh=ImageFont.truetype(FD+'Anton.ttf',100)
    fs=ImageFont.truetype(FD+'Inter-Regular.ttf',34)
    x0=60; y=140
    tw=d.textlength(tag,font=fa)+ 5*len(tag)*0  # chip
    chipw=int(tw+len(tag)*3+70)
    d.rounded_rectangle((x0,y,x0+chipw,y+62),radius=10,fill=(31,94,87,255))
    d.ellipse((x0+18,y+24,x0+32,y+38),fill=YEL)
    d.text((x0+46,y+7),tag,font=fa,fill=(220,240,235,255),spacing=0)
    y+=105
    for ln in lines:
        x=x0
        for t,hl in ln:
            col=YEL if hl else WHITE
            d.text((x+3,y+3),t,font=fh,fill=(0,0,0,150)); d.text((x,y),t,font=fh,fill=col+(255,))
            x+=d.textlength(t,font=fh)
        y+=112
    d.text((x0+2,y+34),sub,font=fs,fill=(0,0,0,200)); d.text((x0,y+32),sub,font=fs,fill=(255,255,255,255))
    d.rectangle((x0,y+90,x0+70,y+95),fill=YEL); d.rectangle((x0+70,y+90,x0+110,y+95),fill=(0,80,200,255))
    im.save(out); return out
LAND_V={'b05c4181-IMG_2457.mov','IMG_2461.mov','IMG_9761_3.mov'}
from PIL import ImageOps
def is_land(it):
    if it['kind']=='v': return os.path.basename(it['src']) in LAND_V
    im=ImageOps.exif_transpose(Image.open(it['src'])); return im.width>im.height
items=[]
def add(sec,kind,src,d,ss=0): items.append(dict(sec=sec,kind=kind,src=src,d=d,ss=ss))
add('intro','p',P('d87a6c14'),2.6); add('intro','p',P('072b35a6'),2.7); add('intro','p',P('5fa0286d'),2.7)
add('s1','v',V('IMG_8506_5.mov'),6,3); add('s1','v',V('IMG_8346_4.mov'),5,2); add('s1','p',P('81af0c3d'),3); add('s1','v',V('IMG_0163_7.mov'),5.4,3)
add('s2','v',V('IMG_8317_6.mov'),6,4); add('s2','v',V('b05c4181-IMG_2457.mov'),6,1); add('s2','v',V('IMG_0202_6.mov'),6.1,4)
add('s3','v',V('IMG_8348_5.mov'),6,3); add('s3','p',P('9f525ff9'),4.35); add('s3','p',P('3e50544e'),4.35)
add('s4','p',P('1193f7bf'),3.5); add('s4','p',P('d90eb664'),3.5); add('s4','v',V('IMG_9761_3.mov'),5.8,8); add('s4','p',P('8c82e304'),3.0)
add('s5','v',V('IMG_2461.mov'),6.2,3); add('s5','p',P('ff2a7d12'),3.5); add('s5','p',P('cd569443'),3.5); add('s5','p',P('aa0ddc10'),3.5)
add('close','v',V('09ed5fa1-IMG_9552.mp4'),5,0); add('close','p',P('21625e05'),3); add('close','p',P('79857402'),3); add('close','p',P('0d2a137b'),3); add('close','p',P('5ba5e079'),3.5); add('close','p',P('3140221a'),2.9)
main=sum(i['d'] for i in items); print('main',main)
BG="split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,eq=brightness=-0.04[bg];[b]scale=1080:1920:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2"
cmds=[]; XF=0.3; seen=set()
for k,it in enumerate(items):
    o=f'/home/claude/v2/seg3/{k:02d}.mp4'; d=it['d']+XF; h=header(it['sec'])
    first = it['sec'] not in seen; seen.add(it['sec'])
    hf = "[HI]format=rgba,fade=t=in:st=0:d=0.45:alpha=1[hh]" if first else "[HI]null[hh]"
    enc=['-r','30','-pix_fmt','yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-an','-t',f'{d:.2f}',o,'-y']
    land=is_land(it)
    inp=(['-ss',str(it['ss']),'-i',it['src']] if it['kind']=='v' else ['-loop','1','-framerate','30','-i',it['src']])
    ins=inp+['-loop','1','-i',h]
    if land:
        ins+=['-loop','1','-i','/home/claude/v2/bg_shadow.png','-loop','1','-i','/home/claude/v2/mask.png','-loop','1','-i','/home/claude/v2/cardfx.png']
        fc=("[0:v]scale=1000:562:flags=lanczos,format=rgba[c];[c][3:v]alphamerge[cm];[2:v][cm]overlay=40:760[b1];[b1][4:v]overlay=0:0[b2];"
            +hf.replace('[HI]','[1:v]')+";[b2][hh]overlay=0:0[v]")
    else:
        if it['kind']=='v': core="[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[b2]"
        else:
            fr=int(d*30); core=f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,zoompan=z='1+0.06*on/{fr}':d=1:s=1080x1920:fps=30[b2]"
        fc=core+";"+hf.replace('[HI]','[1:v]')+";[b2][hh]overlay=0:0[v]"
    cmds.append(['ffmpeg','-v','error']+ins+['-filter_complex',fc,'-map','[v]']+enc)
# outro from reference reel (HORÁRIOS card)
ref=[x for x in os.listdir(U) if x.startswith('d15830b4')][0]
n=len(items); od=120-main
cmds.append(['ffmpeg','-v','error','-ss','26.0','-i',U+ref,'-vf','scale=1080:1920:flags=lanczos,fps=30','-pix_fmt','yuv420p','-c:v','libx264','-preset','veryfast','-crf','18','-an','-t',f'{od:.2f}',f'/home/claude/v2/seg3/{n:02d}.mp4','-y'])
print('outro',od)
from concurrent.futures import ThreadPoolExecutor
def run(c):
    r=subprocess.run(c,capture_output=True,text=True)
    if r.returncode: print('ERR',c[-1],r.stderr[-400:])
LAND=list(range(len(cmds)))
with ThreadPoolExecutor(4) as ex: list(ex.map(run,[cmds[i] for i in LAND]))
json.dump([it['d'] for it in items]+[od],open('/home/claude/v2/durs.json','w'))
print('video done')
