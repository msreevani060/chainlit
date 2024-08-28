echo [$(date)]:"START"
echo [$(date)]:"Creating conda environment with python 3.9"
conda create --prefixt ./env python=3.9 -y
echo [$(date)]: "created conda env"
source activate ./env
echo [$(date)]:"activated conda env"
echo [$(date)]:"installing requirements"
pip install -r requirements.txt
echo [$(date)]:"installed all requirements"
echo [$(date)]: "END"