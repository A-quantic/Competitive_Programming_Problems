import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *

# ---------------- P14 ----------------
nums=[3,1,5,8]; a=[1]+nums+[1]; n=len(a)
f=[[0]*n for _ in range(n)]; arg=[[0]*n for _ in range(n)]
for ln in range(2,n):
    for i in range(0,n-ln):
        j=i+ln
        for k in range(i+1,j):
            v=f[i][k]+f[k][j]+a[i]*a[k]*a[j]
            if v>f[i][j]: f[i][j]=v; arg[i][j]=k
fig,ax,W=new("P14","Programación dinámica","Burst Balloons (LeetCode 312)","reventar todos los globos; al reventar i se gana izq·i·der. Maximizar el total.")
y=-20
step(ax,3,y,1,"Idea clave: pensar en el ÚLTIMO globo k que se revienta dentro del intervalo abierto (i, j):")
y-=6
ax.text(6,y,"f[i][j] = máx sobre k de  f[i][k] + f[k][j] + a[i]·a[k]·a[j]      (a = [1, 3, 1, 5, 8, 1] con bordes 1)",fontsize=12,color=INK,va="center")
y-=7
step(ax,3,y,2,"Orden óptimo que reconstruye la tabla (cada fila es un estado de la secuencia):")
y-=8
order=[]  # reconstruct order: recursively, inner first
def rec(i,j):
    if j-i<2: return
    k=arg[i][j]; rec(i,k); rec(k,j); order.append((k,i,j))
rec(0,n-1)
alive=list(range(n)); total=0
def draw_row(yy,alive,hit,label):
    for idx in range(1,n-1):
        x=14+idx*10
        if idx in alive:
            c= ORANGE if idx==hit else NAVY_L
            ax.add_patch(Circle((x,yy),3.1,fc=c,ec=ORANGE if idx==hit else NAVY,lw=1.6,zorder=3))
            ax.text(x,yy,str(a[idx]),ha="center",va="center",fontsize=13,fontweight="bold",color="white" if idx==hit else INK,zorder=4)
        else:
            ax.text(x,yy,"·",ha="center",va="center",fontsize=16,color=MUTED)
    ax.text(60,yy,label,va="center",fontsize=11.5,color=INK)
for k,i,j in order:
    l=max(x for x in alive if x<k); r=min(x for x in alive if x>k)
    gain=a[l]*a[k]*a[j if False else r]; total+=gain
    draw_row(y,alive,k,f"revienta {a[k]}: {a[l]}·{a[k]}·{a[r]} = {gain}   (total {total})")
    alive=[x for x in alive if x!=k]; y-=8.5
y-=1
step(ax,3,y,3,"Tabla f[i][j] (se llena por longitud de intervalo; la respuesta está en la esquina f[0][5]):")
y-=6; cw=9; ch=5; x0=20
for j in range(n): ax.text(x0+j*cw+cw/2,y,f"j={j}",ha="center",fontsize=10.5,color=INK2)
y-=1.5
for i in range(n):
    ax.text(x0-2,y-i*ch-ch/2,f"i={i}",ha="right",va="center",fontsize=10.5,color=INK2)
    for j in range(n):
        if j<=i: fc="#F1F3F6"; t=""
        else:
            v=f[i][j]; t=str(v)
            fc= GREEN if (i,j)==(0,n-1) else (NAVY_L if v else "white")
        cell(ax,x0+j*cw,y-(i+1)*ch,t,fc=fc,w=cw,h=ch,fs=11.5,bold=(i,j)==(0,n-1),tc="white" if (i,j)==(0,n-1) else INK)
y-=n*ch+8
result(ax,3,y,94,f"máximo de monedas = f[0][5] = {f[0][n-1]}   (último globo: k = {arg[0][n-1]}, el 8)")
save(fig,ax,"p14",y-3)
print(order,f[0][n-1])

