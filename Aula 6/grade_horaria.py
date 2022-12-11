def compromisso_no_periodo(grade_horaria, dia, periodo):
    if(grade_horaria[periodo][dia] == ''): return 'Livre'
    else: return grade_horaria[periodo][dia]

# grade_horaria = [
#     ['GDE',     'Tópicos', 'NatDes',  'Tópicos',   ''         ],
#     ['DesSoft', 'GDE',     'DesSoft', 'InstruMed', 'NatDes'   ],
#     ['ModSim',  '',        '',        '',          ''         ],
#     ['',        'ModSim',  '',        'ModSim',    'InstruMed']
# ]

# print(compromisso_no_periodo(grade_horaria, 4, 2))