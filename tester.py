from app import app
from sqlalchemy.sql import text
from db import db
from flask import render_template, request, redirect
import messages, users
list = messages.get_list()