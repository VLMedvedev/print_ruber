#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore", "'cgi' is deprecated", DeprecationWarning)

import sys
sys.path.insert(0, "/home/user/print_ruber")
import base64
from datetime import datetime
import dbSqliteAlpameter as db
import cgi

#import camera_remote
import command_scripts
#import gpio_ametr
import selectpage

def printpages():
    refrash_page = db.get_refrash()
    button_no_print_class = 'class="button-basic button-green"'
    if db.get_not_print() == 1:
        button_no_print_class = 'class="button-basic-pressed button-green-pressed"'
    startedLoadVideo = db.get_startedLoadVideo()
    #startedLoadVideo = 1
    pathimage = "/opt/ametr/image.png"
    data_uri = base64.b64encode(open(pathimage, 'rb').read()).decode('utf-8')

    last_printed = db.get_last_printed()

    if startedLoadVideo == 1:
        button_on_class = 'class="button-basic-pressed button-green-pressed"'
        button_off_class = 'class="button-basic button-red"'
        button_disable = ''
        img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
        html_tag_material = last_printed.name_materiar + '\n'
        html_tag_diam = str(int(last_printed.id_nom)) + "x" + str(int(last_printed.od_nom)) + "x" + str(last_printed.len)
    else:
        button_on_class = 'class="button-basic button-green"'
        button_off_class = 'class="button-basic-pressed button-red-pressed"'
        button_disable = 'disabled'
        img_tag = ''
        html_tag_material = ''
        html_tag_diam = ''

    tap = db.get_taped()
    material = tap.material
    name = tap.name
    formula = str(tap.formula)
    if material == 'POLYURETHANES':
        label = name + ' #'+formula
    else:
        label = name

    max = db.get_taped_max()
    if name == "H-Pur | FDA":
        if max == 1:
            label = "H-Pur | MAX" + ' #'+formula

    strr = "Content-type: text/html\n"
    strr = strr + (f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta http-equiv="no-cache">
    <meta http-equiv="refresh" content="{refrash_page}" /> 
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
        width: 160px;
        height: 70px;
        border: 4px solid lime;
        margin: 0;
        padding: 0;
        background: lime;
         border-radius: 12px;
     }

     .button-basic-pressed {
        background: black;
        border: 4px solid lime;
        color: white;
        font-size: 2.42rem;
        width: 160px;
        height: 70px;
        border: 4px solid lime;
        margin: 0;
        padding: 0;
        border-radius: 12px;
     }

     .button-basic:disabled {
        background: black;
        color: black;
        border: 4px solid black;
        }
     
    .button-50 {width: 50%;}

    .button-red { background-color: red; border: 4px solid red; }
   	.button-green { background-color: green; border: 4px solid green;}
   	.button-brown { background-color: brown; border: 4px solid brown;}
   	.button-yellow { background-color: MediumSeaGreen; border: 4px solid MediumSeaGreen;}
   	.button-blue { background-color: blue; border: 4px solid blue;}
   	.button-magenta { background-color: magenta; border: 4px solid magenta;}

   	.button-red-pressed { border: 4px solid red; }
   	.button-green-pressed { border: 4px solid green;}
   	.button-brown-pressed { border: 4px solid brown;}
   	.button-yellow-pressed { border: 4px solid MediumSeaGreen;}
   	.button-blue-pressed { border: 4px solid blue;}
   	.button-magenta-pressed { border: 4px solid magenta;}
   	
   	.text-label{
   	    text-align:center;
   	    color:white;
   	    font-size: 1.82rem;
   	    margin: 5;
        	padding: 5;
   	}
   	
   	.text-label-yellow{
   	    color:yellow;
   	}
   	
   	.text-label-blue{
   	    color:blue;
   	}
   	
   	
   	.text-label-deleted{
   	    color:white;
   	    text-decoration: line-through;
	    text-decoration-color: red;
   	}

   .checkbox {
        color: white;
        width: 50px;
        height: 50px;
        margin: 0;
        padding: 0;
     }

    </style>
