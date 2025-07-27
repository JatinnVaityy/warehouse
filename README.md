# Warehouse MVP Project

A Django-based MVP for tracking stock movements and inventory in a small warehouse.

## Features

- Product management (add, edit, delete)
- Stock transactions (in/out, add, delete)
- Inventory summary with current stock per product
- Responsive, professional UI using Tailwind CSS
- Clean code and API design

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JatinnVaityy/warehouse.git
   cd warehouse_mvp_project
   ```

2. **Install dependencies:**
   > **Important:** Replace the contents of `requirements.txt` with:
   ```
   Django>=5.2.4
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   - Main app: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Deployment (Render)

1. **Push your code to GitHub.**
2. **Sign up at [Render](https://render.com/) and create a new Web Service.**
3. **Connect your GitHub repo.**
4. **Set the build command:**
   ```
   pip install -r requirements.txt
   ```
5. **Set the start command:**
   ```
   python manage.py migrate && python manage.py runserver 0.0.0.0:8000
   ```
6. **Set environment variable:**
   ```
   PYTHON_VERSION=3.12
   ```
7. **Update `ALLOWED_HOSTS` in `settings.py` to include your Render URL.**
8. **Deploy and visit your Render URL.**
