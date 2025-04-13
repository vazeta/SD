import requests
import xml.etree.ElementTree as ET

class Direction:
  UP = "up"
  DOWN = "down"
  RIGHT = "right"
  LEFT = "left"

class PicassoBot:

  #  Defines the server address
  server_address = "http://localhost:8080"

  def main(self):
    """
    The main function loops asking input from the user.
    - `tiles` -> Lists the positions and colors of all tiles that are not empty
    - `dot x y r g b` -> Paints a dot in position (x, y) with the color (r, g, b)
    - `line x y direction length r g b` -> Draws a line starting from (x, y) in the given direction with length
    """

    print("Choose your command:")
    while True:
      try:
        cmd = input().strip()
        if cmd == "tiles":
          self.print_tiles()
        elif cmd.startswith("dot"):
          cmd_args = cmd.split()
          if len(cmd_args) == 6:
            x, y, r, g, b = map(int, cmd_args[1:])
            if self.paint_dot(x, y, r, g, b):
              print("Painted your dot!")
        elif cmd.startswith("line"):
          cmd_args = cmd.split()
          if len(cmd_args) == 8:
            x, y = map(int, cmd_args[1:3])
            direction = cmd_args[3]
            length, r, g, b = map(int, cmd_args[4:])
            if self.paint_line(x, y, direction, length, r, g, b):
              print("Painted your line!")
        else:
          print("Please choose one of the available commands")
      except (ValueError, IndexError):
        print("Please choose one of the available commands")
      except KeyboardInterrupt:
        print("\nExiting...")
        break

  def print_tiles(self):
    """
    This function gets the board information and pretty prints it in our
    console
    """

    try:
      # Set the URL for the request.
      url = f"{self.server_address}/game/board"

      # The Accept header defines what kind of formats we are interested in.
      # You should play with "*/*", "application/xml" and "application/json"
      # JSON might need a third party library to parse the response.
      # User Agent is the name of your application.
      # User Agent is the name of your application.
      # Some of the most common are Mozilla, Internet Explorer and GoogleBot.
      headers = {"Accept": "application/xml", "User-Agent": "Pablo v1"}

      # Sends the REST request and stores the response
      response = requests.get(url, headers=headers, allow_redirects=False)

      # If we get a Redirect or an Error (3xx, 4xx and 5xx)
      if response.status_code >= 300:
        print(f"Error: {response.status_code}")
        self.debug(response)
        return

      # Gets the XML from the response text. 
      # ElementTree is a way of reading XML files.
      root = ET.fromstring(response.text)

      # Always close the connection when it is no longer necessary
      response.close()

      # here we are checking the document for all the item info
      # filtering for each created element and pretty printing it
      print("===========================================")
      for item in root.findall(".//item"):
        if item.get("created") == "true":
          x = item.get("x")
          y = item.get("y")
          r = item.get("r")
          g = item.get("g")
          b = item.get("b")
          print(f"Tile ({x},{y}) with color ({r}, {g}, {b})")
      print("===========================================")

    # In case of any other failure we print the information back
    except requests.RequestException as e:
      print(f"Request failed: {e}")

  def paint_dot(self, x, y, r, g, b):
    """
    This function paints a dot on the board
    """

    try:
      # Sets the URL for our request in the specified coordinates x, y
      url = f"{self.server_address}/game/board/{x}/{y}"
      # Set heards for our request
      headers = {"Accept": "application/xml", "User-Agent": "Pablo v1"}
      # Set the color information for our new tyle
      data = {"r": r, "g": g, "b": b}
      # Send the request to the server
      response = requests.post(url, headers=headers, data=data)


      # If we get anything that is a redirect, client side or service side error
      # we print out the information for debugging
      if response.status_code >= 300:
        self.debug(response)
        response.close()
        return False
      return True

    # If the request fails for any other reason we print out the debugging information
    except requests.RequestException as e:
      print(f"Request failed: {e}")
      response.close()
      return False

  def paint_line(self, x, y, direction, length, r, g, b):
    """
    This function paints a line in the board game
    """
    cur_x, cur_y = x, y

    # In our case we will paint our line dot by dot
    # by printing a dot and the update the current position
    # in the desired direction  
    for _ in range(length):
      # Paints dot in the current position
      if not self.paint_dot(cur_x, cur_y, r, g, b):
        # Fails if a dot failed to print.
        return False

      # We update the position according to the
      # disired line direction 
      if direction == Direction.UP:
        cur_y -= 1
      elif direction == Direction.DOWN:
        cur_y += 1
      elif direction == Direction.RIGHT:
        cur_x += 1
      elif direction == Direction.LEFT:
        cur_x -= 1
    return True

  def debug(self, response):
    """
    This function is used to debug the resulting code from HTTP connections.
    """

    # Response codes such as 404 or 500 will give you an idea of what is wrong.
    print(f"Response Code: {response.status_code}")

    # The HTTP headers returned from the server
    print("_____ HEADERS _____")
    for key, value in response.headers.items():
      print(f"{key}: {value}")
    
    # The HTTP body returned from the server
    print(f"Body: {response.text}")

if __name__ == "__main__":
  PicassoBot().main()
