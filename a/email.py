
from django.utils.crypto import get_random_string


def activacion(request,nombre,email,clave,tlf):
  import smtplib 
  import requests
  import json
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText
  from email.mime.base import MIMEBase
  from email import encoders
  token = get_random_string(length=96)


  remitente = 'Milec Shop'
  destinatarios = [str(email),'milecshop@gmail.com']
  asunto = 'Activación de Cuenta.'
  #cuerpo = 'Hola '+ companiaNombre +' le envia la factura electronica de venta '+factura + ' adjunta a este correo'
  html = """
      <!DOCTYPE html>
      <html>
        <head>
          <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
          <title></title>
        </head>
        <body>
          <table width="100%" cellpadding="0" cellspacing="0" border="0">
            <tbody><tr>
                <td align="center" valign="top">

                    <table width="640" cellpadding="0" cellspacing="0" border="0" class="m_-1338105764881537276tablewidth">
                        <tbody><tr>
                            <td align="center" valign="top" width="20"><img src="https://ci6.googleusercontent.com/proxy/PfMR25oE_5LHShyqKdI9dbJ4rhG_vEEyeRgB6_FdyumxnV-uxFvkVb_gPYKpFR7VlJd4iTPQh23Pj5n7REmbYTs4Qw=s0-d-e1-ft#https://assets.yumpu.com/v4/img/mails/spacer.gif" width="20" height="1" style="display:block" border="0" alt="" class="CToWUd"></td>
                            <td align="center" valign="top" width="600" class="m_-1338105764881537276container">

                                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                    <tbody><tr>
                                        <td align="left" valign="top" height="35">
                                            <img src="https://ci6.googleusercontent.com/proxy/PfMR25oE_5LHShyqKdI9dbJ4rhG_vEEyeRgB6_FdyumxnV-uxFvkVb_gPYKpFR7VlJd4iTPQh23Pj5n7REmbYTs4Qw=s0-d-e1-ft#https://assets.yumpu.com/v4/img/mails/spacer.gif" width="1" height="35" border="0" class="CToWUd">
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="left" valign="top">
                                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                <tbody><tr>
                                     <!-- FACEBOOK IMAGEN -->
                                                    <td align="left" valign="top" width="95" height="36"><a href="http://localhost:8000/"><img src="https://scontent.feoh1-1.fna.fbcdn.net/v/t1.0-9/157738438_10222526850712395_186877010901833219_n.jpg?_nc_cat=103&ccb=3&_nc_sid=730e14&_nc_eui2=AeEv5smu0bCn8VCGbB5JCMUlHt6afTsr26Ae3pp9OyvboDCju7TuAbSm2GqO1ycYFVY&_nc_ohc=1zDAynqovyYAX_oUtM8&_nc_ht=scontent.feoh1-1.fna&oh=fc5fcd718c2d6f9b81aa3038df4aff99&oe=60673028" width="200" height="200" style="display:block" border="0"></a></td>
                                                </tr>
                                            </tbody></table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="left" valign="top" height="25">
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="left" valign="top" style="border:1px solid #dddddd" bgcolor="#ffffff">

                                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                <tbody><tr>
                                                    <td align="left" valign="top" width="49" class="m_-1338105764881537276whiteborder"><img src="" width="49" height="1" border="0" class="m_-1338105764881537276whiteborder CToWUd"></td>
                                                    <td align="left" valign="top" width="500" class="m_-1338105764881537276tablecontent">

                                                        <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                            <tbody><tr>
                                                                <td align="left" valign="top" height="50"><img src="" width="1" height="50" border="0" class="CToWUd"></td>
                                                            </tr>
                                                            <tr>
                                      <td align="left" valign="top" style="font-size:22px;line-height:28px;color:#333333;font-weight:bold;font-family:Arial,Helvetica,sans-serif"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">¡Bienvenido a Milec Shop!</font></font></td>
                                  </tr>
                                  <tr>
                                      <td height="20" align="left" valign="top"><img src="" width="1" height="20" border="0" class="CToWUd"></td>
                                  </tr>
                                  <tr>
                                      <td align="left" valign="top" style="font-size:14px;line-height:19px;color:#585858;font-family:Arial,Helvetica,sans-serif"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                                          Hola $(nombre), nos complace darle la bienvenida como nuevo miembro.

                                      </font></font></td>
                                  </tr>

                                  <tr>
                                      <td height="30" align="left" valign="top"><img src="" width="1" height="30" border="0" class="CToWUd"></td>
                                  </tr>

                                  <tr>
                                      <td align="left" valign="top" style="font-size:14px;line-height:19px;color:#585858;font-family:Arial,Helvetica,sans-serif"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                                          Después de la activación exitosa, puede iniciar sesión en su cuenta utilizando los siguientes detalles: </font></font><br>
                                          <b><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Dirección de correo electrónico: </font></font></b> <a href="" ><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">$(email) </font></font></a><br>
                                          <b><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Contraseña:</font></font></b><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> $(pass)

                                      </font></font></td>
                                  </tr>

                                  <tr>
                                      <td height="30" align="left" valign="top"><img src="" width="1" height="30" border="0" class="CToWUd"></td>
                                  </tr>
                                  <tr>
                                      <td align="left" valign="top" style="font-size:14px;line-height:19px;color:#585858;font-family:Arial,Helvetica,sans-serif"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                                          Está a solo un paso de poder comprar la mejor ropa, cosmeticos que estan a la moda.
                                      </font></font></td>
                                  </tr>

                                  <tr>
                                      <td height="40" align="left" valign="top"><img src="" width="1" height="30" border="0" class="CToWUd"></td>
                                  </tr>
                                  <tr>
                                      <td align="left" valign="top" style="font-size:16px;line-height:21px;color:#333333;font-family:Arial,Helvetica,sans-serif;font-weight:bold"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Active su cuenta ahora y comience a comprar:
                                      </font></font></td>
                                  </tr>
                                  <tr>
                                      <td height="25" align="left" valign="top"><img src="" width="1" height="25" border="0" class="CToWUd"></td>
                                  </tr>
                                  <tr>
                                      <td align="left" valign="top" height="50">
                                          <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                              <tbody><tr>
                                                  <td align="left" valign="top" width="126" class="m_-1338105764881537276btn-border"><img src="" width="126" height="1" border="0" class="m_-1338105764881537276btn-border CToWUd"></td>
                                                  <td align="center" valign="middle" height="50" width="248" bgcolor="#0082b2" style="font-size:14px;line-height:19px;color:#ffffff;font-family:Arial,Helvetica,sans-serif"><a href="http://localhost:8000/activacion/$(telefono)" style="color:#ffffff;text-decoration:none" ><span style="font-size:14px;line-height:19px;color:#ffffff;font-family:Arial,Helvetica,sans-serif"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ACTIVAR LA CUENTA</font></font></span></a></td>
                                                  <td align="left" valign="top" width="126" class="m_-1338105764881537276btn-border"><img src="" width="126" height="1" border="0" class="m_-1338105764881537276btn-border CToWUd"></td>
                                              </tr>
                                          </tbody></table>
                                      </td>
                                  </tr>
                                  <tr>
                                      <td height="25" align="left" valign="top"><img src="https://ci6.googleusercontent.com/proxy/PfMR25oE_5LHShyqKdI9dbJ4rhG_vEEyeRgB6_FdyumxnV-uxFvkVb_gPYKpFR7VlJd4iTPQh23Pj5n7REmbYTs4Qw=s0-d-e1-ft#https://assets.yumpu.com/v4/img/mails/spacer.gif" width="1" height="25" border="0" class="CToWUd"></td>
                                  </tr>
                                  <tr>
                                      
                                  </tr>

                                  <tr>
                                      <td height="30" align="left" valign="top"><img src="" width="1" height="30" border="0" class="CToWUd"></td>
                                  </tr>
                                  <tr>
                                      <td align="left" valign="top" style="font-size:14px;line-height:19px;color:#585858;font-family:Arial,Helvetica,sans-serif"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                                          Gracias por elegir </font></font><a href="http://localhost:8000/" style="text-decoration:none;color:#585858" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.yumpu.com/&amp;source=gmail&amp;ust=1615005895448000&amp;usg=AFQjCNFaDKYiy0D4R5njS7MLyPH8XxL4mg"><span style="text-decoration:none;color:#585858"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Milec Shop</font></font></span></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> . </font><font style="vertical-align: inherit;">¡Disfruta la experiencia! </font></font><br><br>

                                         
                                      </td>
                                  </tr>
                                                            <tr>
                                                                <td align="left" valign="top" height="50"><img src="" width="1" height="50" border="0" class="CToWUd"></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>

                                                </td>
                                                <td align="left" valign="top" width="49" class="m_-1338105764881537276whiteborder"><img src="" width="49" height="1" border="0" class="m_-1338105764881537276whiteborder CToWUd"></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="left" valign="top" height="40"><img src="" width="1" height="40" border="0" class="CToWUd"></td>
                            </tr>
                        </tbody>
                    </table>
                </td>
                <td align="center" valign="top" width="20"><img src="" width="20" height="1" style="display:block" border="0" alt="" class="CToWUd"></td>
            </tr>
            </tbody>
            </table>

                        
                        <table width="640" cellpadding="0" cellspacing="0" border="0" class="m_-1338105764881537276tablewidth">
                            <tbody><tr>
                                <td align="center" valign="top" width="20"><img src="" width="20" height="1" style="display:block" border="0" alt="" class="CToWUd"></td>
                                <td align="center" valign="top" width="600" class="m_-1338105764881537276container">
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                        <tbody><tr>
                                          <!-- FACEBOOK IMAGEN -->
                                            <td align="center" valign="top"><a href="http://localhost:8000"><img src="https://scontent.feoh1-1.fna.fbcdn.net/v/t1.0-9/157738438_10222526850712395_186877010901833219_n.jpg?_nc_cat=103&ccb=3&_nc_sid=730e14&_nc_eui2=AeEv5smu0bCn8VCGbB5JCMUlHt6afTsr26Ae3pp9OyvboDCju7TuAbSm2GqO1ycYFVY&_nc_ohc=1zDAynqovyYAX_oUtM8&_nc_ht=scontent.feoh1-1.fna&oh=fc5fcd718c2d6f9b81aa3038df4aff99&oe=60673028" width="150" height="150" border="0" alt="Logo" class="CToWUd"></a></td>
                                        </tr>
                                        <tr>
                                            <td align="left" valign="top" height="20"><img src="https://ci6.googleusercontent.com/proxy/PfMR25oE_5LHShyqKdI9dbJ4rhG_vEEyeRgB6_FdyumxnV-uxFvkVb_gPYKpFR7VlJd4iTPQh23Pj5n7REmbYTs4Qw=s0-d-e1-ft#https://assets.yumpu.com/v4/img/mails/spacer.gif" width="1" height="20" border="0" class="CToWUd"></td>
                                        </tr>
                                        <tr>
                                        </tr>
                                        <tr>
                                            <td align="left" valign="top" height="20"><img src="" width="1" height="20" border="0" class="CToWUd"></td>
                                        </tr>
                                        <tr>
                                            <td align="center" valign="top">
                                                <table width="100%" cellspacing="0" cellpadding="0" border="0">
                                                    <tbody><tr>
                                                        <td align="center" valign="top" width="265" class="m_-1338105764881537276ft-social-border"><img src="" width="265" height="1" border="0" class="m_-1338105764881537276ft-social-border CToWUd"></td>

                                                        <td align="center" valign="top" width="30"><a href="#FACEBOOK"><img src="https://ci3.googleusercontent.com/proxy/OoWBJGp_H2OY8eaw0Vwir9_RDhSsbghGy7TlE-OVGzJ3dN_Dm4CrlB9Ab0ufT77s4YzBJ5pfG70dIB8lfyCbjqoR5qxDnEa7=s0-d-e1-ft#https://assets.yumpu.com/v4/img/mails/yp-facebook.png" width="30" height="30" style="display:block" border="0" alt="Facebook" class="CToWUd"></a></td>

                                                        <td align="center" valign="top" width="10"><img src="" width="10" height="1" border="0" class="CToWUd"></td>

                                                        <td align="center" valign="top" width="30"><a href="#TIWTTER" ><img src="https://ci4.googleusercontent.com/proxy/G0m-68DRWMoUhyLQn9T3IbLFp4mOdLmI0gTFzZewsDvEhHoxHFhuHCoqQClOPxtmEnZh6TeGSKPc0kCXnTYjdPCp00ZkiEw=s0-d-e1-ft#https://assets.yumpu.com/v4/img/mails/yp-twitter.png" width="30" height="30" style="display:block" border="0" alt="Gorjeo" class="CToWUd"></a></td>

                                                        <td align="center" valign="top" width="265" class="m_-1338105764881537276ft-social-border"><img src="" width="265" height="1" border="0" class="m_-1338105764881537276ft-social-border CToWUd"></td>
                                                    </tr>
                                                </tbody></table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="left" valign="top" height="30"><img src="https://ci6.googleusercontent.com/proxy/PfMR25oE_5LHShyqKdI9dbJ4rhG_vEEyeRgB6_FdyumxnV-uxFvkVb_gPYKpFR7VlJd4iTPQh23Pj5n7REmbYTs4Qw=s0-d-e1-ft#https://assets.yumpu.com/v4/img/mails/spacer.gif" width="1" height="30" border="0" class="CToWUd"></td>
                                        </tr>
                                        <tr>
                                            <td align="center" valign="top" style="font-size:11px;line-height:16px;color:#585858;font-family:Arial,Helvetica,sans-serif"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                                                Copyright © 2021-2030 Evansoft </font></font><br><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                                                Software de ventas basado en la web.
                                            </font></font></td>
                                        </tr>
                                    </tbody></table>
                                </td>
                                <td align="center" valign="top" width="20"><img src="https://ci6.googleusercontent.com/proxy/PfMR25oE_5LHShyqKdI9dbJ4rhG_vEEyeRgB6_FdyumxnV-uxFvkVb_gPYKpFR7VlJd4iTPQh23Pj5n7REmbYTs4Qw=s0-d-e1-ft#https://assets.yumpu.com/v4/img/mails/spacer.gif" width="20" height="1" style="display:block" border="0" alt="" class="CToWUd"></td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody>
            </table>

        </body>
      </html>
  """
  html = html.replace("$(nombre)",nombre)
  html = html.replace("$(telefono)",tlf)
  html = html.replace("$(email)",email)
  html = html.replace("$(pass)",clave)
  # Creamos el objeto mensaje
  mensaje = MIMEMultipart()

  # Establecemos los atributos del mensaje
  mensaje['From'] = remitente
  mensaje['To'] = ", ".join(destinatarios)
  mensaje['Subject'] = asunto

  # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
  #mensaje.attach(MIMEText(cuerpo, 'plain'))
  mensaje.attach(MIMEText(html,'html'))

  sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
  sesion_smtp.starttls()
  sesion_smtp.login('milecshop@gmail.com','milec2425')
  #sesion_smtp.login('facturas.theriosoft@gmail.com','M13rd3r0')
  texto = mensaje.as_string()

  sesion_smtp.sendmail(remitente, destinatarios, texto)
  sesion_smtp.quit()