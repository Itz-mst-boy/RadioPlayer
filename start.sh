echo "Cloning The repo, Please Wait..."
git clone https://github.com/Itz-mst-boy/RadioPlayer /RadioPlayer
echo "Installing All Requirements..."
cd /RadioPlayer
pip3 install -U -r requirements.txt
echo "Ok Starting Bot, Please Wait..."
python3 main.py
