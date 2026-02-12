#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/user/print_ruber")
# sys.path.insert(0, "/opt/ametr")
import base64
from datetime import datetime
import dbSqliteAlpameter as db


def printpages():
    # refrash_page = '< meta http - equiv = "refresh" content = "3" / >
    refrash_page = db.get_refrash()
    tap = db.get_taped()
    material = tap.material
    formula = str(tap.formula)
    name = tap.name
    label = name

    #sys.stderr.write("C: disable_max = " + str(disable_max))


    strr = "Content-type: text/html\n"
    strr = strr + (f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta http-equiv="no-cache">
    {refrash_page} 
    <meta charset="utf-8">
    <title>AlpanaMetr</title>
</head>
""")
    strr = strr + ("""
<body bgcolor=black>
    <style media="screen">
    /* Basic Styles */
    .button-basic {
        color: white;
        font-size: 2.42rem;
        width: 100%;
        height: 130px;
        border: 4px solid lime;
        margin: 0;
        padding: 0;
        background: lime;
         border-radius: 12px;
     }

     .button-basic-pressed {
        background: black;
        color: white;
        font-size: 2.42rem;
        width: 100%;
        height: 130px;
        border: 4px solid lime;
        margin: 0;
        padding: 0;
        border-radius: 12px;
     }

     .button-basic:disabled {
        background: black;
        color: black;
        border: 4px solid black;
        margin: 0;
        padding: 0;
        width: 100%;
        height: 150px;
     }

    .button-50 {width: 50%;}

    .button-red { background-color: red; border: 4px solid red; }
    .button-tomato { background-color: tomato; border: 4px solid tomato; }
   	.button-green { background-color: green; border: 4px solid green;}
   	.button-brown { background-color: brown; border: 4px solid brown;}
   	.button-yellow { background-color: MediumSeaGreen; border: 4px solid MediumSeaGreen;}
   	.button-blue { background-color: blue; border: 4px solid blue;}
   	.button-magenta { background-color: magenta; border: 4px solid magenta;}

   	.button-red-pressed { border: 4px solid red; }
   	.button-tomato-pressed { border: 4px solid tomato; }
   	.button-green-pressed { border: 4px solid green;}
   	.button-brown-pressed { border: 4px solid brown;}
   	.button-yellow-pressed { border: 4px solid MediumSeaGreen;}
   	.button-blue-pressed { border: 4px solid blue;}
   	.button-magenta-pressed { border: 4px solid magenta;}

   	.text-label{
   	    text-align:center;
   	    color:white;
   	    font-size: 2.5rem;
   	    margin: 20;
        padding: 20;
   	}

   	.text-label-deleted{
   	    color:white;
   	    text-decoration: line-through;
	    text-decoration-color: red;
   	}

   	     input{
            width: 80%;
            height: 70px;
            border: 2px solid blue;
            text-align:center;
            font-family:courier;
            font-size: 3rem;
            font-style:bold;
        }

    </style>
    <form class="" action="/cgi-bin/selectpage.py" method="post">
""")

    last_printed = db.get_last_printed()
    in_diam = int(last_printed.id_nom)
    out_diam = int(last_printed.od_nom)
    len = last_printed.len
    quantity = 1

    strr = strr + (f"""
    <table width="100%" cellspacing="20" cellpadding="16" border="0" align="center" >
        <tr>    
            <td width="10%" align="center">
                <button class="button-basic button-red" type="submit" name="command" value="return" >To Select</button >
            </td>
        </tr>   
        <tr>
            <td >
                <label   style="text-align:center; color:white; font-size: 2.4rem; "> Serial print custom label </label>
            </td >       
        </tr>     
     </table>
     <table width="100%" cellspacing="0" cellpadding="16" border="0" align="center" >

        <tr>
            <td width="18%" align="right">
               <label   class="text-label "> Inner:</label>
            </td >
              <td width="15%" >
                  <input  style= "font-size: 2.4rem; "  name="in_diam" required type="number" value={in_diam}>
              </td >
              <td width="18%" align="right" >
                    <label   class="text-label "> Outer:</label>
              </td >
              <td width="15%" >
                  <input   style= "font-size: 2.4rem; " name="out_diam" required type="number" value={out_diam}>
              </td >  
              <td width="18%" align="right" >
                    <label   class="text-label "> Len:</label>
              </td >
              <td width="16%" >
                  <input   style= "font-size: 2.4rem; " name="len" required type="number" value={len}>
              </td >       
        </tr>  
        <tr>
              <td colspan = "3" align="right" >
                    <label   style="text-align:right; color:white; font-size: 2.4rem; ">  Quantity : </label>
              </td >
              <td >
                  <input  style="font-size: 2.4rem; " name="quantity" required type="number" value={quantity}>
              </td >    
        </tr>  
        <tr>      
             <td colspan = "6" align="center">
                  <button class="button-basic button-50 button-green" type="submit" name="command" value="print_serial">Print</button>
             </td>              
        </tr>

        </table>


""")
    strr = strr + ("""
      </form>
      <br>
    </div>
  </body>
</html>      
""")

    return strr

if __name__ == "__main__":
    # print("jhhjh")
    pass
    #print(printpages())
