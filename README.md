STEPS TO RUN

1. Clone the repository
2. make a .env from the example.env and change the DB URL to local machine
3. Run pip3 install -r requirements.txt
4. Run alembic upgrade head
5. FInally. Run the project with uvicorn app.main:app --reload

