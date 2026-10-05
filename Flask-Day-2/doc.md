flask work flow

1. user(send request from browser) -> 2. route (match) -> 3. flask fun(will execute)
   -> 4. template file(index.html) -> 5. result display on browser
   user -> route -> function -> template -> result
   MVC architecture ?
   M -> Model (Database)
   V -> UI (index.html)
   c -> Controller

---------------
requests 
1. GET   - Get Data
2. POST  - Create Data
3. PUT   - Update Data
4. PATCH - Update Partial Data
5. DELETE- Delete Data

user Information 
i want to update only name field
Name : Ajay
City : Delhi
Phone: 9897563510

Get :- is faster than POST.
POST:- For security purpose



--------------
error message in flask 
 
import flash




{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class=flashes>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
{% block body %}{% endblock %}

contact from done
validation done 
mail send (pending....)
data save into db (pending.......)