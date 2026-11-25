import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *

# ---------------- P01 ----------------
fig,ax,W=new("P01","Map","Time Based Key-Value Store (LeetCode 981)","guardar (clave, valor, tiempo); get(clave, t) devuelve el valor del mayor tiempo ≤ t.")
y=-20
step(ax,3,y,1,"set(foo, bar, 1) y set(foo, bar2, 4) se guardan en un std::map ordenado por tiempo:")
y-=8
card(ax,8,y-1,48,7,"",fc=PANEL,ec=LINE)
ax.text(11,y+2.5,'db["foo"] =',fontsize=12.5,color=INK2,va="center",family="monospace")
card(ax,26,y+0.2,13,4.6,"1 → \"bar\"",fc=NAVY_L,ec=NAVY,fs=12)
card(ax,41,y+0.2,13,4.6,"4 → \"bar2\"",fc=NAVY_L,ec=NAVY,fs=12)
y-=8
step(ax,3,y,2,"get(foo, t): upper_bound(t) apunta al primer tiempo > t; el anterior es el mayor ≤ t.")
y-=10
tx0,tx1=8,62
def X(t): return tx0+(tx1-tx0)*t/6
for t,v in [(1,"bar"),(4,"bar2")]:
    card(ax,X(t)-4,y+1.6,8,3.8,f'"{v}"',fc=NAVY,ec=NAVY,tc="white",fs=12,bold=True)
    ax.plot([X(t)]*2,[y,y+1.6],color=NAVY,lw=2)
ax.plot([tx0,tx1+2],[y,y],color=INK2,lw=1.6)
for t in range(7):
    ax.plot([X(t)]*2,[y-0.7,y+0.7],color=INK2,lw=1.2); ax.text(X(t),y-2.6,str(t),ha="center",fontsize=11.5,color=INK2)
ax.text(tx1+3,y,"tiempo",fontsize=11.5,color=INK2,va="center")
qs=[(1,1,"bar"),(3,1,"bar"),(4,4,"bar2"),(5,4,"bar2")]
y-=7
for k,(q,f,v) in enumerate(qs):
    yy=y-k*4.6
    if q!=f:
        ax.plot([X(q)],[yy],"o",color=ORANGE,ms=10,zorder=6)
        arrow(ax,(X(q)-0.8,yy),(X(f)+0.9,yy),c=ORANGE)
        ax.plot([X(f)],[yy],"s",color=NAVY,ms=9,zorder=7)
    else:
        ax.plot([X(f)],[yy],"o",mfc="none",mec=ORANGE,mew=2.2,ms=17,zorder=6)
        ax.plot([X(f)],[yy],"s",color=NAVY,ms=9,zorder=7)
        ax.text(X(f)+2.6,yy,"t ya está guardado",va="center",fontsize=10.5,color=INK2)
    card(ax,70,yy-1.9,28,3.8,"",fc=GREEN_L,ec=GREEN)
    ax.text(72,yy,f'get(foo, {q})  →  "{v}"',va="center",fontsize=12,color=INK,zorder=6)
y-=3*4.6+6
legend(ax,8,y,[(ORANGE,ORANGE,"t consultado"),(NAVY,NAVY,"tiempo hallado (mayor ≤ t)")])
save(fig,ax,"p01",y-4)

# ---------------- P02 ----------------
fig,ax,W=new("P02","Map","My Calendar II (LeetCode 731)","aceptar una reserva [inicio, fin) solo si ningún instante queda reservado 3 veces.")
books=[(10,20,True),(50,60,True),(10,40,True),(5,15,False),(5,10,True),(25,55,True)]
y=-20
ax.text(2,y,"Reservas en orden:",fontsize=12.5,color=INK2,va="center")
cx=24
for i,(s,e,ok) in enumerate(books):
    card(ax,cx,y-2.4,11.5,4.8,f"[{s},{e}) {'✓' if ok else '✗'}",fc=GREEN_L if ok else RED_L,ec=GREEN if ok else RED,fs=12)
    cx+=12.5
