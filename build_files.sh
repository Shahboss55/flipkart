echo "BUILD START"
python3 -m ensurepip
python3 -m pip install -r requirements.txt
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"
