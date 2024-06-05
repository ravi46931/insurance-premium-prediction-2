# Insurance Premium Prediction Application

- This repository represents " Insurance premium prediction according to his/her conditions ".
- With the help of this project we can tell that how much insurance can be get based on the his/her conditons.

## Description

- This is regression project.
- In this project we have used various algorithms as follows: <br>
        **Linear regression**<br>
        <bold>Ridge regression</bold>
        <bold>Lasso regression</bold>
        <bold>Polynomial regression</bold>
        <bold>Random Forest regression</bold>
        <bold>Gradient Boost regression</bold>
        <bold>XGBoost regression</bold>
        <bold>LGBoost regression</bold>
        <bold>CatBoost regression</bold>
- In this project we have <bold>GridSearchCV</bold> to find the best parameters.
- Top best 4 models picked according to the <bold>training set</bold>.
- Finally the best model is picked, that best performs on the <bold>test set</bold> out of these 4 models.
- The source code from data ingestion to model pusher is written in `src` folder in the repo.

## How to run

1. Create a new environment

```bash
python -m venv env
```

2. Activate the new environment

```bash
(powershell)
.\env\Scripts\Activate.ps1 
```

3. Install required packages

```bash
pip install -r requirements.txt
```

4. Now run main.py

```bash
python main.py
```

5. Now run the app

```bash
streamlit run app.py
```


## Inference demo

Provide a link and a sample video
and also the link of the HLD documents

## Contributors 👨🏼‍💻

- Ravi Kumar