y-=9
step(ax,3,y,1,"Al llegar book(5, 15) ya hay 3 reservas aceptadas (azul):")
tx0,tx1=12,86
def X(t): return tx0+(tx1-tx0)*t/65
y-=7
for (s,e,yy) in [(10,20,y),(50,60,y),(10,40,y-4.6)]:
    card(ax,X(s),yy-1.8,X(e)-X(s),3.6,f"[{s},{e})",fc=NAVY_L,ec=NAVY,fs=11.5)
card(ax,X(5),y-11,X(15)-X(5),3.6,"[5,15)",fc="white",ec=RED,fs=11.5,ls="--",lw=1.8)
ax.text(X(15)+1.5,y-9.2,"← la nueva reserva",fontsize=11.5,color=RED,va="center")
y-=17
step(ax,3,y,2,"Mapa de diferencias (+1 en el inicio, −1 en el fin) y barrido: reservas activas en cada instante.")
lanes=[(10,20),(50,60),(10,40)]
base=[0]*66
for s,e in lanes:
    for t in range(s,e): base[t]+=1
new_=[base[t]+(1 if 5<=t<15 else 0) for t in range(66)]
py0=y-21; sc=4.4
def Y(v): return py0+v*sc
ax.plot([tx0,tx1],[py0,py0],color=INK2,lw=1.2)
for t in range(0,66,10): ax.text(X(t),py0-2.6,str(t),ha="center",fontsize=11,color=INK2)
for v in range(4): ax.text(tx0-1.5,Y(v),str(v),ha="right",va="center",fontsize=11,color=INK2)
ax.plot([X(0),X(65)],[Y(2),Y(2)],color=RED,lw=1.3,ls=":"); ax.text(X(65)+1,Y(2),"límite = 2",fontsize=11,color=RED,va="center")
xs=[X(t) for t in range(66)]
ax.add_patch(Rectangle((X(10),Y(2)),X(15)-X(10),sc,fc=RED_L,ec="none",zorder=1))
ax.step(xs,[Y(v) for v in base],where="post",color=NAVY,lw=2.6)
ax.step(xs,[Y(v) for v in new_],where="post",color=ORANGE,lw=2.2,ls="--")
ax.text((X(10)+X(15))/2+1,Y(3)+2,"¡3 a la vez en [10, 15)!",ha="center",fontsize=11.5,color=RED,fontweight="bold")
y=py0-8
legend(ax,12,y,[(NAVY,NAVY,"activas antes"),(ORANGE,ORANGE,"activas si se aceptara [5,15)")])
y-=8
result(ax,3,y,94,"book(5, 15) se rechaza y el mapa vuelve a su estado anterior (devuelve false).",ok=False)
save(fig,ax,"p02",y-3)

# ---------------- P03 ----------------
s="aacecaaa"; t=s+"#"+s[::-1]; n=len(t)
lps=[0]*n;k=0
for i in range(1,n):
    while k and t[i]!=t[k]: k=lps[k-1]
    if t[i]==t[k]: k+=1
    lps[i]=k
L=lps[-1]
fig,ax,W=new("P03","KMP","Shortest Palindrome (LeetCode 214)","agregar la menor cantidad de letras AL INICIO de s para volverla palíndromo.")
cw=4.7; x0=12; y=-20
step(ax,3,y,1,'Se arma t = s + "#" + reverso(s), con s = "aacecaaa", y se calcula su arreglo LPS:')
y-=7
ax.text(x0+len(s)*cw/2,y,"s",ha="center",fontsize=12,color=NAVY,fontweight="bold")
ax.text(x0+(len(s)+1+len(s)/2)*cw,y,"reverso(s)",ha="center",fontsize=12,color=ORANGE,fontweight="bold")
y-=7
ax.text(x0-2,y+2,"t",ha="right",va="center",fontsize=12.5,color=INK2); ax.text(x0-2,y-2.6,"lps",ha="right",va="center",fontsize=12.5,color=INK2)
for i,ch in enumerate(t):
    fc= NAVY_L if i<len(s) else ("white" if ch=="#" else ORANGE_L)
    cell(ax,x0+i*cw,y,ch,fc=fc,w=cw,h=4)
    cell(ax,x0+i*cw,y-4.6,lps[i],fc=YEL if i==n-1 else "white",w=cw,h=4,bold=(i==n-1))