# ---------------- P15 ----------------
s,t="horse","ros"; n,m=len(s),len(t)
D=[[0]*(m+1) for _ in range(n+1)]
for i in range(n+1): D[i][0]=i
for j in range(m+1): D[0][j]=j
for i in range(1,n+1):
    for j in range(1,m+1):
        D[i][j]=D[i-1][j-1] if s[i-1]==t[j-1] else 1+min(D[i-1][j-1],D[i-1][j],D[i][j-1])
path=[(n,m)]; ops=[]; i,j=n,m
while i>0 or j>0:
    if i>0 and j>0 and s[i-1]==t[j-1] and D[i][j]==D[i-1][j-1]: ops.append(("=",f"'{s[i-1]}' coincide",0)); i,j=i-1,j-1
    elif i>0 and j>0 and D[i][j]==D[i-1][j-1]+1: ops.append(("R",f"reemplazar '{s[i-1]}' → '{t[j-1]}'",1)); i,j=i-1,j-1
    elif i>0 and D[i][j]==D[i-1][j]+1: ops.append(("D",f"borrar '{s[i-1]}'",1)); i-=1
    else: ops.append(("I",f"insertar '{t[j-1]}'",1)); j-=1
    path.append((i,j))
ops=ops[::-1]
fig,ax,W=new("P15","Programación dinámica","Edit Distance (LeetCode 72)","mínimo de inserciones, borrados y reemplazos para convertir \"horse\" en \"ros\".")
y=-20
step(ax,3,y,1,"D[i][j] = operaciones mínimas para convertir los i primeros de s en los j primeros de t.")
y-=6.5
step(ax,3,y,2,"Si las letras coinciden: D[i−1][j−1]; si no: 1 + mín(reemplazar ↖, borrar ↑, insertar ←).")
y-=9
cw=8.5; ch=5.6; x0=16
for j in range(m+1): ax.text(x0+(j+1)*cw+cw/2,y,("∅" if j==0 else t[j-1]),ha="center",fontsize=13,fontweight="bold",color=NAVY)
y-=2
for i in range(n+1):
    ax.text(x0+cw/2,y-i*ch-ch/2,("∅" if i==0 else s[i-1]),ha="center",va="center",fontsize=13,fontweight="bold",color=ORANGE)
    for j in range(m+1):
        on=(i,j) in path
        fc= GREEN if (i,j)==(n,m) else (YEL if on else "white")
        cell(ax,x0+(j+1)*cw,y-(i+1)*ch,D[i][j],fc=fc,w=cw,h=ch,fs=12.5,bold=on,tc="white" if (i,j)==(n,m) else INK)
# arrows along path
cen=lambda i,j:(x0+(j+1)*cw+cw/2,y-(i+1)*ch+ch/2)
for (i1,j1),(i2,j2) in zip(path[:-1],path[1:]):
    arrow(ax,cen(i2,j2),cen(i1,j1),c=ORANGE,lw=1.8,ms=11,shrink=11)
# ops list right
ox=64; oy=y-2
ax.text(ox,oy,"Camino óptimo (celdas amarillas):",fontsize=11.5,color=INK2,fontweight="bold")
cur=s; k=0; oy-=6
states=["horse"]
w=list(s); pos=0
for sym,txt,c in ops:
    col={ "=":GREEN,"R":ORANGE,"D":RED,"I":NAVY}[sym]
    card(ax,ox,oy-2.3,33,4.6,"",fc="white",ec=col)
    ax.text(ox+1.5,oy,("costo 0  " if c==0 else "costo 1  ")+txt,va="center",fontsize=11,color=INK,zorder=5)
    oy-=5.6
y-=(n+1)*ch+8
ax.text(4,y,"horse  →  rorse (reemplazar h por r)  →  rose (borrar r)  →  ros (borrar e)",fontsize=12,color=INK,fontweight="bold")
y-=8
result(ax,3,y,94,f"distancia de edición = D[5][3] = {D[n][m]}")
save(fig,ax,"p15",y-3)
print(ops)
