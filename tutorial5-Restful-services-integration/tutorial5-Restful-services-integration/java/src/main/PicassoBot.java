package main;

import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;

public class PicassoBot {

  // Defines the server address
  static String serverAddress = "http://localhost:8080";

  enum Direction {
    UP("up"), DOWN("down"), RIGHT("right"), LEFT("left");
  
    private String dir;
  
    Direction() {
    }
  
    Direction(String dir) {
      this.dir = dir;
    }
  
    public String getDir() {
      return dir;
    }
  
    public void setDir(String dir) {
      this.dir = dir;
    }
  }
  
  public static void main(String[] args) {
    /*
     * The main function just loops asking input from the user.
     * 
     * tiles
     * => Lists the positions and colors of all tiles that are not empty (have been
     * created)
     * 
     * dot x y r g b
     * => Paints a dot in position (x, y) with the color (r, g, b)
     * 
     * line x y direction length r g b
     * => draws a line of 'length' starting in point (x, y), with direction as 'dir'
     * (RIGHT, LEFT, UP, DOWN) and color (r, g, b)
     * 
     */

    PicassoBot picasso = new PicassoBot();

    BufferedReader in = new BufferedReader(new InputStreamReader(
        System.in));

    String cmd;
    System.out.println("Choose your command:");
    try {
      while ((cmd = in.readLine()) != null) {
        if (cmd.equals("tiles")) {
          picasso.printTiles();

        } else if (cmd.startsWith("dot")) {
          String[] cmdArgs = cmd.split(" ");
          if (cmdArgs.length == 6) {
            int x = Integer.parseInt(cmdArgs[1]);
            int y = Integer.parseInt(cmdArgs[2]);
            int r = Integer.parseInt(cmdArgs[3]);
            int g = Integer.parseInt(cmdArgs[4]);
            int b = Integer.parseInt(cmdArgs[5]);

            boolean res = picasso.paintDot(x, y, r, g, b);
            if (res == true) {
              System.out.println("Painted your dot!");
            }
          }

        } else if (cmd.startsWith("line")) {
          String[] cmdArgs = cmd.split(" ");
          if (cmdArgs.length == 8) {
            int x = Integer.parseInt(cmdArgs[1]);
            int y = Integer.parseInt(cmdArgs[2]);
            Direction dir = Direction.valueOf(cmdArgs[3]);
            int length = Integer.parseInt(cmdArgs[4]);
            int r = Integer.parseInt(cmdArgs[5]);
            int g = Integer.parseInt(cmdArgs[6]);
            int b = Integer.parseInt(cmdArgs[7]);

            boolean res = picasso.paintLine(x, y, dir, length, r, g, b);
            if (res == true) {
              System.out.println("Painted your line!");
            }
          }
        } else {
          System.out.println("Please choose one of the available commands");
        }
        System.out.println("Choose your command:");
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

  }

  private void printTiles() {
    try {
      // Initiate the REST client.
      URL url = URI.create(serverAddress + "/game/board").toURL();
      HttpURLConnection connection = (HttpURLConnection) url.openConnection();

      // HTTP Verb. Get requests data from the server.
      connection.setRequestMethod("GET");

      // We are interested in the output
      connection.setDoOutput(true);

      // If there is a 3xx error, we want to know.
      connection.setInstanceFollowRedirects(false);

      // The Accept header defines what kind of formats we are interested in.
      // You should play with "*/*", "application/xml" and "application/json"
      // JSON might need a third party library to parse the response.
      connection.setRequestProperty("Accept", "application/xml");

      // User Agent is the name of your application.
      // Some of the most common are Mozilla, Internet Explorer and GoogleBot.
      connection.setRequestProperty("User-agent", "Pablo v1");
      
      // If we get a Redirect or an Error (3xx, 4xx and 5xx)
      if (connection.getResponseCode() >= 300) {
        // We want more information about what went wrong.
        debug(connection);
      }

      // Response body from InputStream.
      InputSource inputSource = new InputSource(connection.getInputStream());

      // XPath is a way of reading XML files.
      XPathFactory factory = XPathFactory.newInstance();
      XPath xPath = factory.newXPath();

      // here we are querying the document (much like SQL) for all the item tags
      // inside row elements.
      NodeList nodes = (NodeList) xPath.evaluate("/board/row/item", inputSource, XPathConstants.NODESET);
      // The last argument defines the type of result we are looking for. Might be
      // NODESET for a list of Nodes
      // or NODE for a single node.

      // We don't need the connection anymore once we get the nodes.
      connection.disconnect();

      // Pretty printing of output
      System.out.println("===========================================");
      for (int i = 0; i < nodes.getLength(); i++) {
        Node node = nodes.item(i);

        // Fetching the attributes of the item element
        String created = node.getAttributes().getNamedItem("created").getTextContent();

        // We only want to print tiles that have been created and painted
        if ("true".equals(created)) {
          String x = node.getAttributes().getNamedItem("x").getTextContent();
          String y = node.getAttributes().getNamedItem("y").getTextContent();
          String r = node.getAttributes().getNamedItem("r").getTextContent();
          String g = node.getAttributes().getNamedItem("g").getTextContent();
          String b = node.getAttributes().getNamedItem("b").getTextContent();

          System.out.println(String.format("Tile (%s,%s) with color (%s, %s, %s)", x, y, r, g, b));
        }

      }
      System.out.println("===========================================");

    } catch (IOException e) {
      e.printStackTrace();
    } catch (XPathExpressionException e) {
      e.printStackTrace();
    }
  }

  private void debug(HttpURLConnection connection) throws IOException {
    // This function is used to debug the resulting code from HTTP connections.

    // Response code such as 404 or 500 will give you an idea of what is wrong.
    System.out.println("Response Code:" + connection.getResponseCode());

    // The HTTP headers returned from the server
    System.out.println("_____ HEADERS _____");
    for (String header : connection.getHeaderFields().keySet()) {
      System.out.println(header + ": " + connection.getHeaderField(header));
    }

    // If there is an error, the response body is available through the method
    // getErrorStream, instead of regular getInputStream.
    BufferedReader in = new BufferedReader(new InputStreamReader(
        connection.getErrorStream()));
    StringBuilder builder = new StringBuilder();
    String inputLine;
    while ((inputLine = in.readLine()) != null)
      builder.append(inputLine);
    in.close();
    System.out.println("Body: " + builder);
  }

  private boolean paintDot(int x, int y, int r, int g, int b) {
    try {
      URL url = URI.create(serverAddress + "/game/board/" + x + "/" + y).toURL();
      HttpURLConnection connection = (HttpURLConnection) url.openConnection();

      // Let's try to paint a tile and hope that there is no tile there yet
      // Method is now POST for creating a new tile
      connection.setRequestMethod("POST");

      connection.setDoOutput(true);
      connection.setInstanceFollowRedirects(false);
      connection.setRequestProperty("Accept", "application/xml");
      connection.setRequestProperty("User-agent", "Pablo v1");

      // We can use getOutputStream() for passing the values for r, g and b in the
      // request's body
      OutputStream os = connection.getOutputStream();
      os.write(("r=" + r + "&g=" + g + "&b=" + b).getBytes());
      os.flush();

      if (connection.getResponseCode() >= 300) {
        debug(connection);
      } else {
        return true;
      }

    } catch (IOException e) {
      e.printStackTrace();
    }

    return false;

  }

  private boolean paintLine(int x, int y, Direction direction, int length, int r, int g, int b) {
    int curX = x;
    int curY = y;

    for (int i = 0; i < length; i++) {
      // Paint dot by dot
      boolean res = paintDot(curX, curY, r, g, b);

      if (res == false) {
        // Failed to paint one of the dots. Stop here.
        return false;
      }

      // Move according to the direction
      switch (direction) {
        case UP:
          --curY;
          break;
        case DOWN:
          ++curY;
          break;
        case RIGHT:
          ++curX;
          break;
        case LEFT:
          --curX;
          break;
      }
    }
    return true;
  }
}
