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

**ACE_EEE_Web_project/setup_instructions.txt**
* **Create Django project and app**
* _django-admin startproject ACE_EEE_Web_
* _cd ACE_EEE_Web_
* _python manage.py startapp department_
* **Run migrations and create superuser**
* _python manage.py makemigrations_
* _python manage.py migrate_
* _python manage.py createsuperuser_
* **Start the server**
* _python manage.py runserver_

