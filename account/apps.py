<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
        <style>
                body {
                            font-family: Arial, sans-serif;
                                        text-align: center;
                                                    padding: 50px;
                                                            }
                                                                    h1 {
                                                                                color: #555;
                                                                                        }
                                                                                                p {
                                                                                                            color: #777;
                                                                                                                    }
                                                                                                                        </style>
                                                                                                                        </head>
                                                                                                                        <body>
                                                                                                                            <h1>404 - Page Not Found</h1>
                                                                                                                                <p>The page you're looking for doesn't exist.</p>
                                                                                                                                    <a href="{% url 'home' %}">Go back to homepage</a>
                                                                                                                                    </body>
                                                                                                                                    </html>

                                                                                                                                    DEBUG = False
                                                                                                                                    ALLOWED_HOSTS = ['yourdomain.com', 'localhost']