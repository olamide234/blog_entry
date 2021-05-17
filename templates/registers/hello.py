# <p>
#     Already have an account?<a href="{% url 'login_user' %}">Log in</a> 
#     <a href="{% url 'login_user' %}">Log in</a> 
# </p>

# <!-- <div>
#                         <a href="{% url 'reset_password' %}">Forgot password?</a>
#                     </div> -->

        # {% if user.is_authenticated %}
        #     <a class="nav-link" href="{% url 'logout' %}">Logout</a>
        # {% else %}
        #     <a class="nav-link" href="{% url 'login' %}">Login</a>
        # {% endif %}