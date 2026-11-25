import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *

# ---------------- P06 ----------------
s="ABACABA"; n=len(s)
z=[0]*n; z[0]=n; l=r=0
for i in range(1,n):
    if i<r: z[i]=min(r-i,z[i-l])
    while i+z[i]<n and s[z[i]]==s[i+z[i]]: z[i]+=1
    if i+z[i]>r: l,r=i,i+z[i]
cnt=[0]*(n+2)
for v in z: cnt[v]+=1
for L in range(n-1,0,-1): cnt[L]+=cnt[L+1]
res=[(L,cnt[L]) for L in range(1,n+1) if L==n or z[n-L]==L]
fig,ax,W=new("P06","Algoritmo Z","Prefixes and Suffixes (Codeforces 432D)","para cada prefijo que también es sufijo, contar cuántas veces aparece en s.")
cw=6.5;x0=14;y=-26
ax.text(x0-2,y+2,"s",ha="right",va="center",fontsize=12.5,color=INK2); ax.text(x0-2,y-2.6,"z",ha="right",va="center",fontsize=12.5,color=INK2)
bset={n-L:L for L,_ in res if L<n}
for i,ch in enumerate(s):
    cell(ax,x0+i*cw,y,ch,w=cw)
    cell(ax,x0+i*cw,y-4.6,z[i],fc=YEL if i in bset else (NAVY_L if i==0 else "white"),w=cw,bold=i in bset)
    ax.text(x0+i*cw+cw/2,y+5.2,str(i),ha="center",fontsize=9.5,color=MUTED)
ax.text(x0+n*cw+3,y-2.6,"amarillo: z[n − l] = l",fontsize=11,color=INK2,va="center")
y-=13
step(ax,3,y,1,"Bordes: el prefijo de longitud l es también sufijo si z[n − l] = l (y siempre l = n).")
y-=9
# border cards
bx=8
for L,c in res:
    wd=n*2.2+12
    card(ax,bx,y-3,wd,6,"",fc=PANEL,ec=LINE)
    for j in range(n):
        fc= GREEN_L if j<L else "white"
        if j>=n-L and L<n: fc= ORANGE_L if j>=L else "#CFE8D9"
        ax.add_patch(Rectangle((bx+1.5+j*2.2,y-1.1),2.2,2.6,fc=fc,ec=LINE,lw=0.8,zorder=4))
        ax.text(bx+1.5+j*2.2+1.1,y+0.2,s[j],ha="center",va="center",fontsize=9,zorder=5)
    ax.text(bx+1.5+n*2.2+1.2,y+0.2,f"l = {L}",va="center",fontsize=11.5,color=INK,fontweight="bold",zorder=5)
    bx+=wd+3
y-=6
legend(ax,8,y,[(GREEN_L,LINE,"prefijo de longitud l"),(ORANGE_L,LINE,"sufijo de longitud l"),("#CFE8D9",LINE,"ambos")])
y-=8
step(ax,3,y,2,"Apariciones: el prefijo de longitud l aparece en i si z[i] ≥ l → contar los z[i] ≥ l.")
y-=4
# bar chart
bx0=14; bw=8; base=y-20; sc=3.4
for L in range(1,n+1):
    isb=any(L==b for b,_ in res)
    ax.add_patch(Rectangle((bx0+(L-1)*(bw+3),base),bw,cnt[L]*sc,fc=ORANGE if isb else "#D5DBE3",ec="none",zorder=3))
    ax.text(bx0+(L-1)*(bw+3)+bw/2,base+cnt[L]*sc+1.5,str(cnt[L]),ha="center",fontsize=11.5,color=INK,fontweight="bold" if isb else "normal")
    ax.text(bx0+(L-1)*(bw+3)+bw/2,base-2.6,f"l={L}",ha="center",fontsize=11,color=INK2)
ax.plot([bx0-2,bx0+n*(bw+3)],[base,base],color=INK2,lw=1.2)
y=base-9
legend(ax,14,y,[(ORANGE,ORANGE,"l es borde (se imprime)"),("#D5DBE3","#D5DBE3","l no es borde")])
y-=8
result(ax,3,y,94,f"salida: {len(res)} bordes →  "+",  ".join(f"(l={L}, veces={c})" for L,c in res))
save(fig,ax,"p06",y-3)

