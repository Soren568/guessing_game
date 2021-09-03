            {% if session['guess'] == session['num']: %}
            <div class="bg-danger text-white rounded border border-3 p-5 mb-4" style="--bs-bg-opacity: .75"> 
                Too low!
            </div>
            {% elif session['guess'] > session['num']: %}
            <div class="bg-danger text-white rounded border border-3 p-5 mb-4" style="--bs-bg-opacity: .75"> 
                Too high!
            </div>
            {% else: %}
            <div class="bg-success text-white rounded border border-3 p-5 mb-4" style="--bs-bg-opacity: .75"> 
                You got it!
            </div>
            {% endif %}