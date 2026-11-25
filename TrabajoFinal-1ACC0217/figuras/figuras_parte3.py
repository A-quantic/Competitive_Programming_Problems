import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *

# ---------------- P09 ----------------
nums=[5,2,6,1]; srt=sorted(set(nums)); rk={v:i+1 for i,v in enumerate(srt)}
fig,ax,W=new("P09","Árbol de Fenwick","Count of Smaller Numbers After Self (LeetCode 315)","para cada nums[i], contar cuántos elementos a su DERECHA son menores.")
y=-20
step(ax,3,y,1,"Compresión de valores a rangos 1..4 y recorrido de derecha a izquierda:")
y-=8; x0=22
ax.text(x0-2,y+2,"nums",ha="right",va="center",fontsize=12,color=INK2); ax.text(x0-2,y-2.6,"rango",ha="right",va="center",fontsize=12,color=INK2)
for i,v in enumerate(nums):
    cell(ax,x0+i*7,y,v,w=7); cell(ax,x0+i*7,y-4.6,rk[v],w=7,fc=PANEL)
arrow(ax,(x0+4*7+4,y-0.4),(x0+4*7+4+0.01,y-0.4),c=WHITE if False else ORANGE) if False else None
ax.annotate("",xy=(x0-0.5,y-8.2),xytext=(x0+28,y-8.2),arrowprops=dict(arrowstyle="-|>",color=ORANGE,lw=2))
ax.text(x0+14,y-10.5,"sentido del recorrido",ha="center",fontsize=11,color=ORANGE)
y-=17
step(ax,3,y,2,"En cada paso: contar los ya vistos con rango menor = query(rango − 1); luego update(rango, +1).")
y-=6
seen=[]; counts=[0]*4; pw=22.5; ph=24
for k,i in enumerate(range(3,-1,-1)):
    v=nums[i]; r=rk[v]; q=sum(1 for s in seen if s<r); counts[i]=q
    px=3+k*(pw+1.5); top=y
    card(ax,px,top-ph,pw,ph,"",fc=PANEL,ec=LINE)
    ax.text(px+pw/2,top-2.6,f"i = {i}: nums = {v} (rango {r})",ha="center",fontsize=11,color=INK,fontweight="bold",zorder=5)
    base=top-17; bw=3.6
    for rr in range(1,5):
        f=seen.count(rr); bx=px+2.5+(rr-1)*(bw+1.3)
        if rr<r: ax.add_patch(Rectangle((bx-0.5,base),bw+1,9.5,fc=NAVY_L,ec="none",zorder=3))
        ax.add_patch(Rectangle((bx,base),bw,max(f,0.04)*3.6,fc=NAVY if f else LINE,ec="none",zorder=4))
        ax.text(bx+bw/2,base-2,str(rr),ha="center",fontsize=10,color=INK2,zorder=5)
        if rr==r: ax.text(bx+bw/2,base+6.3,"+1",ha="center",fontsize=11,color=ORANGE,fontweight="bold",zorder=5)
    ax.text(px+pw/2,top-ph+2.6,f"menores a la derecha = {q}",ha="center",fontsize=11,color=INK,zorder=5)
    seen.append(r)
y-=ph+6
legend(ax,4,y,[(NAVY,NAVY,"rangos ya vistos"),(NAVY_L,NAVY_L,"zona que suma query(rango − 1)")])
ax.text(80,y,"+1 = update(rango)",fontsize=11.5,color=ORANGE,va="center",fontweight="bold")
y-=8
step(ax,3,y,3,"El Fenwick responde cada query y cada update en O(log n): bit[i] guarda la suma de (i − lowbit(i), i].")
y-=7
# fenwick coverage n=8 strip
bx0=8; u=7.5
for i in range(1,9):
    lb=i&-i; l=i-lb
    yy=y-[0,0,3.4,0,6.8,0,3.4,0,10.2][i]
    ax.add_patch(FancyBboxPatch((bx0+l*u+0.4,yy-2.6),lb*u-0.8,2.6,boxstyle="round,pad=0,rounding_size=0.6",fc=ORANGE_L if i in (6,4) else NAVY_L,ec=ORANGE if i in (6,4) else NAVY,lw=1.2,zorder=3))
    ax.text(bx0+l*u+lb*u/2,yy-1.3,f"bit[{i}]",ha="center",va="center",fontsize=10,color=INK,zorder=4)
