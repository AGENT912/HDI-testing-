#Yes, my code is hard to read, sorry

import os
import subprocess
import platform
import sys
import colorama
colorama.init()
print(colorama.Fore.WHITE+colorama.Back.BLACK+' ')
print('HDI β RCD.1.0')
print(colorama.Style.RESET_ALL+'—————————')

while True:
    cow=input('$').strip() # strip уберет пробелы слева и справа
    if cow=='index':
        try:
            os.chdir(input('Dir:'))
            print(' ')
            print('Contents of', os.getcwd())
            print('------------------------------------------------------------------')
            print('| Type  | Name            | Size                                 |')
            print('|-------|-----------------|--------------------------------------|')
            for item in os.listdir():
                if os.path.isfile(item):
                    print('| File: | ' + item + ' | ' + str(os.path.getsize(item)) + ' bytes |')
                if os.path.isdir(item):
                   print('| Dir:  | ' + item + ' | ' + str(os.path.getsize(item)) + ' bytes |')
            print('------------------------------------------------------------------')
        except:
            print(colorama.Fore.LIGHTRED_EX + '    INDEX_ERR')
            print(colorama.Fore.WHITE + '    May be path of dir is invalid')
            print('    Or your system is do not supported')
    elif cow=='read':
        try:
            print('Dir:',os.getcwd())
            with open(input('File:'), 'r') as file:
                contenta = file.read()
            print(colorama.Fore.LIGHTBLACK_EX+'------------------')
            print(colorama.Fore.LIGHTBLUE_EX+' ')
            print(contenta)
            print(colorama.Fore.LIGHTBLUE_EX+' ')
            print(colorama.Fore.LIGHTBLACK_EX+'------------------')
            print(colorama.Fore.WHITE+'')
        except:
            print(colorama.Fore.LIGHTRED_EX + '    READ_ERR')
            print(colorama.Fore.WHITE + '    May be name of file is invalid')
            print('    Or your system is do not supported')
    elif cow=='open':
        try:
            print('Dir:',os.getcwd())
            filepath = os.getcwd() + "/" + input('File:')
            if platform.system() == 'Darwin':       # для macOS
                subprocess.call(('open', filepath))
            elif platform.system() == 'Windows':    # для Windows
                os.startfile(filepath)
            else:                                   # Для linux. На телефоне может и не сработать
                subprocess.call(('xdg-open', filepath))
        except:
            print(colorama.Fore.LIGHTRED_EX + '    OPEN_ERR')
            print(colorama.Fore.WHITE + '    May be name of file is invalid')
            print('    Or your system is do not supported')
    elif cow=='chdir':
         try:
             os.chdir(input('Dir:'))
             print('Dir will be changed!')
         except:
            print(colorama.Fore.LIGHTRED_EX + '    CHDIR_ERR')
            print(colorama.Fore.WHITE + '    May be path of dir is invalid')
            print('    Or your system is do not supported')
    elif cow=='exit':
        sys.exit()
    elif cow=='help':
        print(colorama.Fore.CYAN + 'HDI β1.0 Help Guide')
        print(colorama.Fore.WHITE + 'Commands:')
        print('  index       - Show directory contents')
        print('  read        - Read a text file')
        print('  open        - Open a file with default app')
        print('  chdir       - Change current directory')
        print('  cdir        - Create dir')
        print('  cudir       - Show current dir')
        print('  exit        - Exit the program')
        print('  help        - Show this guide')
        print('  delite file - Delite file')
        print('  delite dir  - Delite empty dir')
        print('  rename      - Rename file or dir')
        print('  copy        - Copy file')
        print('  qr          - Show secret QR-code')
        print('  credits     - Show creators')
    elif cow=='del file' or cow=='delite file':
        print('Dir:',os.getcwd())
        os.remove(input('File:'))
        print('File will be delited!')
    elif cow=='del dir' or cow=='delite dir':
        dirpath=input('Dir:')
        try:
            os.rmdir(dirpath)
            print('Dir will be delited')
        except:
            print(colorama.Fore.LIGHTRED_EX + '    DELDIR_ERR')
            print(colorama.Fore.WHITE + '    May be name of dir is invalid')
            print('    Or your dir is not empty')
            print('    Or your system is do not supported')
    elif cow=='rename' or cow=='renm':
        print('Current dir:',os.getcwd())
        os.rename(input('File or path of dir:'), input('Rename to:'))
        print('File or dir will be renamed!')
    elif cow=='create dir' or cow=='cdir':
        os.mkdir(input('Path of new dir:'))
        print('Dir will be created!')
    elif cow=='cudir':
        print('Current dir:   ',os.getcwd())
    elif cow=='copy': 
        src = input('Source path:')
        dest = input('Copy to:')
        print(src, dest) 
        try:
            if platform.system() == 'Darwin':       # для macOS
                subprocess.call(('cp', src, dest))
            elif platform.system() == 'Windows':    # для Windows
                subprocess.call(('cmd', '/c', 'copy', src, dest))
            else:                                   # Для linux.
                subprocess.call(('cp', src, dest))
        except:
            print(colorama.Fore.LIGHTRED_EX + '    COPY_ERR')
            print(colorama.Fore.WHITE + '    May be name of file is invalid')
            print('    Or your system is do not supported')
    elif cow=='qr':
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')       
        print('@@@                @@@@@  @@@@@     @@               @@                @@@')         
        print('@@@  @@@@@@@@@@@@  @@     @@@@@       @@@  @@@      @@@  @@@@@@@@@@@@  @@@')       
        print('@@@  @@        @@  @@@@@     @@@@@    @@@@@     @@   @@  @@        @@  @@@')      
        print('@@@  @@       .@@  @@+    @@@@@  @@@@@     @@@@@  @@@@@  @@+       @@  @@@')   
        print('@@@  @@        @@  @@@         @@   @@  @@@@@   @@@@@@@  @@        @@  @@@') 
        print('@@@  @@@@@@@@@@@@  @@@  @@.  @@@@          @@@@@     @@  @@@@@@@@@@@@  @@@') 
        print('@@@                @@+  @@   @@  @@@  @@@  @@   @@  @@@                @@@') 
        print('@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@  @@@    @@@  @@@    @@@@@@@@@@@@@@@@@@@@@@') 
        print('@@@@@  @@@     @@       @@@@@@@@@            @@@@@@@   @@       @@   @@@@@')           
        print('@@@       @@  @@@@@@@@     @%     @@  @@@  @@     @@          @@@@@@@   @@')           
        print('@@@  @@@  @@            @@@@@@@@@@@@@@   @@  @@@@@@@@@@       @@@@@@@@@@@@')          
        print('@@@@@  :@@@@@@@@@@@     @@   @@       @@@       @@  @@@         @@@@@  @@@')           
        print('@@@  @@@@@  @@@@@  @@@    @@@    @@@@@@@   @@   @@     @@          @@  @@@')           
        print('@@@     @@@@     @@       @@@  @@     @@@@@@@     @@@@@  @@@@@  @@@@@  @@@')           
        print('@@@@@  @@@@@@@@@@  @@@@@  @@@  @@.  @@          @@@@@@@         @@%  @@@@@')           
        print('@@@@@  @@@     @@@@     @@   @@@@     @@@@@@@@@@  @@       +@@@@   @@   @@')           
        print('@@-            @@  @@@@@@@@@@@@@@@@@  @@@@@@@     @@@@@  @@@@@@@@@@  @@@@@')           
        print('@@@@@@@@@@  @@@@@@@   @@@@     @@@@@@@@@   @@@@@@@     @@@@        @@@@@@@')        
        print('@@@@@@@@@@@@   @@     @@  @@@@@       @@   @@@@@@@@@@  @@  @@@  @@@  @@@@@')     
        print('@@@       @@   @@@@@@@@@@@     @@@@@  @@@@@@@                 @@@@@  @@@@@')           
        print('@@@  @@@@@  @@@@@  @@@@@@@.         @@@@   @@@@@              @@   @@  @@@')           
        print('@@@@@@@@@@@@@@@@@@@@@+       @@  @@@  @@@    -@@    @@@@@@@@  @@   @@  @@@')
        print('@@@                @@+  @@   @@          @@@@@@@    @@@  @@+  @@@@@@@@@@@@')       
        print('@@  @@@@@@@@@@@@  @@@@@@@@@@  @@@@@  @@@@@  @@@    @@@@@@@@       @@  @@@ ')    
        print('@@@  @@        @@  @@+    @@@  @@   @@   @@  @@@@@            @@       @@@')   
        print('@@@  @@       .@@  @@+  @@       @@@         @@@@@@@@  @@  +@@  @@@@@@@@@@')
        print('@@@  @@        @@  @@@@@@@   @@@@   @@  @@@@@            @@@@@       @@@@@')
        print('@@@  @@@@@@@@@@@@  @@     @@@@@  @@@@@     @@@@@    @@@@@   @@    @@@@@@@@')        
        print('@@@                @@@@@@@@@%  @@     @@@  @@   @@@@@@@@@@@   @@     @@@@@')        
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    elif cow=='credits':
        print('(C)AXI 2025')
        print('  Tr37')
        print(' Special thanks')
        print('  Sairsay')
        print('  AGENT912')
    else:
        print(colorama.Fore.LIGHTRED_EX+' ')
        print('SYNTAX_ERR')
        print(colorama.Fore.WHITE+'')
#(C)AXI 2025
