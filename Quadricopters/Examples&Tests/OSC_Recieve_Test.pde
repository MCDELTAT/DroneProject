/**
 * OSC_Recieve_Test by Aaron Chamberlain - May 2014
 * Based off of the example oscP5sendreceive by andreas schlegel
 * Sets up a simple OSC server and routes data from three pages to 
 * appropriate locations.
 * oscP5 website at http://www.sojamo.de/oscP5
 */
 
import oscP5.*;
import netP5.*;
  
OscP5 oscP5;
NetAddress myRemoteLocation;

void setup() 
{
  size(400,400);
  frameRate(25);
  /* start oscP5, listening for incoming messages at port 7000 */
  oscP5 = new OscP5(this,7000); //Create the OSC Server on computer. 

  myRemoteLocation = new NetAddress("xxx.xxx.xxx.xxx",9000); //iPhone Definition
}

void draw() 
{
  background(0);  
}

/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) 
{
  /* print the address pattern and the typetag of the received OscMessage */
  String pg1val = "/1";
  String pg2val = "/2";
  String pg3val = "/3";
  
  String FullAddress = theOscMessage.addrPattern();
  //println(" addrpattern: "+theOscMessage.addrPattern());
  String PageAddress = FullAddress.substring(0, 2);
  //println("This the shortened Address: "+PageAddress);
  
  
  //A few if statements to route the pages to different places.
  if (PageAddress.equals(pg1val)) //Address came from page one
  {
    boolean isObjectAddress = false; 
    if (FullAddress != PageAddress) //True iff FullAddress came from an object
    {
      isObjectAddress = true; 
      if (isObjectAddress) //If object address, use it's data.  
      {
        //Print page 1 data recieved
        print("Data from page one: ");
        println(theOscMessage.arguments());
      }
      else 
      {
        //Option: We can notify ourselves that page 1 is active (I.E. Drone1), but no command sent
      }  
    }                                                                                                   
  }
  
  if (PageAddress.equals(pg2val))
  {
    boolean isObjectAddress = false;
    if (FullAddress != PageAddress)
    {
      isObjectAddress = true;
      if (isObjectAddress)
      {
        //Print page 2 data recieved.
        print("Data from page two: ");
        println(theOscMessage.arguments());
      }  
      else 
      {
        //Option: We can notify ourselves that page 2 is active (I.E. Drone2), but no command sent
      }  
    }  
  } 
 
  if (PageAddress.equals(pg3val))
  {
    boolean isObjectAddress = false;
    if (FullAddress != PageAddress)
    {
      isObjectAddress = true;
      if (isObjectAddress)
      {
        //Print page 3 data recieved.
        print("Data from page three: ");
        println(theOscMessage.arguments());
      }  
      else 
      {
        //Option: We can notify ourselves that page 3 is active (I.E. Drone3), but no command sent
      }  
    }  
  }   
}


