import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *

# ---------------- P11 ----------------
fig,ax,W=new("P11","Árbol ternario","Design Add and Search Words Data Structure (LeetCode 211)","guardar palabras y buscar patrones donde \".\" vale por cualquier letra.")
y=-20
step(ax,3,y,1,'addWord("bad"), addWord("dad"), addWord("mad") construyen este árbol de búsqueda ternario:')
y-=10
N={"b":(20,0),"a1":(20,1),"d1":(20,2),"d":(50,0),"a2":(50,1),"d2":(50,2),"m":(80,0),"a3":(80,1),"d3":(80,2)}
lab={"b":"b","a1":"a","d1":"d","d":"d","a2":"a","d2":"d","m":"m","a3":"a","d3":"d"}
fin={"d1","d2","d3"}
hl={"b","a1","d1"}  # path of ".ad" success
def P(k): x,d=N[k]; return (x,y-d*11)
for a,b,kind in [("b","a1","eq"),("a1","d1","eq"),("d","a2","eq"),("a2","d2","eq"),("m","a3","eq"),("a3","d3","eq"),("b","d","hi"),("d","m","hi")]:
    (x1,y1),(x2,y2)=P(a),P(b)
    c= GREEN if kind=="hi" else NAVY
    on= a in hl and b in hl
    if kind=="hi": ax.plot([x1+5,x2-5],[y1,y2],color=c,lw=2.4,zorder=2); ax.text((x1+x2)/2,y1+1.6,"hi  (letra mayor)",ha="center",fontsize=11,color=GREEN,fontweight="bold")
    else:
        ax.plot([x1,x2],[y1-2.6,y2+2.6],color=ORANGE if on else c,lw=4 if on else 2.2,zorder=2)
        ax.text(x1+1.5,(y1+y2)/2,"eq",fontsize=11,color=ORANGE if on else NAVY,fontweight="bold",va="center")
# lo null stub from b
ax.plot([N["b"][0]-5,N["b"][0]-12],[y,y],color=MUTED,lw=2,ls="--",zorder=2); ax.text(N["b"][0]-12.5,y,"lo: vacío",ha="right",va="center",fontsize=10.5,color=MUTED)
for k in N:
    x,yy=P(k)
    fc= GREEN_L if k in fin else ("white")
    ec= ORANGE if k in hl else (GREEN if k in fin else NAVY)
    card(ax,x-5,yy-2.6,10,5.2,lab[k]+(" ●" if k in fin else ""),fc=fc,ec=ec,fs=14,bold=True,lw=2.4 if k in hl else 1.4)
ax.text(85.5,y-22,"● = fin de palabra",fontsize=11,color=GREEN,va="center")
y-=2*11+9
step(ax,3,y,2,"Búsqueda: cada letra elige UNA rama (lo si es menor, hi si es mayor, eq si coincide).")
y-=6.5
step(ax,3,y,3,'Con ".", se exploran las tres ramas: lo, hi y eq (la letra del nodo vale como coincidencia).')
y-=9
rows=[('search("pad")','p > b → hi;  p > d → hi;  p > m → hi vacío',False),('search(".ad")','"." en b: eq → a = a → d = d y es fin (camino naranja)',True),('search("b..")','b = b → eq;  "." con a → eq;  "." con d, que es fin',True)]
for q,why,ok in rows:
    card(ax,3,y-2.6,94,5.2,"",fc=GREEN_L if ok else RED_L,ec=GREEN if ok else RED)
    ax.text(5,y,("✓ " if ok else "✗ ")+q+"  →  "+("true" if ok else "false"),va="center",fontsize=12,fontweight="bold",color=INK,zorder=5)
    ax.text(45,y,why,va="center",fontsize=11.2,color=INK,zorder=5)
    y-=6.6
save(fig,ax,"p11",y-1)

