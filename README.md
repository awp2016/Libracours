[![Build Status](https://travis-ci.org/awp2016/Libracours.svg?branch=master)](https://travis-ci.org/awp2016/Libracours)
# [Libracours](https://drive.google.com/open?id=1z4R4XMqrmVXvlhJIcYaFKoqQzIJns88wmR9dVgXdxOc)

### How to install and run (*nix friendly guide)
#### Prerequisites

1. Install pip

  ```
  wget https://bootstrap.pypa.io/get-pip.py
  sudo python get-pip.py
  ```

2. Install virtualenv (Optional but highly recommended)

  ```
  sudo pip install virtualenv
  ```

#### Download, set up and run the project
1. Clone the repository

  ```
  git clone https://github.com/awp2016/Libracours
  ```
2. Change current directory to the project's folder

  ```
  cd Libracours
  ```
3. Create and activate the virtual environment (Optional)

  ```
  virtualenv venv
  source venv/bin/activate
  ```
  The virtual environment's name should appear before your username in the terminal prompt if it has been properly activated:```(venv) alexandra@Mereu:<current_path>$``` instead of ```alexandra@Mereu:<current_path>$```

4. Install requirements

  ```
  pip install -r requirements.txt
  ```

5. Apply migrations

  ```
  ./manage.py migrate
  ```

6. Create superuser (Optional)

  ```
  ./manage.py createsuperuser
  ```

7. Run development server

  ```
  ./manage.py runserver
  ```

### Guidelines for contributors
Before contributing please make sure you follow these guidelines:

1. Configure your editor to use **spaces** instead of **tabs** and set the **tab size** to **4**.
2. **Naming convention**: use ```UpperCamelCase``` for **class names**, ```CAPITALIZED_WITH_UNDERSCORES``` for **constants**, and ```lowercase_separated_by_underscores``` for **other names**.
3. Use a **PEP8 validator** to ensure your Python code is compliant with PEP8.