""")
    strr = strr + (f"""
    <div style="text-align:center;">
      <form class="" action="/cgi-bin/scanpage.py" method="post">
 
""")

    strr = strr + (f"""  
       <table width="100%" cellspacing="0" cellpadding="4" border="1" align="center" >

            <tr>   
             <td width="15%">
                    <button  {button_on_class} type="submit" name="command" value="on"  > On </button> 
             </td>
            <td width="15%">     
                    <button  {button_off_class} type="submit" name="command" value="off"  > Off </button>
            </td>            
              <td >
                    <h1  style="text-align:center; color:white; font-size: 3.4rem; " > {label} </h1>
             </td>
              <td width="15%">
                 <button  {button_no_print_class} type="submit" name="command" value="no_print"  >No print</button>
               </td>            
            </tr>
         </table>   
""")

    clone = db.get_clone()
    button_clone_class = 'class="button-basic button-green"'
    if clone == 1:
        button_clone_class = 'class="button-basic-pressed button-green-pressed"'

    strr = strr + (f"""         
              <table width="100%" cellspacing="0" cellpadding="4" border="1" align="center" >
                <tr >
                 <td rowspan="5"  width="85%" align="center" >
                   <!-- <h1   class="text-label" > {html_tag_material} {html_tag_diam} </h1> -->
                       {img_tag}
                    </td>
                     <td width="15%">
                        <button  class="button-basic button-red" type="submit" name="command" value="select"  > Select </button>
                     </td>
                </tr>    
                <tr >
                  <td width="15%">
                        <button  class="button-basic button-green" type="submit" name="command" value="print" {button_disable}  > Print </button>
                  </td>
                 </tr>        
                 <tr >                 
                  <td width="15%">
                         <button  {button_clone_class} type="submit" name="command" value="clone"  >Clone</button> 
                  </td>  
                  <tr >  
                  </tr>
                   <td width="15%">
                         <button  class="button-basic button-blue" type="submit" name="command" value="save"  >Save</button>
                  </td>            
                </tr>               
              </table>     
""")
    log = db.get_log()
    strr = strr + (f"""  
             <table width="100%" cellspacing="0" cellpadding="4" border="1" align="center" >       
                    <td >
                          <h1   class="text-label"  > {log} </h1>
                   </td>
                  </tr>
               </table>   
      """)
    strr = strr + (f"""  
        <table width="100%" cellspacing="0" cellpadding="4" border="1" align="center" >
    """)


    print_epoch32_array = []
    scan_epoch32_array = []
    name_diam_array = []
    class_name_diam_array = []
    print_disable_array = []
    scan_disable_array = []

    count_sc = 0
    last_doc_number = db.get_last_doc_number()
    # cur_sc = db.get_last_s cur_sc         canedQR(last_doc_number)
    cur_sc = db.doc_get_last()
    if cur_sc is not None:
        for sc in cur_sc:
            print_epoch32 = sc.print_epoch32
            print_epoch32_array.append(print_epoch32)
            scan_epoch32 = sc.scan_epoch32
            scan_epoch32_array.append(scan_epoch32)
            if print_epoch32 == 0:
                print_disable_array.append(' disabled')
                date_time = datetime.fromtimestamp(scan_epoch32)
            else:
                print_disable_array.append(' ')
                date_time = datetime.fromtimestamp(print_epoch32)

            d = date_time.strftime("%H:%M:%S-> ")
            #d = date_time.strftime("%M:%S: ")
            name_diam = d + sc.name_materiar + ' ' + sc.diam
            #name_diam = str(sc.print_epoch32) + ' ' + str(sc.scan_epoch32)
            name_diam_array.append(name_diam)
            if scan_epoch32 == 0:
                scan_disable_array.append(' disabled')
            else:
                scan_disable_array.append('')

            #if sc.dels == 1:    cls_label = ' text-label-deleted'
            if scan_epoch32 != 0 and print_epoch32 != 0:
                cls_label = ' text-label-yellow'
            else:
                cls_label = ''
            class_name_diam_array.append(cls_label)

            count_sc += 1

    if count_sc != 12:
        for i in range(count_sc, 12):
            print_epoch32_array.append('0')
            scan_epoch32_array.append('0')
            name_diam_array.append('')
            class_name_diam_array.append('')
            scan_disable_array.append(' disabled')
            print_disable_array.append(' disabled')

    for j in range(12):
        strr = strr + (f"""   
         <tr>    
            <td width="15%">
               <button  class="button-basic button-green" type="submit" name="delete_pr" value="{print_epoch32_array[j]}" {print_disable_array[j]} > Del P</button>
            </td>                  
            <td  align="center">
               <h1   class="text-label {class_name_diam_array[j]}" >{name_diam_array[j]}</h1>
            </td >  
            <td width="15%">
               <button  class="button-basic button-red" type="submit" name="delete_sc" value="{scan_epoch32_array[j]}" {scan_disable_array[j]} > Del S</button>
            </td>
        </tr>
    """)

    strr = strr + ("""             
      </form>
      <br>
    </div>
