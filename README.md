Chapter 13 will focus on installation of packages with pip and hence will not have a whole exercise to go alongside.



python -m pip --version
<img width="283" height="36" alt="image" src="https://github.com/user-attachments/assets/7c185b64-3940-477a-83cd-c1ed70707316" />



python -m pip install --upgrade pip
python -m pip list
<img width="591" height="211" alt="image" src="https://github.com/user-attachments/assets/3c447b7f-e9aa-4479-b420-981f26725760" />



python -m pip install requests
python -m pip install requests>=1.0,<=2.0 (This will not be run as I do not want to downgrade)
python -m pip install requests==2.22.0    (This will not be run as I do not want to downgrade)
python -m pip show requests
<img width="590" height="496" alt="image" src="https://github.com/user-attachments/assets/b3e244cf-1bc0-443e-802f-d70c5a8237d7" />



python -m pip uninstall requests
Also do uninstall dependencies, we have to do so individually
python -m pip uninstall certifi chardet idna urllib3
<img width="623" height="185" alt="image" src="https://github.com/user-attachments/assets/a6bf69a8-ed4e-4b4b-bb85-5a3823d4f717" />
<img width="254" height="79" alt="image" src="https://github.com/user-attachments/assets/c6b3447d-7ff4-48b4-8ba2-50847aa3ca56" />

