
# 🧱 Simple 3-Tier Application with Docker

This is a basic 3-tier web application structured with:

- **Frontend**: A web UI built with Nginx and served as static content.
- **Backend**: A Python Flask API that connects to the database.
- **Database**: PostgreSQL database for storing application data.

The entire stack is containerized using Docker and orchestrated with Docker Compose.

---

## 📦 Project Structure

```
3tier-app/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   └── index.html
├── docker-compose.yml
```

---

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ZaynabMohammed/ITI-Docker-Task.git
   cd 3tier-app
   ```

2. **Start the application**:
   ```bash
   docker compose up --build
   ```

3. Access the app in your browser at:  
   🔗 `http://localhost:8080`

---

## 🛠️ Tech Stack

- **Frontend**: HTML/CSS served with Nginx
- **Backend**: Python + Flask
- **Database**: PostgreSQL
- **Orchestration**: Docker Compose

---

## 🧪 Testing Database Connection

The backend will attempt to connect to the PostgreSQL DB using environment variables:

```python
os.environ["DB_NAME"]
os.environ["DB_USER"]
os.environ["DB_PASS"]
os.environ["DB_HOST"]
```

On success, it returns:  
✅ `Connected to DB!`

On failure, the error is returned as a string.

---

## 🔒 Environment Variables

Edit the `docker-compose.yml` file to customize:

```yaml
DB_NAME: mydb
DB_USER: admin
DB_PASS: secret
DB_HOST: db
```

---

## 📎 Notes

- Make sure Docker and Docker Compose are installed.
- Wait a few seconds for the DB to initialize before backend connects.
- Logs can be viewed using:
  ```bash
  docker compose logs backend
  ```

---

## 📸 Screenshot
![1](1.PNG)
![2](2.PNG)
![3](3.PNG)


