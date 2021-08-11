# 此代码转载于：https://gitbook.cn/books/5b31faa8c70aaa69f465dbd5/index.html
# 请保护原作者，谢谢
"""
三体问题求解
"""

from scipy.integrate import odeint
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy

def Three(w,t,M1,M2,M3):
      """
      三体问题微分方程
      """
      # 三个星体的速度和位置
      v1x,v1y,v2x,v2y,v3x,v3y,x1,y1,x2,y2,x3,y3= w
      # 星体距离
      r12=np.sqrt((x1-x2)**2+(y1-y2)**2)
      r23=np.sqrt((x3-x2)**2+(y3-y2)**2)
      r13=np.sqrt((x1-x3)**2+(y1-y3)**2)
      # 万有引力定律
      rv1x=M2*(x2-x1)/r12**3+M3*(x3-x1)/r13**3
      rv1y=M2*(y2-y1)/r12**3+M3*(y3-y1)/r13**3
      rv2x=M1*(x1-x2)/r12**3+M3*(x3-x2)/r23**3
      rv2y=M1*(y1-y2)/r12**3+M3*(y3-y2)/r23**3
      rv3x=M2*(x2-x3)/r23**3+M1*(x1-x3)/r13**3
      rv3y=M2*(y2-y3)/r23**3+M1*(y1-y3)/r13**3
      # 速度与位置关系
      rx1=v1x
      ry1=v1y
      rx2=v2x
      ry2=v2y
      rx3=v3x
      ry3=v3y
      return np.array([rv1x,rv1y,rv2x,rv2y,rv3x,rv3y,rx1,ry1,rx2,ry2,rx3,ry3])

t = np.arange(0,6000, 0.01) # 创建时间点 
# 调用ode对三体问题进行求解
track1 = odeint(Three, (0,-2,0.1,0.2,0.21,0.1,2,2.1,-2,-2,-2,2), t, args=(6.4,6.4,7.4))
# 绘图
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use("ggplot")

fig = plt.figure()
ax=fig.add_subplot(111);
ax.set_xlabel("X(km)")
ax.set_ylabel("Y(km)")
ax.set_title("Three-body")

plt.axis('equal')
def update_lines(dt):
      plt.cla()
      d=int(dt*600)
      # plt.xlim([-50,50])
      # plt.ylim([-50,50])
      plt.text(4,6, 'T='+str(dt)+'s')
      plt.text(-2,-6, r'Three-body Problem@RS')
      ax.plot(track1[d:d+1, 6], track1[d:d+1, 7],'o')
      ax.plot(track1[d:d+1, 8], track1[d:d+1, 9],'o')
      ax.plot(track1[d:d+1, 10], track1[d:d+1, 11],'o')

      ax.plot(track1[0:d, 6], track1[0:d, 7],color='cornflowerblue',lw=2,alpha=0.5)
      ax.plot(track1[0:d, 8], track1[0:d, 9],color='orange',lw=2,alpha=0.5)
      ax.plot(track1[0:d, 10], track1[0:d, 11],color='b',lw=2,alpha=0.5)
      return mplfig_to_npimage(fig)

# 输出动画
animation =mpy.VideoClip(update_lines, duration=39)
animation.write_gif("long.gif", fps=5)