y-=12
step(ax,3,y,2,f"lps final = {L}: los {L} primeros caracteres de s se leen igual al revés (palíndromo).")
y-=9; xs0=30
for i,ch in enumerate(s):
    cell(ax,xs0+i*cw,y,ch,fc=GREEN_L if i<L else ORANGE_L,w=cw)
ax.annotate("",xy=(xs0,y-1.2),xytext=(xs0+L*cw,y-1.2),arrowprops=dict(arrowstyle="<->",color=GREEN,lw=1.6))
ax.text(xs0+L*cw/2,y-3.6,f'palíndromo "{s[:L]}"',ha="center",fontsize=12,color=GREEN,fontweight="bold")
ax.text(xs0+L*cw+cw/2,y-3.6,"resto",ha="center",fontsize=12,color=ORANGE,fontweight="bold")
y-=10
step(ax,3,y,3,"Se copia el resto invertido delante de s:")
y-=9
rest=s[L:][::-1]; ans=rest+s
for i,ch in enumerate(ans):
    j=i-len(rest)
    cell(ax,xs0+j*cw,y,ch,fc=ORANGE if j<0 else (GREEN_L if j<L else ORANGE_L),w=cw,tc="white" if j<0 else INK,bold=j<0)
ax.text(xs0-cw/2,y+6,"agregado",ha="center",fontsize=11.5,color=ORANGE,fontweight="bold")
y-=8
result(ax,3,y,94,f'respuesta: "{ans}"  (se agrega 1 letra)')
save(fig,ax,"p03",y-3)

# ---------------- P04 ----------------
s="fixprefixsuffix"; n=len(s)
lps=[0]*n;k=0
for i in range(1,n):
    while k and s[i]!=s[k]: k=lps[k-1]
    if s[i]==s[k]: k+=1
    lps[i]=k
M=max(lps[1:n-1])
fig,ax,W=new("P04","KMP","Password (Codeforces 126B)","la subcadena más larga que sea prefijo y sufijo de s y que además aparezca en su interior.")
cw=5.4;x0=12;y=-24
for (a,b,lab,c) in [(0,3,"prefijo",NAVY),(6,9,"aparición interior",GREEN),(n-3,n,"sufijo",ORANGE)]:
    ax.text(x0+(a+b)/2*cw,y,lab,ha="center",fontsize=12,color=c,fontweight="bold")
    ax.plot([x0+a*cw+0.4,x0+b*cw-0.4],[y-1.8,y-1.8],color=c,lw=3)
y-=8
ax.text(x0-2,y+2,"s",ha="right",va="center",fontsize=12.5,color=INK2); ax.text(x0-2,y-2.6,"lps",ha="right",va="center",fontsize=12.5,color=INK2)
for i,ch in enumerate(s):
    fc=NAVY_L if i<3 else (GREEN_L if 6<=i<=8 else (ORANGE_L if i>=n-3 else "white"))
    cell(ax,x0+i*cw,y,ch,fc=fc,w=cw)
    inter=1<=i<=n-2
    cell(ax,x0+i*cw,y-4.6,lps[i],fc=YEL if (inter and lps[i]==M) else (ORANGE_L if i==n-1 else ("#E9EDF2" if not inter else "white")),w=cw,bold=(i==n-1 or (inter and lps[i]==M)))
    ax.text(x0+i*cw+cw/2,y-7.2,str(i),ha="center",fontsize=9.5,color=MUTED)
