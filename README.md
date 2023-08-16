# Boston House Pricing Prediction


## Workflows
```bash
# Create a new environment
conda create -p venv python==3.7 -y

# Activate the environment
conda activate venv/

# Install requirements
pip install -r requirements.txt

# Set git repository & global options
git config --global user.name <user_name>
git config --global user.email <email>

# List all variables set in config file, along with their values.
git config -l

# Run web application
python app.py

# Test application via Postman
POST http://127.0.0.1:5000/predict_api
raw:
{
    "data": {
        "CRIM": 0.00632,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0.0,
        "NOX": 0.538,
        "RM": 6.575,
        "Age": 65.2,
        "DIS": 4.0900,
        "RAD": 1.0,
        "TAX": 296,
        "PTRATIO": 15.3,
        "B": 396.90,
        "LSTAT": 4.98
    }
}
```

# Test application via Web-UI
> http://127.0.0.1:5000/predict