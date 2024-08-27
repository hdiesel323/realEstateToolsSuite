from django.shortcuts import render
from django.template import TemplateDoesNotExist, loader
import logging

# Set up logging
logger = logging.getLogger(__name__)

def investment_home(request):
    try:
        logger.info("Attempting to load 'investment_home.html' template.")
        return render(request, 'investment/investment_home.html')
    except TemplateDoesNotExist as e:
        logger.error(f"Template '{e}' does not exist!")
        raise e

def investment_detail(request):
    try:
        logger.info("Attempting to load 'investment_detail.html' template.")
        return render(request, 'investment/investment_detail.html')
    except TemplateDoesNotExist as e:
        logger.error(f"Template '{e}' does not exist!")
        raise e

def investment_list(request):
    try:
        logger.info("Attempting to load 'investment_list.html' template.")
        return render(request, 'investment/investment_list.html')
    except TemplateDoesNotExist as e:
        logger.error(f"Template '{e}' does not exist!")
        raise e

def simple_test(request):
    try:
        logger.info("Attempting to load 'simple_test.html' template.")
        return render(request, 'investment/simple_test.html')
    except TemplateDoesNotExist as e:
        logger.error(f"Template '{e}' does not exist!")
        raise e
