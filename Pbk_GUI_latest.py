#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pbk GUI
"""

import PySimpleGUI as sg
from Pbk_main_function_latest import *

sg.theme('Dark Green 7')


#window layout of two columns
file_list_column = [  [sg.Txt('Polubarinova-Kochina Solution',font = ("Serif", 28,"bold"))],
           [sg.Txt('  ',font = ("Serif", 10))],
           [sg.Txt('Developed by:',font = ("Serif", 15,'bold')),sg.Txt('M.A. Shadab*, E. Hiatt & M.A. Hesse',font = ("Serif", 15))],
           [sg.Txt('The University of Texas at Austin    \ ',font = ("Serif", 15,'italic')),sg.Txt('* mashadab@utexas.edu',font = ("Serif", 15))],
           [sg.Txt('',font = ("Serif", 2))],
           [sg.Txt('Notes: - All units must be consistent.',font = ("Serif", 15))],
           [sg.Txt('            - For low-aspect ratio dams.',font = ("Serif", 15))],
           [sg.Txt('            - Fill checkboxes and enter exactly 4 variables.',font = ("Serif", 15))],
           [sg.Txt('_________________________________________________________',font = ("Serif", 18))],
           [sg.Txt('Input variables ',font = ("Serif", 18,'bold','italic'))],
           [sg.Txt('Units:   Length [e.g. m]',font = ("Serif", 15)), 
            sg.In(size=(4,1), key='-U-',font = ("Serif", 15)),
            sg.Txt(',',font = ("Serif", 20)),
            sg.Txt('Time [e.g. day]',font = ("Serif", 15)),
            sg.In(size=(4,1), key='-U2-',font = ("Serif", 15))],
           [sg.Checkbox('Dam length, L [e.g. 100]',font = ("Serif", 15), default=False, key="-CheckL-"), sg.Txt('                     ',font = ("Serif", 10)),sg.In(size=(8,1), key='-L-',font = ("Serif", 15))],
           [sg.Checkbox('Lower lake height, H  [e.g. 10]',font = ("Serif", 15), default=False, key="-CheckH-"),sg.Txt('        ',font = ("Serif", 10)),sg.In(size=(8,1), key='-H-',font = ("Serif", 15))],
           [sg.Checkbox('Upper lake height, H1  [e.g. 110]',font = ("Serif", 15), default=False, key="-CheckH1-"),sg.Txt(' ',font = ("Serif", 10)),sg.In(size=(8,1), key='-H1-',font = ("Serif", 15))],
           [sg.Checkbox('Specific discharge, Q  [e.g. 1]',font = ("Serif", 15), default=False, key="-CheckQ-"),sg.Txt('         ',font = ("Serif", 10)),sg.In(size=(8,1), key='-Q-',font = ("Serif", 15))],
           [sg.Checkbox('Seepage face height, H0  [e.g. 1]',font = ("Serif", 15), default=False, key="-CheckH0-"),sg.Txt(' ',font = ("Serif", 10)),sg.In(size=(8,1), key='-H0-',font = ("Serif", 15))],
           [sg.Checkbox('Hydraulic conductivity, K  [e.g. 2]',font = ("Serif", 15), default=False, key="-CheckK-"),sg.Txt('',font = ("Serif", 10)),sg.In(size=(8,1), key='-K-',font = ("Serif", 15))],
           [sg.Txt('Free surface resolution:',font = ("Serif", 15)),
            sg.Radio('Low',"RADIO1",font = ("Serif", 15), default=True, key="-CheckLowRes-"),
            sg.Radio('High',"RADIO1",font = ("Serif", 15), default=False, key="-CheckHighRes-"),
            sg.Radio('Very high',"RADIO1",font = ("Serif", 15), default=False, key="-CheckVHRes-")],
           [sg.Txt(' ',font = ("Serif", 2))], 
           [sg.Button('\t   Calculate \t \t ', bind_return_key=True,font = ("Serif", 20,'bold','italic'))],
           [sg.Text("Output Folder  [e.g. /Users/admin/Desktop]",font = ("Serif", 15))],
           [
            sg.In(size=(24,1), key="-FOLDER-",font = ("Serif", 15)),
            sg.FolderBrowse(font = ("Serif", 20)),
            sg.Txt(' ',font = ("Serif", 15)),
            sg.Button('  Save  ', bind_return_key=True,font = ("Serif", 20,'italic','bold'))
            ]
           ]

#for now will only show the name of the chosen file
image_viewer_column = [
           [sg.Txt('Output details',font = ("Serif", 18,'bold','italic'))],
           [sg.Text("Location:",font = ("Serif", 15)),
            sg.Text(size=(50,1), key="-TOUT-",font = ("Serif", 15))],
           [sg.Txt('Seepage face height, H0 :',font = ("Serif", 15)), sg.Txt(size=(30,1), key='-OUTPUT-')  ],
           [sg.Txt('Alpha :',font = ("Serif", 15)),sg.Txt(size=(30,1), key='-OUTPUT1-')  ],
           [sg.Txt('Beta :',font = ("Serif", 15)),sg.Txt(size=(30,1), key='-OUTPUT2-')  ],
           [sg.Txt('C :',font = ("Serif", 15)),sg.Txt(size=(30,1), key='-OUTPUT3-')  ],
           [sg.Txt(' ',font = ("Serif", 2))],
            [sg.Image(size=(600,490),key="-IMAGE-")]
]

layout = [
    [
         sg.Column(file_list_column),
         sg.VSeparator(),
         sg.Column(image_viewer_column),
     ]    
]

window = sg.Window('Polubarinova-Kochina Solution', layout)

while True:
    event, values = window.read()

    if event != sg.WIN_CLOSED:  
        if values['-CheckH-'] == False:
            H = nan
        else: 
            H = float(values['-H-'])
        if values['-CheckH1-'] == False:
            H1 = nan
        else: 
            H1 = float(values['-H1-'])
        if values['-CheckL-'] == False:
            L = nan
        else: 
            L = float(values['-L-'])

        if values['-CheckLowRes-'] == True:
            N = 100
        elif values['-CheckHighRes-'] == True: 
            N = 1000
        else:
            N = 5000
            
        if values['-U-'] == False:
            unit = 'Length-unit'
        else: 
            unit = str(values['-U-'])

        if values['-U2-'] == '':
            Tunit = 'Time-unit'
        else: 
            Tunit = str(values['-U2-'])        
        
        if values['-CheckQ-'] == False:
            Q = nan
        else: 
            Q = float(values['-Q-'])

        if values['-K-'] == False:
            K = nan
        else: 
            K = float(values['-K-'])
        
        
        if values['-FOLDER-'] == '':
            output_folder = ''
        else: 
            output_folder = str(values['-FOLDER-'])
        

        H0, H, L, res, xz_array,Q,K, H1 = PbK_solution_full(nan,H,L,H1,N,output_folder,Q,K,unit,Tunit)
        calc = H0
        calc1 = res[0]
        calc2 = res[1]        
        calc3 = res[2]
        print('Worked')
        if isnan(H0) and isnan(H1) and isnan(res):
            print('Did not work')
            calc = 'Invalid H0'
            calc1 = 'Invalid Alpha'
            calc2 = 'Invalid Beta'
            calc3 = 'Invalid C'

        window['-OUTPUT-'].update(calc,font = ("Serif", 15))
        window['-OUTPUT1-'].update(calc1,font = ("Serif", 15))
        window['-OUTPUT2-'].update(calc2,font = ("Serif", 15))
        window['-OUTPUT3-'].update(calc3,font = ("Serif", 15))
        
        if not output_folder =='':
            filename = f"{output_folder}/L{L}{unit}_H{H}{unit}_H1_{H1}{unit}_N{N}"
            window["-TOUT-"].update(filename,font = ("Serif", 15))
            filename = f"{output_folder}/L{L}{unit}_H{H}{unit}_H1_{H1}{unit}_N{N}/free-surface-profile.png"
            window["-IMAGE-"].update(filename=filename)
    else:
        break

window.close()

'''
#window layout of two columns
file_list_column = [  [sg.Txt('Polubarinova-Kochina Solution',font = ("Serif", 25,"bold"))],
           [sg.Txt('  ',font = ("Serif", 10))],
           [sg.Txt('Notes: - All units must be consistent.',font = ("Serif", 13))],
           [sg.Txt('            - This method only works for low-aspect ratio dams.',font = ("Serif", 13))],
           [sg.Txt('______________________________________________',font = ("Serif", 18))],
           [sg.Txt('Input variables ',font = ("Serif", 18,'bold','italic'))],
           [sg.Txt('Unit [e.g. m]',font = ("Serif", 13))],
           [sg.In(size=(4,1), key='-U-',font = ("Serif", 13))],
           [sg.Txt('Dam length, L  [e.g. 100]',font = ("Serif", 13))],
           [sg.In(size=(8,1), key='-L-',font = ("Serif", 13))],
           [sg.Txt('Lower lake height, H  [e.g. 10]',font = ("Serif", 13))],
           [sg.In(size=(8,1), key='-H-',font = ("Serif", 13))],
           [sg.Txt('Upper lake height, H1  [e.g. 110]',font = ("Serif", 13))],
           [sg.In(size=(8,1), key='-H1-',font = ("Serif", 13))],
           [sg.Txt('Rough number of points at free-surface, N  [e.g. 1000]',font = ("Serif", 13))],
           [sg.In(size=(8,1), key='-N-',font = ("Serif", 13))],
           [sg.Text("Output Folder  [e.g. /Users/admin/Desktop]",font = ("Serif", 13))],
           [
            sg.In(size=(30,1), key="-FOLDER-",font = ("Serif", 13)),
            sg.FolderBrowse(font = ("Serif", 13)),
            ],
           [sg.Txt(' ',font = ("Serif", 5))], 
           [sg.Button('Calculate', bind_return_key=True,font = ("Serif", 15))],
           [sg.Txt('______________________________________________',font = ("Serif", 18))],
           [sg.Txt('',font = ("Serif", 5))], 
            [sg.Txt('About Us',font = ("Serif", 18,'bold','italic'))],
            [sg.Txt('M.A. Shadab, E. Hiatt & M.A. Hesse',font = ("Serif", 15))],
            [sg.Txt('The University of Texas at Austin',font = ("Serif", 15))],
            [sg.Txt('Contact: mashadab@utexas.edu',font = ("Arial", 15))]]

#for now will only show the name of the chosen file
image_viewer_column = [
           [sg.Txt('Output details',font = ("Serif", 18,'bold','italic'))],
           [sg.Text("Location:",font = ("Serif", 13)),
            sg.Text(size=(50,1), key="-TOUT-",font = ("Serif", 13))],
           [sg.Txt('Seepage face height, H0 :',font = ("Serif", 13)), sg.Txt(size=(30,1), key='-OUTPUT-')  ],
           [sg.Txt('Alpha :',font = ("Serif", 13)),sg.Txt(size=(30,1), key='-OUTPUT1-')  ],
           [sg.Txt('Beta :',font = ("Serif", 13)),sg.Txt(size=(30,1), key='-OUTPUT2-')  ],
           [sg.Txt('C :',font = ("Serif", 13)),sg.Txt(size=(30,1), key='-OUTPUT3-')  ],
           [sg.Txt('Free surface profile:',font = ("Serif", 13))],
           [sg.Txt(' ',font = ("Serif", 2))],
            [sg.Image(size=(600,490),key="-IMAGE-")],
]

layout = [
    [
         sg.Column(file_list_column),
         sg.VSeparator(),
         sg.Column(image_viewer_column),
     ]    
]

window = sg.Window('Polubarinova-Kochina Solution', layout)

while True:
    event, values = window.read()

    if event != sg.WIN_CLOSED:
        try:
            H = float(values['-H-'])
            H1 = float(values['-H1-'])
            L = float(values['-L-'])
            N = int(values['-N-'])
            unit = str(values['-U-'])
            output_folder = str(values['-FOLDER-'])            
            H0, res, xz_array = PbK_solution(H,L,H1,N,output_folder,unit)
            calc = H0*H1
            calc1 = res[0]
            calc2 = res[1]        
            calc3 = res[2]
        except:
            calc = 'Invalid H0'
            calc1 = 'Invalid Alpha'
            calc2 = 'Invalid Beta'
            calc3 = 'Invalid C'

        window['-OUTPUT-'].update(calc,font = ("Serif", 13))
        window['-OUTPUT1-'].update(calc1,font = ("Serif", 13))
        window['-OUTPUT2-'].update(calc2,font = ("Serif", 13))
        window['-OUTPUT3-'].update(calc3,font = ("Serif", 13))
        
        filename = f"{output_folder}/L{L}{unit}_H{H}{unit}_H1_{H1}{unit}_N{N}"
        window["-TOUT-"].update(filename,font = ("Serif", 13))
        filename = f"{output_folder}/L{L}{unit}_H{H}{unit}_H1_{H1}{unit}_N{N}/free-surface-profile.png"
        window["-IMAGE-"].update(filename=filename)
    else:
        break
'''