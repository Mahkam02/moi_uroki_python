# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:59:10 2023

@author: Mahkam
"""

#1
Al_Xorezmiy={'imya':'Al_Xorezmiy',
            'god rojdeniya':783,
            'kem bil':'matematik',
            'mesto rojdeniya':'Xorezm',
            'trudi':['Kitab al-jabr', 'KItab surat al-ard']}
Al_Farabiy={'imya':'Al_Farabiy',
            'god rojdeniya':870,
            'kem bil':'filosof',
            'mesto rojdeniya':'Farab',
            'trudi':['O misle razuma', 'Kniga vvedeniya v logiku']}
Al_Beruniy={'imya':'Al_Beruniy',
            'god rojdeniya':973,
            'kem bil':'geograf',
            'mesto rojdeniya':'Kyat',
            'trudi':['Indiya', 'Xronologiya']}
Mirza_Ulugbek={'imya':'Mirza_Ulugbek',
                'god rojdeniya':1394,
                'kem bil':'astronom',
                'mesto rojdeniya':'Soltaniye',
                'trudi':['Zidji jadidi Guragani', 'Zidj Ulugbeka']}
uchyonie=[Al_Xorezmiy, Al_Farabiy, Al_Beruniy, Mirza_Ulugbek]
for a in uchyonie:
    print(f"{a['imya']} rodilsya v {a['god rojdeniya']}-godu v gorode {a['mesto rojdeniya']}")
    
#2
for b in uchyonie:
    print(f"\n{b['imya']} napisal trudi kak:")
    for c in b['trudi']:
        print(c)
        
#3
cinemas={'dad':['Otalar so\'zi', 'Sardor'],
          'mum':['Qara sevda', 'Ishani'],
          'brother':['Terminator', 'Purpurnie serdca']}
for a1 in cinemas.keys():
    print(f'\nMy {a1} likes cinemas:')
    for cinema in cinemas[a1]:
        print(cinema)
        
#4
strani={
    'Uzbekistan':
            {'stolica':'Tashkent',
            'ploshad':'448tis.',
            'valyuta':'uzb sum'},
    'Kazaxstan':
        {'stolica':'Astana',
          'ploshad':'2724tis.',
          'valyuta':'tenge'},
        'Kirgizstan':
            {'stolica':'Bishkek',
              'ploshad':'199tis.',
              'valyuta':'som'}
            }

for strana, info in strani.items():
    print(f"\nStolica {strana}a {info['stolica']}.\
\nPloshad {info['ploshad']} kv.km.\
\nValyuta {info['valyuta']}.")

# 5
strana1=input('\nKakuyu stranu xotite znat?>>>').title()
if strana1 in strani.keys():
    print(f"\nStolica {strana1}a {strani[strana1]['stolica']}.\
\nPloshad {strani[strana1]['ploshad']} kv.km.\
\nValyuta {strani[strana1]['valyuta']}.")
else:
    print('U nas net informacii ob etoy strane')