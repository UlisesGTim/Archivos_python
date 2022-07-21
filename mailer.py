# The necessary libraries are imported
import smtplib #
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import datetime
#from System.all import Dbstorage

#---------------------------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------------------------




#---------------------------------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------------------------------


#db = Dbstorage()

class Mail():
    
    #-----------------------------------------------------------------------------------------------------------------------------
    def __init__(self, ):
        #Credentials
        self.server = 'local_pc'
        self.email_to = ''
        self.email_from = ''
        self.password = ''
       
        #Set day
        self.__day = (
            ( 
                datetime.datetime.today() - datetime.timedelta( 1 ) 
            ).strftime(
                '%Y%m%d'
            )
        )
    
    #-----------------------------------------------------------------------------------------------------------------------------
    def MailSend( self, ):
        print("-------------------------------------------------------")
        print("           Inicia Proceso de Envío de Mail             ")
        print("-------------------------------------------------------")
        msg = MIMEMultipart()
        msg['From']=self.email_from
        msg['To']=','.join(self.email_to)
        msg['Subject']="Correo de prueba"
        adjunto=MIMEBase("application","octect-stream")
        adjunto.set_payload(open('utilities\mailer\paymentperday_' + self.__day + '.csv',"rb").read())
        adjunto.add_header("content-Disposition", 'attachment', filename='paymentperday_' + self.__day + '.csv')
        msg.attach(adjunto)
        encoders.encode_base64(adjunto) 
        body="""\
        <html>
        <html>
        <head><style>tr:hover {
        background-color: #d3b9eb;
        }
        td {
        text-align: center;
        margin: 8px !important;
        border: hidden;
        }
        th {
        background-color: #8140c2 !important;
        color: #ffffff !important;
        border: hidden;
        }
        table{
            font-family: Vegur, 'PT Sans', Verdana, sans-serif;
            font-size: 12px;    margin: 8px;     width: 300px;   border: hidden;
        }
        table tbody tr td:nth-child(2){
            text-align:center;
        }
        </style>
        </head>
        <body>
            <head>Estimados,</head>
            
            <body>
            <p>Buen día,</p>
                <p>Se adjunta Reporte de PaymentReport por día, al día: """+ (datetime.datetime.today() - datetime.timedelta( 1 ) 
            ).strftime(
                '%d/%m/%Y') + """</p>
                <p>----------------------------------------------------------------------</p>
                <p>""" + db.mailheader() + """</p>
                <p>----------------------------------------------------------------------</p>
                <p>Un saludo</p>
            </body>
        </html>"""
        txtmsg= MIMEText(body,"html")
        msg.attach(txtmsg)
        #
        if self.server == 'local_pc':
            #
            server=smtplib.SMTP( 'smtp.gmail.com', 587 )
            server.starttls()
            server.login( self.email_from, self.password )
        else:
            #
            server = smtplib.SMTP( '10.225.175.239' )
        #
        server.sendmail(self.email_from,self.email_to.split(','),msg.as_string())
        server.quit()
        print("-------------------------------")
        print("            Enviado            ")
        print("-------------------------------")


