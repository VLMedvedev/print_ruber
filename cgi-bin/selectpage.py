#!/usr/bin/env python3
import sys
sys.path.insert(0, "/opt/print_ruber")
import base64
from datetime import datetime
import dbSqliteAlpameter as db
import cgi
import command_scripts
import printpage

def printpages():
    #refrash_page = '< meta http - equiv = "refresh" content = "3" / >
    refrash_page = ''
    tap = db.get_taped()
    material = tap.material
    formula = str(tap.formula)
    name = tap.name
    label = name
    max = db.get_taped_max()
    disable_max = 'disabled'
    if name == "H-Pur | FDA":
        disable_max = ''
        if max == 1:
            label = "H-Pur | MAX"
        else:
            label = name

    sys.stderr.write("C: disable_max = " + str(disable_max))

    button_max_class = 'class="button-basic button-red"'
    if max == 1:
        button_max_class = 'class="button-basic-pressed button-red-pressed"'

    no_formula = "disabled"
    collor = ''
    if material == 'OTHER':
        collor = 'blue'
        bt_material_class_1 = 'class="button-basic-pressed button-blue-pressed"'
        bt_material_class_2 = 'class="button-basic button-yellow"'
        bt_material_class_3 = 'class="button-basic button-red"'
        bt_material_class_4 = 'class="button-basic button-green"'
        bt_material_class_5 = 'class="button-basic button-tomato"'
    elif material == 'PLASTICS':
        collor = 'yellow'
        bt_material_class_1 = 'class="button-basic button-blue"'
        bt_material_class_2 = 'class="button-basic-pressed button-yellow-pressed"'
        bt_material_class_3 = 'class="button-basic button-red"'
        bt_material_class_4 = 'class="button-basic button-green"'
        bt_material_class_5 = 'class="button-basic button-tomato"'
    elif material == 'POLYURETHANES':
        collor = 'red'
        no_formula = ''
        bt_material_class_1 = 'class="button-basic button-blue"'
        bt_material_class_2 = 'class="button-basic button-yellow"'
        bt_material_class_3 = 'class="button-basic-pressed button-red-pressed"'
        bt_material_class_4 = 'class="button-basic button-green"'
        bt_material_class_5 = 'class="button-basic button-tomato"'
    elif material == 'MAX_PUR':
        collor = 'tomato'
        no_formula = ''
        bt_material_class_1 = 'class="button-basic button-blue"'
        bt_material_class_2 = 'class="button-basic button-yellow"'
        bt_material_class_3 = 'class="button-basic button-red"'
        bt_material_class_4 = 'class="button-basic button-green"'
        bt_material_class_5 = 'class="button-basic-pressed button-tomato-pressed"'
    elif material == 'RUBBERS':
        collor = 'green'
        bt_material_class_1 = 'class="button-basic button-blue"'
        bt_material_class_2 = 'class="button-basic button-yellow"'
        bt_material_class_3 = 'class="button-basic button-red"'
        bt_material_class_4 = 'class="button-basic-pressed button-green-pressed"'
        bt_material_class_5 = 'class="button-basic button-tomato"'

    class_name_array = []
    name_array = []
    name_disabled_array = []

    for i in range(9):
        name_disabled_array.append('disabled')
        class_name_array.append('class="button-basic button-'+collor+'"')
        name_array.append('.')

    name_db = db.get_materials_for_type_id(material)
    j = 0
    for n in name_db:
        nam = n.name
        name_array[j] = nam
        name_disabled_array[j] = ''
        if nam == name:
            class_name_array[j] = 'class="button-basic-pressed button-' + collor+'-pressed"'
        j += 1

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
""")
    strr = strr + (f"""
    <div style="text-align:center;">
      <form class="" action="/cgi-bin/selectpage.py" method="post">
        <table width="100%" cellspacing="0" cellpadding="4" border="0" align="center" >
        <tr>
              <td>
                    <h1   style="text-align:center; color:white; font-size: 4.4rem; ">{label}</h1>
              </td >
               <td width="15%">
                    <h1   style="text-align:right; color:white; font-size: 2.4rem; "  {no_formula}>Formula: </h1>
              </td >
              <td width="15%" >
                  <input name="formula" required type="text" value={formula} {no_formula}>
              </td >
             #     <td width="10%" align="center">
             #       <button {button_max_class} type="submit" name="command" value="max" {disable_max}>Max</button >
             # </td>
        </tr>
        </table>
        <table width="100%" cellspacing="0" cellpadding="4" border="0"  >
        <tr>
              <td>
                    <button {class_name_array[8] } type="submit" name="name" value="{name_array[8]}"  {name_disabled_array[8]}>{name_array[8]}</button>
              </td>
              <td>
                    <button {class_name_array[7] } type="submit" name="name" value="{name_array[7]}"  {name_disabled_array[7]}>{name_array[7]}</button>
              </td>
              <td>
                    <button {class_name_array[6] } type="submit" name="name" value="{name_array[6]}"  {name_disabled_array[6]}>{name_array[6]}</button>
              </td>
          </tr>
          <tr>
              <td>
                    <button {class_name_array[5] } type="submit" name="name" value="{name_array[5]}"  {name_disabled_array[5]}>{name_array[5]}</button>
              </td>
              <td>
                    <button {class_name_array[4] } type="submit" name="name" value="{name_array[4]}"  {name_disabled_array[4]}>{name_array[4]}</button>
              </td>
              <td>
                    <button {class_name_array[3] } type="submit" name="name" value="{name_array[3]}"  {name_disabled_array[3]}>{name_array[3]}</button>
              </td>
          </tr>
          <tr>
              <td>
                    <button {class_name_array[2] } type="submit" name="name" value="{name_array[2]}"  {name_disabled_array[2]}>{name_array[2]}</button>
              </td>
              <td>
                    <button {class_name_array[1] } type="submit" name="name" value="{name_array[1]}"  {name_disabled_array[1]}>{name_array[1]}</button>
              </td>
              <td>
                    <button {class_name_array[0] } type="submit" name="name" value="{name_array[0]}"  {name_disabled_array[0]}>{name_array[0]}</button>
              </td>
          </tr>
          </table>
          <table width="100%" cellspacing="0" cellpadding="4" border="0"  >
          <tr>
              <td>
                    <button {bt_material_class_1} width="20%" type="submit" name="material" value="OTHER" >OTHER</button>
              </td>
              <td>
                    <button {bt_material_class_2} width="20%" type="submit" name="material" value="PLASTICS" >PLASTICS</button>
              </td>
              <td>
                    <button {bt_material_class_3} width="20%" type="submit" name="material" value="POLYURETHANES" >POLYURETHANES</button>
              </td>
              <td>
                    <button {bt_material_class_5} width="20%" type="submit" name="material" value="MAX_PUR" >Max H-Pur</button>
              </td>
              <td>
                    <button {bt_material_class_4} width="20%" type="submit" name="material" value="RUBBERS" >RUBBERS</button>
              </td>

          </tr>
          </table>
