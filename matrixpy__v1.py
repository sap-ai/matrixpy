class matrix:
   def build(self, rap):
      l = self.split()
      ll = len(l)
      art = ""
      for i in range(round(ll / rap)):
         for x in range(rap):
            art += l[i]
            if x != rap:
               art += " "
         if i != (round(ll / rap)):
            art += "\n"
      return art
   def __mul__(self, other):
      i = 0
      rap = 1
      n = 0
      nl = []
      fl = []
      sv = self
      ov = other
      while True:
         if sv[i:i+1] == " ":
            rap += 1
         else:
            if sv[i:i+1] == "\n":
               break
      ss = sv.split()
      for i in range(round(ss / rap)):
         for x in range(rap):
            n += int(ss[i])
         nl.append(n)
         n = 0
      rap = 1
      while True:
         if ov[i:i+1] == " ":
            rap += 1
         else:
            if ov[1:1+1] == "\n":
               break
      osp = ov.split()
      ospl = len(osp)
      e = 0
      for i in range(round(ospl / rap)):
         for x in range(rap):
            fl.append(str(int(osp[x+e]) * nl[x]))
            e += 1
      e = 0
      fll = len(fl)
      ctt = ""
      for i in range(round(fll / rap)):
         for x in range(rap):
            ctt += fl[x]
            if rap != x:
               ctt += " "
         if i != (round(fll / rap)):
            ctt += "\n"
      return ctt
   def __add__(self, other):
      i = 0
      rap = 1
      n = 0
      nl = []
      fl = []
      sv = self
      ov = other
      while True:
         if sv[i:i+1] == " ":
            rap += 1
         else:
            if sv[i:i+1] == "\n":
               break
      ss = sv.split()
      for i in range(round(ss / rap)):
         for x in range(rap):
            n += int(ss[i])
         nl.append(n)
         n = 0
      rap = 1
      while True:
         if ov[i:i+1] == " ":
            rap += 1
         else:
            if ov[i:i+1] == "\n":
               break
      osp = ov.split()
      ospl = len(osp)
      e = 0
      for i in range(round(ospl / rap)):
         for x in range(rap):
            fl.append(str(int(osp[x+e]) + nl[x]))
            e += 1
      e = 0
      fll = len(fl)
      ctt = ""
      for i in range(round(fll / rap)):
         for x in range(rap):
            ctt += fl[x]
            if rap != x:
               ctt += " "
         if i != (round(fll / rap)):
            ctt += "\n"
      return ctt
   def __min__(self, other):
      i = 0
      rap = 1
      n = 0
      nl = []
      fl = []
      sv = self
      ov = other
      while True:
         if sv[i:i+1] == " ":
            rap += 1
         else:
            if sv[i:i+1] == "\n":
               break
      ss = sv.split()
      for i in range(round(ss / rap)):
         for x in range(rap):
            n += int(ss[i])
         nl.append(n)
         n = 0
      rap = 1
      while True:
         if ov[i:i+1] == " ":
            rap += 1
         else:
            if ov[1:i+1] == "\n":
               break
      osp = sv.split()
      ospl = len(osp)
      e = 0
      for i in range(round(ospl / rap)):
         for x in range(rap):
            fl.append(int(osp[x+e]) - nl[x])
            e += 1
      e = 0
      fll = len(fl)
      ctt = ""
      for i in range(round(fll / rap)):
         for x in range(rap):
            ctt += fl[x]
            if rap != x:
               ctt += " "
         if i != (round(fll / rap)):
            ctt += "\n"
      return ctt
   def __div__(self, other):
      i = 0
      rap = 1
      n = 0
      nl = []
      fl = []
      sv = self
      ov = other
      while True:
         if sv[i:i+1] == " ":
            rap += 1
         else:
            if sv[i:i+1] == "\n":
               break
      ss = sv.split()
      for i in range(round(ss / rap)):
         for x in range(rap):
            n += int(ss[i])
         nl.append(n)
         n = 0
      rap = 1
      while True:
         if ov[i:i+1] == " ":
            rap += 1
         else:
            if ov[i:i+1] == "\n":
               break
      osp = ov.split()
      ospl = len(osp)
      e = 0
      for i in range(round(ospl / rap)):
         for x in range(rap):
            fl.append(int(osp[x+e]) / nl[x])
            e += 1
      e = 0
      fll = len(fl)
      ctt = ""
      for i in range(round(fll / rap)):
         for x in range(rap):
            ctt += fl[x]
            if rap != x:
               ctt += " "
         if i != (round(fll / rap)):
            ctt += "\n"
      return ctt
