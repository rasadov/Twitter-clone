# Twitter-clone
REST API built on FastAPI framework

# Getting Started
1. Clone the repository
```bash
git clone https://github.com/rasadov/Twitter-clone.git
```
2. Install the dependencies
```bash
pip install -r requirements.txt
```
3. Create a `.env` file in the root directory and add the following environment variables
4. Create database tables
```bash
alembic upgrade head
```
5. Run the server
```bash
uvicorn src.main:app --reload
```