# 1. Run the venv
.\.photogallery\Scripts\Activate.ps1

# 2. Upgrade the pip 
pip install --upgrade pip

# 3. Install all the depedencies
flask
flask_bootstrap

# 4. Install boto3 (sdk from amazon s3)
pip3 --no-cache-dir install --upgrade boto3

# If you are running app in powershell and are having permissions issues
Set-ExecutionPolicy → unrestricted 