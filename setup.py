from setuptools import find_packages, setup


project = "django-react-oauth"
version = "0.1.0"

setup(
    name=project,
    version=version,
    description="django-react-oauth",
    author="Jakub Szwajka",
    author_email="szwajkajakub@gmail.com",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=[
        "Django==4.1.7",
        "django-webpack-loader==1.8.1",
        "djangorestframework==3.14.0",
        "djangorestframework_simplejwt==5.2.2",
        "dj_rest_auth==3.0.0",
        "gunicorn==20.1.0",
        "python-dotenv==1.0.0",
        "psycopg2==2.9.5",
    ],
    extras_require={"DEV": ["flake8", "isort", "black"]},
    scripts=[],
)
