<!-- contact.html -->
<form method="post">
    {% csrf_token %}
        <input type="text" name="name" required placeholder="Your name">
            <input type="email" name="email" required placeholder="Your email">
                <textarea name="message" required placeholder="Your message"></textarea>
                    <button type="submit">Submit</button>
                    </form>
                                                                                 ALLOWED_HOSTS = ['yourdomain.com', 'localhost']