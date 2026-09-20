import pandas as pd


class Player:

    def __init__(self, club=None, name='Player', crv=50, df=50, dri=50, fka=50, pac=50, pas=50, pen=50, phy=50, pos=50,
                 pwr=50):
        self.club = club
        self.name = name
        self.crv = crv
        self.df = df
        self.dri = dri
        self.fka = fka
        self.pac = pac
        self.pas = pas
        self.pen = pen
        self.phy = phy
        self.pos = pos
        self.pwr = pwr
        self.ovr = (self.pen + self.crv + self.dri + self.fka + self.df + self.pac + self.pas + self.phy +
                    self.pos + self.pwr) / 10


ronaldo = Player('Juventus', 'Cristiano Ronaldo', 81, 28, 89, 76, 91, 82, 85, 85, 95, 95)
messi = Player('F.C Barcelona', 'Leo Messi', 93, 32, 97, 94, 84, 91, 75, 82, 94, 86)
neymar = Player('PSG', 'Neymar', 88, 32, 96, 89, 89, (87 + 87 + 81) // 3, 92, 80, 87, 80)

dtf = pd.DataFrame([{'Name': ronaldo.name, 'CRV': ronaldo.crv, 'DEF': ronaldo.df,
                     'DRI': ronaldo.df, 'FKA': ronaldo.fka,
                     'PAC': ronaldo.pac, 'PAS': ronaldo.pas, 'PEN': ronaldo.pen, 'PHY': ronaldo.phy,
                     'POS': ronaldo.pos, 'PWR': ronaldo.pwr, 'OVR': ronaldo.ovr},
                    {'Name': messi.name, 'CRV': messi.crv, 'DEF': messi.df,
                     'DRI': messi.df, 'FKA': messi.fka,
                     'PAC': messi.pac, 'PAS': messi.pas, 'PEN': messi.pen, 'PHY': messi.phy,
                     'POS': messi.pos, 'PWR': messi.pwr, 'OVR': messi.ovr},
                    {'Name': neymar.name, 'CRV': neymar.crv, 'DEF': neymar.df,
                     'DRI': neymar.df, 'FKA': neymar.fka,
                     'PAC': neymar.pac, 'PAS': neymar.pas, 'PEN': neymar.pen, 'PHY': neymar.phy,
                     'POS': neymar.pos, 'PWR': neymar.pwr, 'OVR': neymar.ovr}])

dtf['Club'] = [ronaldo.club, messi.club, neymar.club]
dtf = dtf.set_index(['Name', 'Club'])
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)
dtf = dtf.sort_values('OVR', ascending=False)
print(dtf, '\n')
lewandoski = Player('Bayern Munich', 'Robert Lewandoski', 79, 32, 85, 85, 76, (71+82+70) // 3, 88, 80, 93, 88)
lewa = pd.Series({'Name': lewandoski.name, 'CRV': lewandoski.crv, 'DEF': lewandoski.df, 'DRI': lewandoski.dri,
                  'FKA': lewandoski.fka, 'PAC': lewandoski.pac, 'PAS': lewandoski.pas, 'PEN': lewandoski.pen,
                  'PHY': lewandoski.phy, 'POS': lewandoski.pos, 'PWR': lewandoski.pwr, 'OVR': lewandoski.ovr,
                  'Club': lewandoski.club})
dtf = dtf.reset_index()
dtf = dtf.append(lewa, ignore_index=True)
dtf = dtf.set_index(['Name', 'Club'])
print(dtf, '\n')

salah = Player('Liverpool', 'Mohamed Salah', 83, (38+41+43)//3, 90, 69, 92, (79+84+75)//3, 81, 86, 91, 80)
sala = pd.Series({'Name': salah.name, 'CRV': salah.crv, 'DEF': salah.df, 'DRI': salah.dri,
                  'FKA': salah.fka, 'PAC': salah.pac, 'PAS': salah.pas, 'PEN': salah.pen,
                  'PHY': salah.phy, 'POS': salah.pos, 'PWR': salah.pwr, 'OVR': salah.ovr,
                  'Club': salah.club})
dtf = dtf.reset_index()
dtf = dtf.append(sala, ignore_index=True)
dtf = dtf.set_index(['Name', 'Club'])
dtf = dtf.sort_values('OVR', ascending=False)
print(dtf, '\n')

rohit = Player('Real Madrid', 'Rohit Rasam')
roh = pd.Series({'Name': rohit.name, 'CRV': rohit.crv, 'DEF': rohit.df, 'DRI': rohit.dri,
                 'FKA': rohit.fka, 'PAC': rohit.pac, 'PAS': rohit.pas, 'PEN': rohit.pen,
                 'PHY': rohit.phy, 'POS': rohit.pos, 'PWR': rohit.pwr, 'OVR': rohit.ovr,
                 'Club': rohit.club})
dtf = dtf.reset_index()
dtf = dtf.append(roh, ignore_index=True)
dtf = dtf.set_index(['Club', 'Name'])
dtf = dtf.sort_values('OVR', ascending=False)
print(dtf, '\n')
# dtf.to_csv('FIFA.csv')