ax.text(x0,y-11,"lps[i] = largo del mayor prefijo de s que termina en i.   Amarillo = M (máximo interior);  naranja = k (borde).",fontsize=10.5,color=INK2)
y-=18
step(ax,3,y,1,f'Candidato más largo: k = lps[n−1] = {lps[-1]}  →  "{s[:lps[-1]]}" es prefijo y sufijo a la vez.')
y-=6.5
step(ax,3,y,2,f"Máximo en el interior: M = máx lps[1..n−2] = {M} (celda amarilla, termina en i = 8).")
y-=6.5
step(ax,3,y,3,"Si k ≤ M, el candidato también aparece dentro; si no, se prueba el siguiente borde lps[k−1].")
y-=10
result(ax,3,y,94,'k = 3 ≤ M = 3  →  respuesta "fix"')
save(fig,ax,"p04",y-3)

# ---------------- P05 ----------------
s="aabcaabxaaz"; n=len(s)
z=[0]*n; z[0]=n; l=r=0; reuse=None
for i in range(1,n):
    if i<r:
        z[i]=min(r-i,z[i-l])
        if reuse is None and z[i-l]>0: reuse=(i,l,r,i-l)
    while i+z[i]<n and s[z[i]]==s[i+z[i]]: z[i]+=1
    if i+z[i]>r: l,r=i,i+z[i]
i0,L0,R0,k0=reuse
fig,ax,W=new("P05","Algoritmo Z","Sum of Scores of Built Strings (LeetCode 2223)","sumar, para cada sufijo de s, cuántas letras iniciales comparte con s (eso es z[i]).")
cw=6.2;x0=14;y=-24
ax.annotate("",xy=(x0+L0*cw,y),xytext=(x0+R0*cw,y),arrowprops=dict(arrowstyle="<->",color=NAVY,lw=1.6))
ax.text(x0+(L0+R0)/2*cw,y+2,f"ventana [L, R) = [{L0}, {R0}) igual al prefijo",ha="center",fontsize=11.5,color=NAVY,fontweight="bold")
ax.annotate("",xy=(x0,y),xytext=(x0+(R0-L0)*cw,y),arrowprops=dict(arrowstyle="<->",color=GREEN,lw=1.6))
ax.text(x0+(R0-L0)/2*cw,y+2,"prefijo",ha="center",fontsize=11.5,color=GREEN,fontweight="bold")
y-=8
ax.text(x0-2,y+2,"s",ha="right",va="center",fontsize=12.5,color=INK2); ax.text(x0-2,y-2.6,"z",ha="right",va="center",fontsize=12.5,color=INK2)
for i,ch in enumerate(s):
    fc="white"
    if L0<=i<R0: fc=NAVY_L
    if i<R0-L0: fc=GREEN_L
    cell(ax,x0+i*cw,y,ch,fc=fc,w=cw)
    cell(ax,x0+i*cw,y-4.6,z[i],fc=YEL if i in (i0,k0) else "white",w=cw,bold=i in (i0,k0))
    ax.text(x0+i*cw+cw/2,y-7.2,str(i),ha="center",fontsize=9.5,color=MUTED)
arrow(ax,(x0+i0*cw+cw/2,y-9.6),(x0+k0*cw+cw/2,y-9.6),c=ORANGE,rad=-0.3)
ax.text(x0+(i0+k0)/2*cw+cw/2,y-16.5,f"z[{i0}] copia z[{k0}] = {z[k0]} sin comparar",ha="center",fontsize=11.5,color=ORANGE,fontweight="bold")
y-=22
step(ax,3,y,1,f"z[i] = letras iniciales que s[i..] comparte con s; z[0] = n = {n}.")
y-=6.5
step(ax,3,y,2,"Dentro de la ventana, s[i..] repite lo que hay en s[i − L..]: se parte de min(R − i, z[i − L]).")
y-=6.5
step(ax,3,y,3,"Solo se compara más allá de R y R nunca retrocede: el arreglo completo cuesta O(n).")
y-=10
result(ax,3,y,94,"puntaje total = "+" + ".join(map(str,z))+f" = {sum(z)}")
save(fig,ax,"p05",y-3)
