from django.apps import AppConfig

class {{cookiecutter.example_app|dookie_format|ToPascalCase}}Config(AppConfig):
    name = '{{cookiecutter.example_app|dookie_format}}'