# ---------------- P07 ----------------
a=[1,0,1,1,0,0,1,0]; b=a[:]
for i in range(2,6): b[i]^=1
fig,ax,W=new("P07","Segment Tree","Handling Sum Queries After Update (LeetCode 2569)","invertir bits de nums1 en [l, r]; sumar p·nums1 a nums2; reportar la suma de nums2.")
y=-20
step(ax,3,y,1,"La clave: el tipo 2 suma p × (cantidad de unos de nums1). El Segment Tree cuenta esos unos.")
y-=9; cw=7; x0=20
ax.text(x0-2,y+2,"antes",ha="right",va="center",fontsize=12,color=INK2)
for i,v in enumerate(a): cell(ax,x0+i*cw,y,v,w=cw,fc=NAVY_L if v else "white",bold=bool(v))
ax.text(x0+8*cw+3,y+2,f"unos = {sum(a)}",va="center",fontsize=12,color=INK)
arrow(ax,(x0+4*cw,y-0.8),(x0+4*cw,y-4.2),c=ORANGE)
ax.text(x0+4*cw+2,y-2.5,"tipo 1: invertir [2, 5]",va="center",fontsize=11.5,color=ORANGE,fontweight="bold")
y-=9
ax.text(x0-2,y+2,"después",ha="right",va="center",fontsize=12,color=INK2)
for i,v in enumerate(b): cell(ax,x0+i*cw,y,v,w=cw,fc=(ORANGE_L if 2<=i<=5 else (NAVY_L if v else "white")),bold=bool(v))
ax.text(x0+8*cw+3,y+2,f"unos = {sum(b)}",va="center",fontsize=12,color=INK)
for i in range(8): ax.text(x0+i*cw+cw/2,y-2.2,str(i),ha="center",fontsize=9.5,color=MUTED)
y-=9
step(ax,3,y,2,"Inversión con propagación diferida (lazy): un nodo cubierto por completo pasa de unos a (largo − unos).")
y-=9
# tree after flip
nodes={}
def build(nd,l,r,depth,x):
    nodes[(l,r)]=(x,depth)
    if l==r: return
    m=(l+r)//2; off=26/(2**depth)
    build(2*nd,l,m,depth+1,x-off); build(2*nd+1,m+1,r,depth+1,x+off)
build(1,0,7,0,50)
lazy={(2,3),(4,5)}; partial={(0,7),(0,3),(4,7)}; pend={(2,2),(3,3),(4,4),(5,5)}
def ones(l,r,arr): return sum(arr[l:r+1])
for (l,r),(x,d) in nodes.items():
    if l!=r:
        m=(l+r)//2
        for c in [(l,m),(m+1,r)]:
            cx,cd=nodes[c]; ax.plot([x,cx],[y-d*8.5-2,y-cd*8.5+2],color=LINE,lw=1.4,zorder=1)
for (l,r),(x,d) in nodes.items():
    yy=y-d*8.5
    if (l,r) in lazy: fc,ec,txt=ORANGE,ORANGE,f"[{l},{r}]\nunos {ones(l,r,b)} ⚑"
    elif (l,r) in partial: fc,ec,txt=YEL,"#C9A227",f"[{l},{r}]\nunos {ones(l,r,b)}"
    elif (l,r) in pend: fc,ec,txt="#EEF1F5",LINE,f"[{l},{r}]\npend."
    else: fc,ec,txt="white",LINE,f"[{l},{r}]\nunos {ones(l,r,b)}"
    wd=9 if d<3 else 6.2
    card(ax,x-wd/2,yy-2.6,wd,5.2,"",fc=fc,ec=ec)
    ax.text(x,yy,txt,ha="center",va="center",fontsize=9.5 if d==3 else 10.5,color="white" if (l,r) in lazy else INK,zorder=5,fontweight="bold" if (l,r) in lazy else "normal")
