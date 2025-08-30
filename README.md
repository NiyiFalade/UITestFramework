# 🧪 UI Test Automation Framework

This project is a **test framework** built with [Playwright](https://playwright.dev/), [pytest](https://docs.pytest.org/), and [pytest-bdd](https://pytest-bdd.readthedocs.io/).  

It automates **UI functionality testing** for an e-commerce flow:
- Selecting the **highest-priced item**
- Adding the item to the cart
- Verifying that the **correct item** is in the cart

---

## ✨ Features

- 🔑 Log in to the website  
- 🔍 Search and identify the highest-priced item  
- 🛒 Add item to the shopping cart  
- ✅ Verify correct item is added  

---

## ⚙️ Installation (Local)

1. Clone this repository:

```bash
git clone  https://github.com/NiyiFalade/UITestFramework.git
cd uitestframework
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install
```

---

## 🚀 Running Tests Locally

Run all tests:

```bash
pytest tests/ --alluredir=allure-results
```

Generate and open an Allure report:

```bash
allure serve allure-results
```

Run tests in a specific browser (e.g., Chromium):

```bash
pytest --browser chromium --alluredir=allure-results
```

---

## 🐳 Running with Docker

### 1. Build and run with Docker only

```bash
docker build -t ui-test-framework .
docker run --rm -v $(pwd)/allure-results:/app/allure-results ui-test-framework
```

This will:
- Build the Docker image  
- Run tests inside the container  
- Save results into the `allure-results` folder on your host machine  

After the run, generate and view the Allure report locally:

```bash
allure serve allure-results
```

### 2. Run using docker-compose

```bash
docker-compose up --build
```

This will:
- Build the Docker image  
- Run tests inside the container  
- Mount `allure-results` to the host machine  

View the report:

```bash
allure serve allure-results
```

---

## 📦 Dependencies

All dependencies are managed in `requirements.txt`:

- [playwright](https://playwright.dev/)  
- [pytest](https://docs.pytest.org/)  
- [pytest-bdd](https://pytest-bdd.readthedocs.io/)  
- [allure-pytest](https://docs.qameta.io/allure/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  
- [pytest-playwright](https://pypi.org/project/pytest-playwright/)  
- [pytest-dotenv](https://pypi.org/project/pytest-dotenv/)  

---
<img width="1353" height="679" alt="allurereport" src="https://github.com/user-attachments/assets/1b27b14a-97cb-4418-9da6-2143fcc4d8d1" />

![Alt text](path/to/image.png)