""")

    strr = strr + (f"""
     <table width="100%" cellspacing="0" cellpadding="16" border="0" align="center" >      
        <tr>      
             <td colspan = "6" align="center">
                  <button class="button-basic button-50 button-green" type="submit" name="command" value="print_page">To Print</button>
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


form = cgi.FieldStorage()
# Get data from fields
if form.getvalue('command'):
    button = form.getvalue('command')
    if button == 'start':
        db.set_refrash(150)
        print(printpages())
    elif button == 'print_page':
        db.set_refrash(1)
        print(printpage.printpages())
    elif button == 'reprint':
        db.set_refrash(1)
        command_scripts.reprint()
    elif button == 'save':
        command_scripts.save_to_1c()
    elif button == 'return':
        db.set_refrash(150)
        print(printpages())
    elif button == 'print_serial':
        in_diam = form.getvalue('in_diam')
        out_diam = form.getvalue('out_diam')
        quantity = form.getvalue('quantity')
        db.set_taped_diam(in_diam, out_diam)
        db.set_refrash(15)
        command_scripts.print_serial(quantity)
        sys.stderr.write("print = " + str(quantity))
        print(printpage.printpages())
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



if form.getvalue('name'):
    name = form.getvalue('name')
    db.set_taped_name(name)
    db.set_refrash(150)
    print(printpages())

if form.getvalue('material'):
    material = form.getvalue('material')
    db.set_taped_material(material)
    db.set_refrash(150)
    print(printpages())

# Get data from fields
if form.getvalue('formula'):
    formula = form.getvalue('formula')
    db.set_taped_formula(formula)

if __name__ == "__main__":
    pass
    #print("jhhjh")
    #print(printpages())
