# 🕸️ Spider Web Forum - Django Project

**Spider Web Forum** is a discussion platform inspired by *4chan*, developed with **Django**.  
It allows users to create boards, post messages with text and images, reply to threads, manage user roles, and moderate content.  
Additionally, it integrates modern monitoring and automation tools to enhance development quality and user experience.

---

## 🚀 Main Features

- 🧩 **Board creation and visualization** – organize discussion topics by category.  
- 💬 **Post messages with text and images** – users can create threads or reply with multimedia content.  
- 🧵 **Collapsible reply system** – improves readability within long threads.  
- 🧑‍💻 **User roles:**  
  - `User`  
  - `Forum_Admin`  
  - `Element_Admin`  
- 🔐 **Full authentication system** – registration, login, and password recovery.  
- 🧙‍♂️ **Profile editing and custom avatar upload.**  
- 🛠️ **Admin panel** – manage users, posts, and boards.  
- 🧭 **Optional monitoring with LogRocket** – real-time error and session tracking.  
- ⚙️ **Optional automation with UiPath** – automatic workflows for testing and repetitive tasks.

---

## 🧰 Requirements

- 🐍 Python **3.9 or higher**  
- 📦 **pip**  
- 🌱 **Git**  
- 🧱 **Virtualenv** *(optional but recommended)*  
- 🗄️ **PostgreSQL** or **SQLite** *(default)*

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_user/your_repository.git
   cd your_repository
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

---

## 🧠 Problems and Solutions

| Problem | Solution |
|----------|-----------|
| Logs showed all users as anonymous | Implemented `LogRocket.identify()` to record user ID and properties. |
| Mix of irrelevant or outdated errors | Filtered events by severity and configured alerts for critical errors only. |
| Automation failed due to dynamic elements | Used anchors and custom selectors in UiPath for stability. |
| Inconsistencies in automated login flow | Added controlled delays and step-by-step validations (`Element Exists`, `If`). |

---



📌 **Authors:**  
- *Juan José Tamayo Ospina*  

📚 **Course:** Enterprise Programming Platforms  
🏫 **Submission #2**