y-=3*8.5+7
legend(ax,8,y,[(ORANGE,ORANGE,"cubierto: se invierte y se marca ⚑"),(YEL,"#C9A227","parcial: se recalcula"),("#EEF1F5",LINE,"hijos: se actualizan después")],fs=11)
y-=7
step(ax,3,y,3,"tipo 2 con p = 3: suma += 3 × unos(raíz) = 3 × 4 = 12.   tipo 3: se reporta la suma.")
y-=9
result(ax,3,y,94,"cada consulta cuesta O(log n): solo se visitan los nodos del borde del rango")
save(fig,ax,"p07",y-3)

# ---------------- P08 ----------------
free=[1,2,5,5]; m=5
fig,ax,W=new("P08","Segment Tree","Booking Concert Tickets in Groups (LeetCode 2286)","gather: k asientos juntos en una fila ≤ maxRow; scatter: k asientos en filas ≤ maxRow.")
y=-20
step(ax,3,y,1,"Estado de la sala (m = 5 asientos por fila). Cada fila se llena de izquierda a derecha:")
y-=6; sx=22; sw=6
for r in range(4):
    yy=y-r*6.2
    ax.text(sx-3,yy-2.4,f"fila {r}",ha="right",va="center",fontsize=12,color=INK2)
    for c in range(m):
        occ=c< m-free[r]
        new=(r==2 and c<4)
        fc= "#9AA5B1" if occ else (GREEN if new else "white")
        ec= "#6B7785" if occ else (GREEN if new else NAVY)
        card(ax,sx+c*(sw+1),yy-4.8,sw,4.8,"",fc=fc,ec=ec,r=0.6)
    ax.text(sx+m*(sw+1)+2,yy-2.4,f"libres = {free[r]}"+("  → 1 tras gather" if r==2 else ""),va="center",fontsize=12,color=INK)
legend(ax,sx-8,y-4*6.2-2,[("#9AA5B1","#6B7785","ocupado"),("white",NAVY,"libre"),(GREEN,GREEN,"asignado por gather(4, 3)")])
y-=4*6.2+11
step(ax,3,y,2,"Segment Tree: cada nodo guarda (máximo de libres, suma de libres) de un rango de filas.")
y-=8
pos={(0,3):(50,0),(0,1):(28,1),(2,3):(72,1),(0,0):(17,2),(1,1):(39,2),(2,2):(61,2),(3,3):(83,2)}
path={(0,3),(2,3),(2,2)}
for (l,r),(x,d) in pos.items():
    if l!=r:
        mid=(l+r)//2
        for c in [(l,mid),(mid+1,r)]:
            cx,cd=pos[c]; onp=(l,r) in path and c in path
            ax.plot([x,cx],[y-d*9-2.6,y-cd*9+2.6],color=ORANGE if onp else LINE,lw=3 if onp else 1.4,zorder=1)
for (l,r),(x,d) in pos.items():
    sub=free[l:r+1]; yy=y-d*9
    fc=ORANGE_L if (l,r) in path else ("#EEF1F5" if (l,r)==(0,1) else "white")
    ec=ORANGE if (l,r) in path else LINE
    card(ax,x-9,yy-2.8,18,5.6,"",fc=fc,ec=ec,lw=1.8 if (l,r) in path else 1.2)
    ax.text(x,yy+1,f"filas {l}–{r}" if l!=r else f"fila {l}",ha="center",va="center",fontsize=10.5,color=INK2,zorder=5)
    ax.text(x,yy-1.3,f"máx {max(sub)} · suma {sum(sub)}",ha="center",va="center",fontsize=11,color=INK,fontweight="bold",zorder=5)
ax.text(28-10,y-9+4.2,"máx 2 < 4 → se descarta",ha="center",fontsize=10.5,color=RED)
y-=2*9+11
step(ax,3,y,3,"gather(4, 3): bajar por el hijo izquierdo si su máximo ≥ 4; si no, por el derecho → fila 2.",c=ORANGE)
y-=6.5
step(ax,3,y,4,"scatter(4, 1): suma de libres en filas 0–1 = 1 + 2 = 3 < 4 → no alcanza.",c=RED)
y-=9
result(ax,3,y,45,"gather(4, 3) → [fila 2, asiento 0]")
result(ax,52,y,45,"scatter(4, 1) → false",ok=False)
save(fig,ax,"p08",y-3)