# ---------------- P12 ----------------
nums=[3,10,5,25,2,8]; B=5
fig,ax,W=new("P12","Trie","Maximum XOR of Two Numbers in an Array (LeetCode 421)","el mayor valor de a XOR b entre dos números del arreglo.")
y=-20
step(ax,3,y,1,"Cada número se inserta en un trie binario, del bit más alto al más bajo (5 bits aquí):")
y-=7
for i,v in enumerate(nums):
    bx=6+i*15.5
    b=format(v,'05b')
    card(ax,bx,y-3,14,6,"",fc=ORANGE_L if v==25 else (NAVY_L if v==5 else PANEL),ec=ORANGE if v==25 else (NAVY if v==5 else LINE))
    ax.text(bx+7,y+1,str(v),ha="center",fontsize=12,fontweight="bold",color=INK,zorder=5)
    ax.text(bx+7,y-1.5,b,ha="center",fontsize=11,family="monospace",color=INK2,zorder=5)
y-=9
step(ax,3,y,2,"Para 5 = 00101 se busca, en cada nivel, el bit CONTRARIO (así ese bit del XOR vale 1):")
y-=8
# build trie
trie={(): None}
for v in nums:
    b=format(v,'05b')
    for d in range(1,B+1): trie[tuple(b[:d])]=None
levels={d:sorted([k for k in trie if len(k)==d]) for d in range(B+1)}
pos={}
leaves=levels[B]; 
for i,k in enumerate(leaves): pos[k]=8+i*(52/(len(leaves)-1))
for d in range(B-1,-1,-1):
    for k in levels[d]:
        ch=[c for c in levels[d+1] if c[:d]==k]
        pos[k]=sum(pos[c] for c in ch)/len(ch)
path25=[tuple(format(25,'05b')[:d]) for d in range(B+1)]
dy=7
for k in trie:
    if len(k)>0:
        p=k[:-1]; on=k in path25 and p in path25
        ax.plot([pos[p],pos[k]],[y-len(p)*dy,y-len(k)*dy],color=ORANGE if on else LINE,lw=3.5 if on else 1.5,zorder=1)
        ax.text((pos[p]+pos[k])/2+(-1.4 if k[-1]=="0" else 1.4),y-(len(p)+0.5)*dy,k[-1],ha="center",va="center",fontsize=10.5,color=ORANGE if on else INK2,fontweight="bold" if on else "normal")
for k in trie:
    on=k in path25
    ax.add_patch(Circle((pos[k],y-len(k)*dy),1.5,fc=ORANGE if on else "white",ec=ORANGE if on else NAVY,lw=1.5,zorder=3))
for k in leaves:
    v=int(''.join(k),2); ax.text(pos[k],y-B*dy-3.2,str(v),ha="center",fontsize=11.5,fontweight="bold",color=ORANGE if v==25 else INK)
# decision table at right
q=format(5,'05b'); tx=70
y_tab=y
ax.text(tx+12,y_tab+3,"decisión por nivel (q = 5)",ha="center",fontsize=11,color=INK2,fontweight="bold")
for d in range(B):
    want='1' if q[d]=='0' else '0'
    ok=True
    card(ax,tx-1,y_tab-(d+0.5)*dy-2.2,28,4.4,"",fc=GREEN_L,ec=GREEN,lw=1)
    ax.text(tx+0.5,y_tab-(d+0.5)*dy,f"bit {4-d}: q={q[d]} → quiero {want} → existe ✓",fontsize=10.3,color=INK,va="center",zorder=5)
y-=B*dy+10
for lbl,vv,c in [("5 ",5,NAVY),("25",25,ORANGE)]:
    ax.text(30,y,f"{lbl} = {format(vv,'05b')}",fontsize=13,family="monospace",color=c,fontweight="bold",va="center"); y-=4
ax.plot([30,52],[y+1.8,y+1.8],color=INK,lw=1.2)
ax.text(30,y-0.6,f"XOR= {format(5^25,'05b')} = 28",fontsize=13,family="monospace",color=GREEN,fontweight="bold",va="center")
y-=10
result(ax,3,y,94,"máximo XOR = 5 XOR 25 = 28   (cada consulta recorre 31 niveles: O(31·n) en total)")
save(fig,ax,"p12",y-3)

