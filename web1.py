# Version 20250709 @ 16:05
#
def web_page():
    import socket
    from time import sleep
    from machine import deepsleep
    # Configure the web server
    html_header = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Clock Tools</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    width: 80vw;
                    margin: 0;
                    background-color: #a0f0f0;
                    text-align: center;
                }
                .form-container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }
            </style>
        </head>
    """

    html_option_1_1 = html_header + """
    <body>
        <div class="form-container">
        <h3><u>Clock - Check Wifi</u></h3>
        <p><b>WiFi Settings</b></p>
        <p><u>Local IP Address:</u><br>
    """    
    html_option_1_2 = """
        <p><u>Local SSID:</u><br>"""

    html_option_1_3 = """</p>
        <p><u>Local Wi-Fi Password:</u><br>"""

    html_option_1_4 = """<hr>
        <form action="/" method="POST">
        <label for="option">Option:</label>
        <select id="option" name="option">
        <option value="1">Check WiFi</option>
        <option value="2">Edit WiFi</option>
        <option value="3">Clock Extras</option>
        <option value="4" selected>Setup Tools</option>
        <option value="5">Exit Setup</option>
        </select>   
        <br><br>
        <button type="submit">Submit</button><br>
        </form>
        <p><i>Version 0.927 - 27/06/2025</i>
        <br>
        </div>
    </body>
    </html>
    """

    html_option_2_1 = html_header + """
    <body>
        <div class="form-container">
        <h3><u>Clock - Edit Wifi</u></h3>
        <form action="/" method="POST">
        <label for="option">Option:</label><br>
        <select id="option" name="option">
        <option value="1">Check WiFi</option>
        <option value="2" selected >Edit WiFi</option>
        <option value="3">Clock Extras</option>
        <option value="4">Setup Tools</option>
        <option value="5">Exit Setup</option>
        
        </select>
        <br><br><hr><br>
        <label for="option2">SSID:</label><br>
        <textarea name="edit_wifi" rows="1" cols="25">"""
    # The 'cols' value should be atleat 5 more than the expectd txt length (Both SSID & PASSWORD)
    html_option_2_2 = """</textarea>    <br><br>
        <label for="option3">Password:</label><br>
        <textarea name="edit_wifi" rows="1" cols="25">"""
    html_option_2_3 = """</textarea>"""
    html_option_2_4 = """     <br><br><br><hr>
        <button type="submit">Submit</button><br>
        </form>
        <p><i>Version 1.000 - 29/06/2025</i>
        <br>
        </div>
    </body>
    </html>
    """

    html_option_3_1 = html_header + """
    <body>
        <div class="form-container">
        <h3><u>Clock - Clock Extras</u></h3>
        
        <form action="/" method="POST">
        <label for="option">Option:</label><br>
        <select id="option" name="option">
        <option value="1">Check WiFi</option>
        <option value="2">Edit WiFi</option>
        <option value="3" selected>Clock Extras</option>
        <option value="4">Setup Tools</option>
        <option value="5">Exit Setup</option>
        </select>
        <br><br><hr>
        <p><b>Extras Available</b></p>
        <p><u>Day of Week Display</u><br></p>
    """    
    html_option_3_2 = """    
        <p><u>Alarm Clock</u><br></p>
    """    
    html_option_3_3 = """    
        <br><br><hr>
        <button type="submit">Submit</button>
        </form>
        <p><i>Version 1.000 - 29/06/2025</i>
        <br>
        </div>
    </body>
    </html>
    """
    # This is the home page
    html_option_4 = html_header + """
    <body>
        <div class="form-container">
        <h3><u>Clock - Setup Tools</u></h3>
        <p><b>Options Available</b></p>
        <p><u>Option <b>1</b></u><br>Check WiFi.</p>
        <p><u>Option <b>2</b></u><br>Edit WiFi Settings.</p>
        <p><u>Option <b>3</b></u><br>Clock Extras</p>
        <p><u>Option <b>4</b></u><br>Setup Tools.</p>
        <p><u>Option <b>5</b></u><br>Exit Setup.</p>

        <hr>
        <form action="/" method="POST">
        <label for="option">Option:</label><br>
        <select id="option" name="option">
        <option value="1">Check WiFi</option>
        <option value="2">Edit WiFi</option>
        <option value="3">Clock Extras</option>
        <option value="4" selected>Setup Tools</option>
        <option value="5">Exit Setup</option>
        </select>
        <br><br>
        <button type="submit">Submit</button><br>
        </form>
        <p><i>Version 1.000 - 29/06/2025</i>
        <br>
        </div>
    </body>
    </html>
    """
    # Set home page to option 4
    html = html_option_4

    html_option_5 = html_header + """
    <body>
        <div class="form-container">
        <h3><u>Clock - Exit Setup</u></h3>
        
        <form action="/" method="POST">
        <label for="option">Option:</label><br>
        <select id="option" name="option">
        <option value="1">Check WiFi</option>
        <option value="2">Edit WiFi</option>
        <option value="3">Clock Extras</option>
        <option value="4">Setup Tools</option>
        <option value="5"selected>Exit Setup</option>
        </select>
        <br><br><hr>
        <p><b>Exit - No or Yes</b></p>
        
        <label><input type="radio" name="exit_setup" value="no" checked="checked" >No</label>
        <label><input type="radio" name="exit_setup" value="yes">Yes</label>
      
        <br><br><hr>
        <button type="submit">Submit</button>
        </form>
        <p><i>Version 1.000 - 29/06/2025</i>
        <br>
        </div>
    </body>
    </html>
    """
    # End of Option 5

    # Create a socket and bind it to the IP address and port 80
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows soctect reuse from crash
    server.bind(('', 80))
    server.listen(5)
    print('Listening on port 80')

    while True:
       
        try:
            # Accept a client connection
            conn, addr = server.accept()
            print('Client connected from', addr)

            # Receive the request
            request = conn.recv(1024).decode()

            if 'GET /favicon.ico' in request:
               print('Display favicon.ico for PC users')
               FAVICON = b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
               response = FAVICON
           
           # Check if it's a POST request
            if "POST / " in request:
                print('Request:', request)
                headers, body = request.split("\r\n\r\n", 1)
                key = key2 = key3 = "" # Set to "" to prevent errors when not enough data elements posted
                # The above line breaks the request in to 2 bits using the blank line i.e. '\r\n\r\n'
                # That way 'body' has the 'Posted' value
                # Process form data
                # This section further processes the 'Posted' data to key  e.g.option has value 1
                # It also splits the 'Posted' data if more than one item returned
                # To exit from the help pages a Post with no values is generated then display home page
                # If no values are posted set 'option to '4' which causes the Help page to be displayed
                print('Body\n' + body) # See what s posted
                # Allow for upto 3 values to be posted
                post_number = body.count("&") + 1
                # Create empty variables
                SSID_post = PASSWORD_post = pair1 = pair2 = pair3 = option_value = option2_value = option3_value = ""
                # Now process form
                form_data = {}
                if post_number == 1:
                    print('1 Post')
                    pair1 = body
                    key, option_value = pair1.split('=') # splits key and data using the equals sign
                    form_data[key] = option_value
                    
                if post_number == 2:
                    print('2 Posts')
                    pair1, pair2 = body.split('&') # Splits multiple 'Posted' data
                    key, option_value = pair1.split('=') # splits key and data using the equals sign
                    form_data[key] = option_value
                    key2, option2_value = pair2.split('=') # splits key and data using the equals sign
                    form_data[key] = option2_value
                    
                if post_number == 3:
                    print('3 Posts')
                    pair1, pair2, pair3 = body.split('&') # Splits multiple 'Posted' data
                    key, option_value = pair1.split('=') # splits key and data using the equals sign
                    form_data[key] = option_value
                    key2, option2_value = pair2.split('=') # splits key and data using the equals sign
                    form_data[key] = option2_value
                    key3, option3_value = pair3.split('=') # splits key and data using the equals sign
                    form_data[key] = option3_value
                    
                if option_value == "":
                    option_value = 4
                option_value = int(option_value) # makes 'option_value' testable
                
                if option_value == 1:
                    
                    SSID, PASSWORD, local_ip = check_local_wifi()
                    print(SSID, ' ', PASSWORD, ' ', local_ip)
                    
                    if local_ip == 'No WiFi':
                        local_ip = '<p style="color:red;"><b>' + local_ip + '<br>Check Settings</b></p>'
                    else:
                        local_ip = '<p style="color:green;"><b>Wi-Fi Test Okay<br>' + local_ip + '</b></p>'
                    # Now display results of the wifi check
                    html_option_1 = html_option_1_1
                    html_option_1 = html_option_1 + "<p>" + local_ip 
                    html_option_1 = html_option_1 + html_option_1_2
                    html_option_1 = html_option_1 + "<p>" + SSID + "<br>"
                    html_option_1 = html_option_1 + html_option_1_3
                    html_option_1 = html_option_1 + "<p>" + PASSWORD + "<br>"
                    html_option_1 = html_option_1 + html_option_1_4
                    html = html_option_1
                    # print('Display Option 1')
                    
                if option_value == 2:
                  # Rename 'POST'ed values to SSID, PASSWORD
                    if key2 == 'edit_wifi':
                        SSID = option2_value
                        PASSWORD = option3_value
                        SSID = SSID.strip('+')
                        SSID = SSID.strip('%0D%0A')
                        SSID = SSID.rstrip() # Remove neline sequence i.e. \n
                        PASSWORD = PASSWORD.strip('+')
                        PASSWORD = PASSWORD.strip()
                        PASSWORD = PASSWORD.replace("+", " ")
                        PASSWORD = PASSWORD.strip('%0D%0A')
                    else:
                        f = open('config/wifi_config.txt', 'r') 
                        SSID = f.readline()
                        SSID = SSID.rstrip() # Remove neline sequence i.e. \n
                        print('\nReloading SSID - "' + SSID + '"')
                        PASSWORD = f.readline()
                        print('Reloading PASSWORD = "' + PASSWORD + '"')
                        f.close()
                        
                    # Now update wifi_config.txt file
                    f = open('config/wifi_config.txt', 'w') #writing a new file
                    SSID = SSID.strip() # Make sure clean version is writen back
                    SSID = SSID.replace("+", " ")
                    f.write(SSID + "\n")
                    PASSWORD = PASSWORD.strip()
                    f.write(PASSWORD)
                    f.close()
                    print('\nUpdating Wi-Fi Config file\n')
                    
                    html_option_2 = html_option_2_1 + SSID
                    html_option_2 = html_option_2 + html_option_2_2 + PASSWORD
                    html_option_2 = html_option_2 + html_option_2_3
                    html_option_2 = html_option_2 + html_option_2_4
                    html = html_option_2
                  #  print('Display Option 2')

                if option_value == 3:
                    
                    try:
                        f = open('config/day_of_week.txt', 'r') #makes an exception if not exist
                        Data = f.read() 
                        f.close()
                        day_of_week = 'yes'
                        print('dow-yes')
                    except:
                        day_of_week = 'no'# day of week does not exist
                        print('dow-no')
                    
                    try:
                        f = open('config/alarm_clock.txt', 'r') #makes an exception if not exist
                        Data = f.read() 
                        f.close()
                        alarm_clock = 'yes'
                        print('ac - yes')
                    except:
                        alarm_clock = 'no'# alarm clock does not exist
                        print('ac-no')
                        
                    if key2 == 'day_of_week':
                        day_of_week = option2_value
                        if option3_value != "":
                            alarm_clock = option3_value
                        if day_of_week == 'no':
                            try:
                                f = open('config/day_of_week.txt', 'r') #makes an exception if not exist
                                Data = f.read() 
                                f.close()
                                print('kill the dow')
                                os.remove('config/day_of_week.txt')
                                print('killed dow')
                            except:
                                print('Already killed dow')
                       
                        if day_of_week == 'yes':
                            f = open('config/day_of_week.txt', 'w') #writing a new file
                            f.write("yes")
                            f.close()
                            print('made dow')

                        if alarm_clock == 'no':
                            try:
                                f = open('config/alarm_clock.txt', 'r') #makes an exception if not exist
                                Data = f.read() 
                                f.close()
                                print('kill the a.c')
                                os.remove('config/alarm_clock.txt')
                                print('killed a.c')
                            except:
                                print('Already killed a.c')
                       
                        if alarm_clock == 'yes':
                            f = open('config/alarm_clock.txt', 'w') #writing a new file
                            f.write("yes")
                            f.close()
                            print('made alarm')


                    print('Day_of_Week - ' + day_of_week)
                    print('Alarm_Clock - ' + alarm_clock)
                    
                    html_option_3 = html_option_3_1
                    
                    if day_of_week == 'no':
                        html_option_3 = html_option_3  + """
                    <label><input type="radio" name="day_of_week" value="no" checked="checked" >Disabled</label>
                    <label><input type="radio" name="day_of_week" value="yes">Enabled</label>
                    """
                    if day_of_week == 'yes':
                        html_option_3 = html_option_3 + """
                    <label><input type="radio" name="day_of_week" value="no" >Disabled</label>
                    <label><input type="radio" name="day_of_week" value="yes" checked="checked">Enabled</label>
                    """
                    html_option_3 = html_option_3 + html_option_3_2
                    
                    if alarm_clock == 'no':
                        html_option_3 = html_option_3 + """
                    <label><input type="radio" name="alarm_clock" value="no" checked="checked">Disabled</label>
                    <label><input type="radio" name="alarm_clock" value="yes">Enabled</label>
                    """
                    if alarm_clock == 'yes':
                        html_option_3 = html_option_3 + """
                    <label><input type="radio" name="alarm_clock" value="no" >Disabled</label>
                    <label><input type="radio" name="alarm_clock" value="yes" checked="checked">Enabled</label>
                    """
                    html_option_3 = html_option_3 + html_option_3_3
                    
                    html = html_option_3
                 #   print('Display Option 3')
                    
                if option_value == 4:
                    html = html_option_4
                 #   print('Display Option 4')

                if option_value == 5:
                    if key2 == 'exit_setup':
                        exit_setup = option2_value
                        if exit_setup == 'yes':
                            print('Kaa Boom')
                            sleep(2)
                        #    deepsleep(2000)
                    
                    html = html_option_5
                 #   print('Display Option 4')
            
            # Send the response
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(html)

            # Close the connection
            conn.close()
            print('Client disconnected')

        except Exception as e:
            print('Error:', e)
            if 'conn' in locals():
                conn.close()
