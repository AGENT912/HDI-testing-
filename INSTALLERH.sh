find . -name "HDI.py"
A=$(find . -name "HDI.py")
A="${A%??????}"
cd $A
clear
alias YES="python3 HDI.py"
alias NO="quit"
clear
echo "Would You like to install HDI?(answer is only YES/NO)"