# ---------------- P13 ----------------
fig,ax,W=new("P13","Trie","Concatenated Words (LeetCode 472)","devolver las palabras que se forman uniendo al menos dos palabras más cortas de la lista.")
y=-20
step(ax,3,y,1,"Se procesan por longitud; el trie solo tiene palabras más cortas: cat, cats, dog, rat.")
y-=6
T={"r0":(16,0),"c":(6,1),"d":(16,1),"r":(26,1),"ca":(6,2),"do":(16,2),"ra":(26,2),"cat":(6,3),"dog":(16,3),"rat":(26,3),"cats":(6,4)}
L={"r0":"·","c":"c","d":"d","r":"r","ca":"a","do":"o","ra":"a","cat":"t","dog":"g","rat":"t","cats":"s"}
def P(k): x,d=T[k]; return (x,y-d*7.2)
for a,b in [("r0","c"),("r0","d"),("r0","r"),("c","ca"),("d","do"),("r","ra"),("ca","cat"),("do","dog"),("ra","rat"),("cat","cats")]:
    (x1,y1),(x2,y2)=P(a),P(b); ax.plot([x1,x2],[y1,y2],color=LINE,lw=1.6,zorder=1)
for k in T:
    x,yy=P(k); f=k in ("cat","dog","rat","cats")
    ax.add_patch(Circle((x,yy),2.3,fc=GREEN_L if f else "white",ec=GREEN if f else NAVY,lw=1.6,zorder=3))
    ax.text(x,yy,L[k],ha="center",va="center",fontsize=12.5,fontweight="bold",zorder=4)
    if f: ax.text(x+3,yy,k,va="center",fontsize=10.5,color=GREEN)
ax.text(2,y-4*7.2-5,"verde = fin de palabra",fontsize=11,color=GREEN)
# DP on right
w="catsdogcats"; n=len(w); words={"cat","cats","dog","rat"}
puede=[False]*(n+1); puede[0]=True; arcs=[]
for i in range(n):
    if puede[i]:
        for j in range(i+1,n+1):
            if w[i:j] in words: puede[j]=True; arcs.append((i,j,w[i:j]))
x0=40; cw=4.9; yy=y-14
ax.text(x0+n*cw/2,y-1,'w = "catsdogcats"',ha="center",fontsize=12.5,fontweight="bold",color=INK)
for i,ch in enumerate(w): cell(ax,x0+i*cw,yy,ch,w=cw)
import matplotlib.patches as mp
for (i,j,s) in arcs:
    up=len(s)==3; c=ORANGE if up else NAVY
    yb= yy+4.3 if up else yy-0.3
    ax.add_patch(mp.FancyArrowPatch((x0+i*cw,yb),(x0+j*cw,yb),connectionstyle="arc3,rad=%s"%("-0.5" if up else "0.5"),arrowstyle="-|>",color=c,lw=2,mutation_scale=13,zorder=5))
    ax.text(x0+(i+j)/2*cw,(yb+(j-i)*cw*0.25+1.2) if up else (yb-(j-i)*cw*0.25-2.6),s,ha="center",fontsize=11,color=c,fontweight="bold")
for i in range(n+1):
    ax.add_patch(Circle((x0+i*cw,yy-12),1.4,fc=GREEN if puede[i] else "white",ec=GREEN if puede[i] else MUTED,lw=1.4,zorder=4))
    ax.text(x0+i*cw,yy-15.5,str(i),ha="center",fontsize=9.5,color=MUTED)
ax.text(x0-2,yy-12,"puede",ha="right",va="center",fontsize=11,color=INK2)
y-=4*7.2+11
step(ax,3,y,2,"DP: puede[i] = el prefijo w[0..i) se parte en palabras del trie. Desde cada i alcanzable se")
ax.text(5.8,y-4.5,"recorre el trie y cada nodo fin en la posición j marca puede[j + 1] (arcos).",fontsize=12.5,color=INK,va="center")
y-=14
result(ax,3,y,94,'puede[11] = true: "catsdogcats" = cats + dog + cats  →  es concatenada')
y-=7
ax.text(3,y,'Con la lista oficial se devuelven: catsdogcats, dogcatsdog, ratcatdogcat.',fontsize=11.5,color=INK2)
save(fig,ax,"p13",y-4)
