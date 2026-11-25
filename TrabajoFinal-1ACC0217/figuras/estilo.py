import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13})
NAVY="#2F5597"; NAVY_L="#DCE6F5"; ORANGE="#D9622B"; ORANGE_L="#FBE3D5"
GREEN="#2E8B57"; GREEN_L="#D9F0E3"; RED="#C93C3C"; RED_L="#F8DADA"
INK="#1E293B"; INK2="#475569"; MUTED="#94A3B8"; LINE="#CBD5E1"; PANEL="#F5F7FB"; YEL="#FFE8A3"
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"png")+os.sep
os.makedirs(OUT,exist_ok=True)
def new(code,tema,titulo,pide,w=10):
    fig=plt.figure(figsize=(w,6)); ax=fig.add_axes([0,0,1,1]); ax.axis("off")
    W=w*10
    ax.add_patch(Rectangle((0,-8.5),W,8.5,fc=NAVY,ec="none"))
    ax.text(2,-4.25,f"{code} · {tema}",color="#C9D8F0",fontsize=12,fontweight="bold",va="center")
    ax.text(2+len(f"{code} · {tema}")*1.05+2.5,-4.25,titulo,color="white",fontsize=14.5,fontweight="bold",va="center")
    ax.add_patch(Rectangle((0,-14),W,5.5,fc=NAVY_L,ec="none"))
    ax.text(2,-11.25,"¿Qué se pide?",color=NAVY,fontsize=12,fontweight="bold",va="center")
    ax.text(17.5,-11.25,pide,color=INK,fontsize=12,va="center")
    ax._W=W
    return fig,ax,W
def card(ax,x,y,w,h,txt="",fc="white",ec=LINE,fs=13,tc=INK,bold=False,lw=1.3,r=0.8,ls="-"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f"round,pad=0,rounding_size={r}",fc=fc,ec=ec,lw=lw,ls=ls,zorder=3))
    if txt!="": ax.text(x+w/2,y+h/2,txt,ha="center",va="center",fontsize=fs,color=tc,fontweight="bold" if bold else "normal",zorder=4)
def cell(ax,x,y,txt,fc="white",ec=INK2,w=4,h=4,fs=13,bold=False,tc=INK):
    ax.add_patch(Rectangle((x,y),w,h,fc=fc,ec=ec,lw=1.1,zorder=3))
    ax.text(x+w/2,y+h/2,str(txt),ha="center",va="center",fontsize=fs,fontweight="bold" if bold else "normal",color=tc,zorder=4)
def step(ax,x,y,n,txt,fs=12.5,c=NAVY):
    ax.add_patch(Circle((x,y),1.7,fc=c,ec="none",zorder=5))
    ax.text(x,y,str(n),ha="center",va="center",color="white",fontsize=11.5,fontweight="bold",zorder=6)
    ax.text(x+2.8,y,txt,va="center",fontsize=fs,color=INK,zorder=6)
def arrow(ax,p,q,c=ORANGE,lw=2,rad=0,ms=16,ls="-",shrink=2):
    ax.add_patch(FancyArrowPatch(p,q,connectionstyle=f"arc3,rad={rad}",arrowstyle="-|>",mutation_scale=ms,color=c,lw=lw,ls=ls,zorder=5,shrinkA=shrink,shrinkB=shrink))
def result(ax,x,y,w,txt,h=6,ok=True):
    card(ax,x,y,w,h,"",fc=GREEN_L if ok else RED_L,ec=GREEN if ok else RED,lw=1.8)
    ax.text(x+2,y+h/2,("✓  " if ok else "✗  ")+txt,va="center",fontsize=13,color=INK,fontweight="bold",zorder=6)
def legend(ax,x,y,items,fs=11.5,gap=None):
    cx=x
    for fc,ec,lab in items:
        ax.add_patch(Rectangle((cx,y-1.2),2.4,2.4,fc=fc,ec=ec,lw=1.2,zorder=5))
        ax.text(cx+3.2,y,lab,va="center",fontsize=fs,color=INK2,zorder=5)
        cx+= 3.2+len(lab)*0.95*fs/11.5+4 if gap is None else gap
def save(fig,ax,name,bottom):
    W=ax._W; ax.set_xlim(0,W); ax.set_ylim(bottom,0)
    fig.set_size_inches(W/10,-bottom/10)
    fig.savefig(OUT+name+".png",dpi=200); plt.close(fig)
