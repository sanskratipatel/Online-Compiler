# Online-Compiler  



## **1. Python & FastAPI**

* **Why:** FastAPI will be your backend framework to receive code from frontend, execute it, and return output/errors.
* **Topics to learn:**

  * Python basics (variables, functions, I/O)
  * FastAPI:

    * Creating endpoints (`@app.post`, `@app.get`)
    * Request and response models (`Pydantic`)
    * JSON request/response handling
    * Middleware basics (if needed for auth)
* **Hands-on practice:** Create a simple REST API first that just echoes back data sent from frontend.

---

## **2. Docker Basics**  
* **Why:** Docker will run user-submitted code in a **safe isolated container**, supporting multiple languages.
* **Topics to learn:**

  * Docker concepts: Image vs Container
  * Running containers: `docker run`
  * Mounting volumes: `-v host_folder:container_folder`
  * Passing commands: `docker run python:3.12 python /code/main.py`
  * Removing containers: `--rm`
  * Setting resource limits: `--memory`, `--cpus`, `timeout`
* **Hands-on practice:**

  * Run a Python container.
  * Mount a folder with a `.py` file and run it.
  * Try a JS container (`node`) and run a `.js` file.
* **Optional advanced:** Create custom Docker images with preinstalled libraries.

---

## **3. PostgreSQL / Database Basics**

* **Why:** To store user code, generated shareable links, timestamps, language, and optionally user info.
* **Topics to learn:**

  * Creating tables, columns, and relations
  * INSERT, SELECT queries
  * Unique keys (for shareable links)
  * Using SQLAlchemy or Tortoise ORM with FastAPI
* **Hands-on practice:** Create a table for storing code snippets and save/retrieve code.

---

## **4. Frontend Basics (Minimal)**

* **Why:** Even minimal frontend is needed to let users type code, select language, toggle suggestions, and see output.
* **Topics to learn:**

  * HTML: `textarea`, `select`, `button`, `checkbox`
  * JS basics: `fetch` API to call FastAPI endpoints
  * Displaying JSON response in `<pre>` or `<div>`
* **Hands-on practice:** Create a simple page with textarea + run button that sends code to FastAPI and prints output.
---

## **5. Code Execution & Security**

* **Why:** User code can be malicious; understanding execution safety is crucial.
* **Topics to learn:**

  * How to run shell commands safely in Python (`subprocess`)
  * Docker resource limits
  * Timeout handling to prevent infinite loops
  * Prevent access to server file system outside container

---

## **6. Optional: AI / Code Suggestions**

* **Why:** If you want autocomplete or method suggestions.
* **Options:**

  * **Basic:** Use static libraries or language servers per language.
  * **Advanced (AI):** Use OpenAI Codex, ChatGPT, or other AI APIs.
* **Topics to learn:**

  * Calling external APIs from Python
  * Sending code as input and parsing suggested methods
  * Toggle feature (on/off) in frontend and backend

---

## **7. Other Helpful Knowledge**

* **Git/GitHub** → For version control.
* **Basic Linux commands** → Especially if running Docker on Linux server.
* **REST API best practices** → For designing endpoints cleanly.
* **Deployment basics** → Later, for cloud deployment (Docker + FastAPI + PostgreSQL).

---

### **Suggested Learning Order**

1. Python basics
2. FastAPI basics → simple endpoints
3. PostgreSQL basics + ORM integration
4. Docker basics → run code in container
5. Code execution & security concepts
6. Minimal frontend with fetch API
7. Optional: AI integration for code suggestions
8. Deployment and scaling

---

💡 **Tip:** Don’t try to learn everything perfectly before starting. You can **start with a minimal MVP** (Python + FastAPI + Docker Python container + save code in DB) and gradually add features like multi-language support, AI suggestions, and code sharing.

---

If you want, I can make a **step-by-step learning roadmap with resources**, so you can go from zero to building this full online compiler.

Do you want me to make that roadmap?



