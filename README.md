# ai-automation-python

UI automation framework for [DemoQA](https://demoqa.com) built with **Python**, **Selenium**, and **pytest**.

The project demonstrates a strict layered architecture inspired by Page Object Model best practices:

- **BasePage** — generic Selenium primitives only
- **Page Objects** — page-specific locators and UI interactions
- **Services** — orchestration layer (no Selenium, no assertions)
- **Data layer** — dataclasses and factory functions for test data
- **Tests** — thin assertion-only layer

## Tech Stack

| Tool | Version |
|---|---|
| Python | 3.9+ |
| Selenium | 4.27.1 |
| pytest | 8.3.4 |
| pytest-html | 4.1.1 |
| Allure pytest | 2.13.5 |
| Faker | 37.1.0 |
| python-dotenv | 1.0.1 |
| webdriver-manager | 4.0.2 |

## Project Setup

### 1. Clone and create virtual environment

```bash
git clone https://github.com/elenaalkoli/ai-automation-python.git
cd ai-automation-python
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the project root:

```text
BASE_URL=https://demoqa.com
HEADLESS=true
```

## Running Tests

All tests:

```bash
pytest
```

Headed mode (visible browser):

```bash
HEADLESS=false pytest
```

By marker — regression only:

```bash
pytest -m regression
```

By marker — smoke only:

```bash
pytest -m smoke
```

Specific test file:

```bash
pytest tests/test_text_box.py
```

## Reports

HTML report is generated automatically after each run:

```bash
open reports/report.html
```

Allure report:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Project Structure

```
.
├── api/
│   └── book_store_api.py   # HTTP client for API setup (Repository)
├── core/
│   ├── base_page.py        # Generic Selenium primitives (BasePage)
│   ├── driver_factory.py   # WebDriver factory (Singleton)
│   └── config.py
├── data/
│   ├── text_box_data.py
│   ├── book_store_data.py
│   └── ...
├── pages/
│   ├── text_box_page.py
│   ├── books_page.py
│   └── ...
├── services/
│   ├── base_service.py
│   ├── text_box_service.py
│   ├── book_store_service.py
│   ├── book_store_setup.py
│   ├── search_strategy.py
│   └── ...
├── tests/
│   ├── test_text_box.py
│   ├── test_book_store.py
│   └── ...
├── conftest.py             # pytest fixtures
├── pytest.ini
├── requirements.txt
└── .env
```

## Covered Scenarios

| # | Scenario | Page |
|---|---|---|
| 1 | Text Box — fill and verify output | `/text-box` |
| 2 | Check Box — expand tree and select node | `/checkbox` |
| 3 | Web Tables — CRUD (add, search, edit, delete) | `/webtables` |
| 4 | Browser Windows — new tab and new window | `/browser-windows` |
| 5 | Modal Dialogs — open, verify content, close | `/modal-dialogs` |
| 6 | Sortable — reverse list and grid order via drag | `/sortable` |
| 7 | Draggable — Simple, Axis Restricted, Container Restricted, Cursor Style | `/dragabble` |
| 8 | Book Store — login, add book via API, verify profile, search by title/author, delete | `/books` |

## Architecture Principles

- **BasePage** contains only generic helpers: `find`, `click`, `type`, `is_visible`, `wait_until_invisible`
- **Page Objects** own locators and all Selenium interactions; never import data models
- **Services** orchestrate multi-step flows across page objects and return typed result dataclasses
- **Tests** contain all `assert` statements; call only service methods
- **Fixtures** in `conftest.py` inject page and service instances via pytest dependency injection
- **API layer** (`api/`) isolates HTTP test data setup from UI — bypasses reCAPTCHA via REST API (Repository pattern)

## Design Patterns

| Pattern | Location | Role |
|---|---|---|
| Page Object Model | `pages/` | UI interaction per page |
| Factory | `data/generate_*` functions | Test data generation |
| Facade | `services/` | Hide multi-step flows |
| Singleton | `core/driver_factory.py` | Single WebDriver instance |
| Value Object | frozen dataclasses in `data/` | Immutable test data |
| Repository | `api/book_store_api.py` | Isolate API from UI |
| Strategy | `services/search_strategy.py` | Pluggable search behaviour |
| Builder | `services/book_store_setup.py` | Fluent test precondition setup |