for i in range(8): ax.text(bx0+i*u+u/2,y-16,str(i+1),ha="center",fontsize=10,color=MUTED)
ax.text(bx0+8*u+4,y-4,"query(6) = bit[6] + bit[4]",fontsize=12,color=ORANGE,va="center",fontweight="bold")
ax.text(bx0+8*u+4,y-8,"2 saltos en vez de sumar 6 casillas",fontsize=11,color=INK2,va="center")
ax.text(bx0+8*u+4,y-12,"update(5): bit[5] → bit[6] → bit[8]",fontsize=11,color=INK2,va="center")
y-=26
result(ax,3,y,94,"counts = [2, 1, 1, 0]")
save(fig,ax,"p09",y-3)

# ---------------- P10 ----------------
nums1=[2,0,1,3]; nums2=[0,1,2,3]; n=4; pos2={v:i for i,v in enumerate(nums2)}
fig,ax,W=new("P10","Árbol de Fenwick","Count Good Triplets in an Array (LeetCode 2179)","contar ternas (x, y, z) que aparecen en el mismo orden en nums1 y en nums2.")
y=-20
step(ax,3,y,1,"Fijar el elemento central y: ternas con y = (x válidos antes) × (z válidos después).")
y-=6.5
step(ax,3,y,2,"Se recorre nums1; el Fenwick, indexado por posición en nums2, cuenta los x ya vistos antes de y.")
y-=8; x0=28
ax.text(x0-2,y+2,"nums1",ha="right",va="center",fontsize=12,color=INK2); ax.text(x0-2,y-2.6,"pos en nums2",ha="right",va="center",fontsize=12,color=INK2)
for i,v in enumerate(nums1): cell(ax,x0+i*7,y,v,w=7); cell(ax,x0+i*7,y-4.6,pos2[v],w=7,fc=PANEL)
y-=12
pw=22.5; ph=27; seen=[]; tot=0
for j,v in enumerate(nums1):
    a=pos2[v]; left=sum(1 for s in seen if s<a); right=(n-1-a)-(j-left); tot+=left*right
    px=3+j*(pw+1.5); top=y
    card(ax,px,top-ph,pw,ph,"",fc=PANEL,ec=GREEN if left*right else LINE,lw=2 if left*right else 1.2)
    ax.text(px+pw/2,top-2.6,f"j = {j}: y = {v}",ha="center",fontsize=11.5,fontweight="bold",color=INK,zorder=5)
    for p in range(n):
        if p==a: fc,t="#D9622B","y"
        elif p in seen and p<a: fc,t=NAVY,"x"
        elif p not in seen and p>a: fc,t=GREEN,"z"
        elif p in seen: fc,t="#B8C1CC",""
        else: fc,t="white",""
        bx=px+2+p*4.8
        card(ax,bx,top-13,4.2,6,t,fc=fc,ec=INK2 if fc=="white" else fc,tc="white",bold=True,fs=12,r=0.4)
        ax.text(bx+2.1,top-15,str(p),ha="center",fontsize=9.5,color=MUTED)
    ax.text(px+pw/2,top-19.5,f"left = {left}   right = {right}",ha="center",fontsize=11,color=INK,zorder=5)
    ax.text(px+pw/2,top-23.5,f"aporta {left}·{right} = {left*right}",ha="center",fontsize=11.5,color=GREEN if left*right else INK2,fontweight="bold",zorder=5)
    seen.append(a)
y-=ph+6
legend(ax,4,y,[(ORANGE,ORANGE,"y"),(NAVY,NAVY,"x válido (lo cuenta el Fenwick)"),(GREEN,GREEN,"z válido"),("#B8C1CC","#B8C1CC","visto, pero después en nums2")],fs=10.5)
y-=5
ax.text(4,y,"right = (posiciones después de y en nums2) − (vistos que quedaron después) = (n − 1 − a) − (j − left)",fontsize=11,color=INK2)
y-=8
result(ax,3,y,94,f"total de ternas buenas = 0 + 0 + 1 + 0 = {tot}   (la terna (0, 1, 3))")
save(fig,ax,"p10",y-3)
