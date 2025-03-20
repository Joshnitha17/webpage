pip install Flask
from flask import Flask
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the server time in IST
        ist = pytz.timezone('Asia/Kolkata')
            server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
                username = os.getlogin()  # Get the system username
                    name = "Your Full Name"    # Replace with your full name

                        return f"""
                 …
                                                <pre>
                                                    # You can add the output of 'top' command here.
                                                        </pre>
                                                            """

                                                            if __name__ == "__main__":
                                                                app.run(host='0.0.0.0', port=5000)  # Make it publicly accessible
