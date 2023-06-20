import requests
import json
import os
os.chdir(os.path.dirname(__file__))
# f = open("陽明山國家公園url.txt","r")
# url_list = f.readlines()
url_list =[
    "https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m1!2i10!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlDZw%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlGQQ%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlIZw%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlLQQ%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlQQQ%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlSZw%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlVQQ%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlXZw%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUlaQQ%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUliZw%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESBkVnSUllQQ%3D%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlnZ0U%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlqQUU%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlsZ0U%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlvQUU%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlxZ0U%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl0QUU%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl2Z0U%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl5QUU%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUkwZ0U%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUkzQUU%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUk1Z0U%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUk4QUU%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUktZ0U%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUloQUk%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlqZ0k%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUltQUk%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlvZ0k%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlyQUk%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl0Z0k%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl3QUk%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl5Z0k%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUkxQUk%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUkzZ0k%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUk2QUk%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUk4Z0k%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlfQUk%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUloZ00%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlrQU0%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUltZ00%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlwQU0%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlyZ00%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl1QU0%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl3Z00%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUl6QU0%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUkxZ00%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUk0QU0%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUk2Z00%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUk5QU0%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlfZ00%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m2!2i10!3sCAESB0VnTUlpQVE%3D!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81",
]
date_list = []
star_list = []
review_list = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
a ="https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765763519716247371!2y6632645166790586489!2m1!2i10!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1s-dRkZO7oO9iB-Qa23bDwAw!7e81"
for url in url_list:
        text = requests.get(url,headers=headers).text
        pretext = ')]}\'' # 取代特殊字元
        text = text.replace(pretext,' ') # 把字串讀取成json
        soup = json.loads(text)
        for i in range(10):
            try:
                ymd = [""]
                ymd = soup[2][i][14][0][21][6][7][0:3]
                date = str(ymd[0])+"/"+str(ymd[1])+"/"+str(ymd[2])
                star = soup[2][i][4]
                review = soup[2][i][3]
                date_list.append(date)
                star_list.append(star)
                review_list.append(review)
            except:
                pass


#匯出檔案
import pandas as pd
raw_data = {"日期": date_list,"星數":star_list,"評論":  review_list}
df = pd.DataFrame(raw_data,columns=["日期","星數","評論"])
df.to_csv( "陽明山國家公園_reviews.csv",encoding='utf-8-Sig',index=False)




        