</body>
</html>
""")

    if refrash_page == 15:
        return ''

    return strr

form = cgi.FieldStorage()
# Get data from fields
if form.getvalue('command'):
    button = form.getvalue('command')
    if button == 'select':
        db.set_refrash(15)
        print(selectpage.printpages())

    elif button == 'print':
        db.set_started(1)
        db.set_refrash(1)

    elif button == 'reprint':
        db.set_refrash(1)
        command_scripts.reprint()

    elif button == 'save':
        command_scripts.save_to_1c()

    elif button == 'on':
        on = db.get_startedLoadVideo()
        if on != 1:
            db.set_not_print(0)
            db.set_startedLoadVideo(1)
            command_scripts.video_on()
    elif button == 'off':
        on = db.get_startedLoadVideo()
        if on == 1:
            db.set_startedLoadVideo(0)
            command_scripts.video_off()
    elif button == 'return':
        formula = form.getvalue('formula')
        db.set_taped_formula(formula)
        db.set_refrash(1)
        #print(selectpagepage.printpages())
    elif button == 'print_serial':
        in_diam = form.getvalue('in_diam')
        out_diam = form.getvalue('out_diam')
        len = form.getvalue('len')
        quantity = form.getvalue('quantity')
        db.set_taped_diam(in_diam, out_diam, len)
        db.set_refrash(15)
        command_scripts.print_serial(quantity)
        print(selectpage.printpages())
    elif button == 'no_print':
        not_pr = db.get_not_print()
        if not_pr == 0:
            db.set_not_print(1)
        else:
            db.set_not_print(0)
        sys.stderr.write("G: not_pr = " + str(not_pr))
    elif button == 'clone':
        clone = db.get_clone()
        if clone == 0:
            db.set_clone(1)
        else:
            db.set_clone(0)
        sys.stderr.write("C: clone = " + str(clone))
    elif button == 'max':
        max = db.get_taped_max()
        if max == 0:
            db.set_taped_max(1)
        else:
            db.set_taped_max(0)
        sys.stderr.write("C: max = " + str(max))
        print(selectpage.printpages())

if form.getvalue('delete_pr'):
    epoch32 = form.getvalue('delete_pr')
    #print(epoch32)
    if epoch32 != 0:
        db.delete_print_log(epoch32)
        db.doc_delete_Print(epoch32)

if form.getvalue('delete_sc'):
    epoch32 = form.getvalue('delete_sc')
    #print(epoch32)
    if epoch32 != 0:
        db.delete_scanedQR(epoch32)
        db.doc_delete_scanedQR(epoch32)

if form.getvalue('name'):
    name = form.getvalue('name')
    db.set_taped_name(name)
    db.set_refrash(15)
    print(selectpage.printpages())

if form.getvalue('material'):
    material = form.getvalue('material')
    db.set_taped_material(material)
    db.set_refrash(15)
    print(selectpage.printpages())

# Get data from fields
if form.getvalue('formula'):
    formula = form.getvalue('formula')
    db.set_taped_formula(formula)

if __name__ == "__main__":
    #print("jhhjh")
    print(printpages())
