**📌 Project Name:** ACE EEE Department Web Portal

**📝 Description:**
A Django-based web application designed for the Electrical and Electronics Engineering department to provide easy access to academic resources, syllabus downloads, contact forms, and departmental updates. The platform features a responsive UI built with Bootstrap 5 and integrates backend form handling with secure data storage. It includes role-based access for admins to manage submissions and leverages email notifications for form responses.

**🔹 Key Features:**
* **Dynamic syllabus pages** for all four academic years with download links.
* **Contact form with backend storage** using Django models and admin panel for easy management.
* **Responsive navigation bar & styling** using Bootstrap 5.
* **Email notifications** for new submissions via SMTP.
* **Deployment-ready structure** for hosting with custom domains.

**🛠 Tech Stack:**
* **Backend:** Django 5, Python 3.13
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Other:** Git, GitHub, PythonAnywhere (deployment)

* ACE_EEE_Web_project/setup_instructions.txt
* Create Django project and app
**django-admin startproject ACE_EEE_Web**
**cd ACE_EEE_Web**
**python manage.py startapp department**
* Run migrations and create superuser
**python manage.py makemigrations**
**python manage.py migrate**
**python manage.py createsuperuser**
* Start the server
**python manage.py runserver**

