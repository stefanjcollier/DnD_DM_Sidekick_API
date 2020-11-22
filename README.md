# D&D DM Sidekick API

 The backend API to the 'DM Sidekick' tool
 

# Requirements
- Python 3.9
- Pipenv

# Installation
```bash
git clone git@github.com:stefanjcollier/DnD_DM_Sidekick_API.git
cd DnD_DM_Sidekick_API

# Install python packages
pipenv install

# Create database with tables
python manage.py migrate
```

# Run
```bash
cd DnD_DM_Sidekick_API
pipenv shell
python manage.py runserver
```

# Test
No testing yet 😅
