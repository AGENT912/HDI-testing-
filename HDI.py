# Yes, my code is hard to read, sorry


# Import libs
import os
import subprocess
import platform
import sys
import colorama
colorama.init()


# Read config file
with open("config.conf", 'r', encoding='utf-8') as file:
    configdata = file.readlines()
file.close()


# Output Header
print(colorama.Fore.WHITE+colorama.Back.BLACK+' ')
print('HDI β6')
print(colorama.Style.RESET_ALL+'—————————')


# Main part
while True:
    cow=input('$').strip() 
    if cow=='index': # Index command
        try:
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

    elif cow=='read': # Read txt file
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
            file.close()
        except:
            print(colorama.Fore.LIGHTRED_EX + '    READ_ERR')
            print(colorama.Fore.WHITE + '    May be name of file is invalid')
            print('    Or your system is do not supported')

    elif cow=='open': # Open file with default application
        try:
            print('Dir:',os.getcwd())
            filepath = os.getcwd() + "/" + input('File:')
            if platform.system() == 'Darwin':       # for macOS
                subprocess.call(('open', filepath))
            elif platform.system() == 'Windows':    # for Windows
                os.startfile(filepath)
            else:                                   # for Pinguins
                subprocess.call(('xdg-open', filepath))
        except:
            print(colorama.Fore.LIGHTRED_EX + '    OPEN_ERR')
            print(colorama.Fore.WHITE + '    May be name of file is invalid')
            print('    Or your system is do not supported')

    elif cow=='chdir': # Change dir
         try:
             os.chdir(input('Dir:'))
             print('Dir will be changed!')
         except:
            print(colorama.Fore.LIGHTRED_EX + '    CHDIR_ERR')
            print(colorama.Fore.WHITE + '    May be path of dir is invalid')
            print('    Or your system is do not supported')

    elif cow=='exit': # For haters)
        sys.exit()

    elif cow=='help': # Help manual
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
        print('  delete file - Delete file')
        print('  delete dir  - Delete empty dir')
        print('  rename      - Rename file or dir')
        print('  copy        - Copy file')
        print('  qr          - Show secret QR-code')
        print('  about       - About HDI')

    elif cow=='del file' or cow=='delete file': # Delete file
        try:
            print('Dir:',os.getcwd())
            os.remove(input('File:'))
            print('File will be deleted!')
        except:
            print(colorama.Fore.LIGHTRED_EX + '    DEL_FILE_ERR')
            print(colorama.Fore.WHITE + '    May be path of file is invalid')
            print('    Or your system is do not supported')

    elif cow=='del dir' or cow=='delete dir': # Delete dir
        dirpath=input('Dir:')
        try:
            os.rmdir(dirpath)
            print('Dir will be deleted')
        except:
            print(colorama.Fore.LIGHTRED_EX + '    DEL_DIR_ERR')
            print(colorama.Fore.WHITE + '    May be name of dir is invalid')
            print('    Or your dir is not empty')
            print('    Or your system is do not supported')

    elif cow=='rename' or cow=='renm': # Rename file or dir
        try:
            print('Current dir:',os.getcwd())
            os.rename(input('File or path of dir:'), input('Rename to:'))
            print('File or dir will be renamed!')
        except:
            print(colorama.Fore.LIGHTRED_EX + '    RENAME_ERR')
            print(colorama.Fore.WHITE + '    May be path of file is invalid')
            print('    Or your system is do not supported')

    elif cow=='create dir' or cow=='cdir': # Create dir
        try:
            os.mkdir(input('Path of new dir:'))
            print('Dir will be created!')
        except:
            print(colorama.Fore.LIGHTRED_EX + '    CREATE_DIR_ERR')
            print(colorama.Fore.WHITE + '    May be path of new dir is invalid')
            print('    Or your system is do not supported')

    elif cow=='cudir': # Show current dir
        print('Current dir:   ',os.getcwd())

    elif cow=='copy': # Copy file
        src = input('Source path:')
        dest = input('Copy to:')
        print(src, dest) 
        try:
            if platform.system() == 'Darwin':       # for macOS
                subprocess.call(('cp', src, dest))
            elif platform.system() == 'Windows':    # for Windows
                subprocess.call(('cmd', '/c', 'copy', src, dest))
            else:                                   # for Pinguins
                subprocess.call(('cp', src, dest))
        except:
            print(colorama.Fore.LIGHTRED_EX + '    COPY_ERR')
            print(colorama.Fore.WHITE + '    May be name of file is invalid')
            print('    Or your system is do not supported')
    
    elif cow=='qr': # Emm, here was be a qr code to NOWKIES Telegram post
        print('Ha!')
        print('What you want to see here?')

    elif cow=='about': # About HDI
        print('')
        print('▓▓▓▓▓▓▓▓▓▓▓▓▒')
        print('▓           ▒       ',colorama.Back.LIGHTWHITE_EX+colorama.Fore.BLACK+'αxi')
        print(colorama.Back.BLACK+colorama.Fore.WHITE+'▓ HDI       ▒')
        print('▓ ────      ▒',colorama.Style.BRIGHT+colorama.Fore.LIGHTWHITE_EX+'       HDI β6')
        print(colorama.Style.RESET_ALL+colorama.Fore.WHITE+'▓ $         ▒')
        print('▓           ▒')
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('')
        print(' HDI it`s a simple open sourse console file manager based on Python3')
        print('')
        print('Developers from AXI:')
        print('  Tr37')
        print('Another Developers')
        print('  Sairsay')
        print('  AGENT912')
        print('')
        print('(C)AXI 2025')

    else: # This SYNTAX else)
        print(colorama.Fore.LIGHTRED_EX+' ')
        print('SYNTAX_ERROR')
        print(colorama.Fore.WHITE+'')

# from AXI in 2025
